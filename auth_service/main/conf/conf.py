import dotenv
import os
from pathlib import Path

# TODO Abstract Conf maybe
BASE_DIR = Path('.')
print(BASE_DIR.absolute())
dotenv.load_dotenv(dotenv_path=BASE_DIR/'.env')

try:
    DATABASE = {
        'DBNAME': os.environ['DBNAME'],
        'DBUSER': os.environ['DBUSER'],
        'DBPASSWORD': os.environ['DBPASSWORD'],
        'DBHOST': os.getenv('DBHOST', 'localhost'),
        'DBPORT': os.getenv('DBPORT', 5432),
    }

    SECRET_KEY = os.environ['SECRET_KEY']
    TOKEN_ALG = os.getenv('TOKEN_ALG', 'HS256')
except KeyError as e:
    raise KeyError(f'.env improperly configurated: {e}')
