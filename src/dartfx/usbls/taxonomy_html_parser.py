import argparse
import dataclasses
from dataclasses import dataclass
import hashlib
import json
import logging
import os
from rdflib import Graph, URIRef, BNode, Literal
from rdflib.namespace import CSVW, DC, DCAT, DCTERMS, DOAP, FOAF, ODRL2, ORG, OWL, \
                           PROF, PROV, RDF, RDFS, SDO, SH, SKOS, SOSA, SSN, TIME, \
                           VOID, XMLNS, XSD
import re
from typing import List


@dataclass
class ConceptReference:
    uri: str = None
    name: str = None
    htmlfile: str = None

@dataclass
class Concept:
    uri: str = None
    name: str = None
    description: str = None
    database: str = None
    mappingfile: str = None
    parent: ConceptReference = None
    children: List[ConceptReference] = None
    htmlfile: str = None

@dataclass
class Stats:
    n_files: int = 0 
    n_skipped: int = 0 
    n_name: int = 0 
    n_description: int = 0 
    n_parent: int = 0 
    n_children: int = 0 
    n_database: int = 0 
    n_mappingfile: int = 0 
stats = Stats()

def remove_nulls(d):
    return {k: v for k, v in d.iteritems() if v is not None}

class CustomJSONEncoder(json.JSONEncoder):
    """JSON encoder with support for @dataclass"""
    def default(self, o):
        if dataclasses.is_dataclass(o):
            return dataclasses.asdict(o)
        return super().default(o)

def uri_from_filename(filename) -> str:
    """Generates an URI based on a hash of the filename"""
    hash = hashlib.md5(filename.encode('utf-8'))
    uri = f"http://bls.gov/taxonomy/{hash.hexdigest()}"
    return uri

def create_graph() -> Graph:
    graph = Graph()
    graph.bind("skos", SKOS)
    return graph

def concept_to_rdf(concept, graph) -> Graph:
    resource = URIRef(concept.uri)
    graph.add((resource, RDF.type, SKOS.Concept))
    graph.add((resource, SKOS.prefLabel, Literal(concept.name)))
    if concept.description:
        graph.add((resource, SKOS.definition, URIRef(concept.description)))
    if concept.parent:
        graph.add((resource, SKOS.broader, URIRef(concept.parent.uri)))
    if concept.children:
        for child in concept.children:
            graph.add((resource, SKOS.narrower, URIRef(child.uri)))

    return graph

def parse_html_file(filepath) -> Concept:
    global stats
    filename = os.path.basename(filepath)
    concept = Concept()
    concept.uri= uri_from_filename(filename)
    concept.htmlfile = filename
    with open(filepath, encoding='cp1252') as fp:
        lines = fp.readlines()
        children = ""
        children_section = False
        for line in lines:
            if children_section: 
                # we're reached the children section
                # remaining lines are all children concept references
                children += line.strip()
            else:
                if line.startswith("Description"):
                    m = re.match("Description:(.*)<br", line)
                    value = m.group(1).strip()
                    if value != ".":
                        stats.n_description += 1
                        concept.description = value
                elif line.startswith("Name"):
                    m = re.match("Name:(.*)<br", line)
                    value = m.group(1).strip()
                    stats.n_name += 1
                    concept.name = value
                elif line.startswith("Database"):
                    m = re.match("Database:(.*)<br", line)
                    value = m.group(1).strip()
                    stats.n_database += 1
                    concept.database = value
                elif line.startswith("Mapping"):
                    m = re.match("Mapping File:(.*)<br", line)
                    value = m.group(1).strip()
                    stats.n_mappingfile += 1
                    concept.mappingfile = value
                elif line.startswith("Parent"):
                    m = re.match("Parent: <a href=\"(.*)\">(.*)</a>", line)
                    filename = m.group(1).strip()
                    name = m.group(2).strip()
                    uri = uri_from_filename(filename)
                    stats.n_parent += 1
                    concept.parent = ConceptReference(uri=uri, htmlfile=filename, name=name)
                elif line.startswith("Children"):
                    children = line[9:].strip()
                    children_section = True
        if children!="": # parse children
            stats.n_children += 1
            concept.children = list()
            children = children.replace("<br />","")
            n_child = 0
            for child in children.split("&nbsp"):
                n_child += 1
                if child != "":
                    m = re.match("<a href=\"(.*)\">(.*)</a>", child)
                    filename = m.group(1).strip()
                    name = m.group(2).strip()
                    uri = uri_from_filename(filename)
                    ref = ConceptReference(uri=uri, htmlfile=filename, name=name)
                    concept.children.append(ref)

    return concept

def main():
    root_dir = args.root
    for entry in os.listdir(root_dir):
        entrypath = os.path.join(root_dir, entry)
        if os.path.isfile(entrypath):
            stats.n_files += 1
            if args.start and stats.n_files < args.start:
                stats.n_skipped += 1
                continue
            logging.debug(f"{stats.n_files}: {entry}")
            concept = parse_html_file(entrypath)
            concept_json = json.dumps(concept, indent=4, cls=CustomJSONEncoder)
            logging.debug(f"\n{concept_json}")
            concept_graph = concept_to_rdf(concept, create_graph())
            logging.debug(f"\n{concept_graph.serialize()}")
        # check limit
        if args.limit and stats.n_files > args.limit:
            logging.info(f"Limit of {args.limit} reached")
            break
        # checkpoint
        if stats.n_files % 1000 == 0:
            logging.info(stats)
    logging.info(stats)

if __name__ == '__main__':
    """Main"""
    script_dir = os.path.dirname(os.path.realpath(__file__))
    parser = argparse.ArgumentParser()
    parser.add_argument("-r","--root", default=os.path.join(script_dir,"../Taxonomy"), help="Taxonomy dump root directory")
    parser.add_argument("-s","--start", type=int, help="Entries to start with")
    parser.add_argument("-l","--limit", type=int, help="Maximun number of entries to process")
    parser.add_argument("-ll","--loglevel", default='INFO', help="Log Level")
    args = parser.parse_args()
    print(args)

    loglevel = getattr(logging, args.loglevel.upper(), None)
    logging.basicConfig(format='%(asctime)s %(levelname)s: %(message)s', level=loglevel)
    
    main()
    
