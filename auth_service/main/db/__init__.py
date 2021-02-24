from .postgres_connection import PostgresConnectionManager
from auth_service.main.conf import conf

psql_connection_manager = PostgresConnectionManager(conf)
