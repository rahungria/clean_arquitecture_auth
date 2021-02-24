import psycopg2


ClientError = (
    psycopg2.IntegrityError,
    psycopg2.DataError
)

ServerError = (
    psycopg2.OperationalError,
    psycopg2.DatabaseError,
    psycopg2.ProgrammingError,
    psycopg2.InternalError
)