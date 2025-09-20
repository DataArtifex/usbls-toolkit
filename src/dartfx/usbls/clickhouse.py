
import clickhouse_connect

class ClickhouseServer:
    host: str
    port: int
    user: str
    password: str

    def __init__(self, host="localhost", port=8123, database="default", user="default", password=None):
        self.host = host
        self.port = port
        self.database = database
        self.user = user
        self.password = password