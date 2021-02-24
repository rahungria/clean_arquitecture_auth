import psycopg2

from auth_service.main.db.abstract_connection import AbstractConnectionManager

# TODO Abstract interface for connection object
class PostgresConnectionManager(AbstractConnectionManager):
    '''
    class to open, create, serve and close Postgres connections

    conf -- configuration dependency (most external)
    '''
    # TODO pool connections
    def __init__(self, conf):
        self.connection = psycopg2.connect(
            database=conf.DATABASE['DBNAME'],
            user=conf.DATABASE['DBUSER'],
            password=conf.DATABASE['DBPASSWORD'],
            host=conf.DATABASE['DBHOST']
        )

    def close(self):
        self.connection.close()

    def get_connection(self):
        return self.connection
