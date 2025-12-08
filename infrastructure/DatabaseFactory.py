from infrastructure.DatabaseConnection import DatabaseConnection
from infrastructure.DbConnection import (
    MSSQLConnection,
    OracleConnection,
    PostgreSQLConnection,
)


class DatabaseFactory:
    @staticmethod
    def create_connection(**kwargs) -> DatabaseConnection:
        if kwargs["db_type"] == "oracle":
            return OracleConnection(
                kwargs["host"],
                kwargs["port"],
                kwargs["service_name"],
                kwargs["user"],
                kwargs["password"],
            )
        elif kwargs["db_type"] == "mssql":
            return MSSQLConnection(kwargs["dsn"], kwargs["user"], kwargs["password"])
        elif kwargs["db_type"] == "postgresql":
            return PostgreSQLConnection(
                kwargs["host"], kwargs["db_name"], kwargs["user"], kwargs["password"]
            )
        else:
            raise ValueError(f"Unsupported database type: {kwargs["db_type"]}")
