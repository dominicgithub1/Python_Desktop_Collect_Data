import oracledb
import pyodbc
import psycopg2
from infrastructure.DatabaseConnection import DatabaseConnection


class OracleConnection(DatabaseConnection):
    def __init__(self, host, port, service_name, user, password):
        self.host = host
        self.port = port
        self.service_name = service_name
        self.user = user
        self.password = password
        self.conn = None

    def connect(self):
        self.conn = oracledb.connect(
            user=self.user,
            password=self.password,
            host=self.host,
            port=self.port,
            service_name=self.service_name,
        )
        print("Đã kết nối Oracle")

    def disconnect(self):
        if self.conn:
            self.conn.close()

    def execute_query(self, query: str, return_cursor: bool = False):
        cursor = self.conn.cursor()
        cursor.execute(query)

        if return_cursor:
            return cursor
        else:
            return cursor.fetchall()


class MSSQLConnection(DatabaseConnection):
    def __init__(self, dsn, user, password):
        self.dsn = dsn
        self.user = user
        self.password = password
        self.conn = None

    def connect(self):
        self.conn = pyodbc.connect(
            f"DSN={self.dsn};UID={self.user};PWD={self.password}"
        )
        print("Đã kết nối MS SQL")

    def disconnect(self):
        if self.conn:
            self.conn.close()

    def execute_query(self, query: str, return_cursor: bool = False):
        cursor = self.conn.cursor()
        cursor.execute(query)

        if return_cursor:
            return cursor
        else:
            return cursor.fetchall()


class PostgreSQLConnection(DatabaseConnection):
    def __init__(self, host, dbname, user, password):
        self.host = host
        self.dbname = dbname
        self.user = user
        self.password = password
        self.conn = None

    def connect(self):
        self.conn = psycopg2.connect(
            host=self.host, dbname=self.dbname, user=self.user, password=self.password
        )
        print("Đã kết nối PostgreSQL")

    def disconnect(self):
        if self.conn:
            self.conn.close()

    def execute_query(self, query: str):
        cursor = self.conn.cursor()
        cursor.execute(query)
        return cursor.fetchall()
