from sqlalchemy import URL, create_engine
from sqlalchemy.orm import sessionmaker

url_object = URL.create(
    drivername = "mssql+pyodbc",
    username = "sa",
    password = "Pass!word",
    host = "host.docker.internal",
    port = "5433",
    database = "sql_app",
    query = {"driver": "ODBC Driver 17 for SQL Server"}
)

engine = create_engine(
    url = url_object
)

SessionLocal = sessionmaker(
  autocommit = False,
  autoflush = False,
  bind = engine
)