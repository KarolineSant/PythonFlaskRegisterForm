import os

DBPESSOAL = os.environ.get("DBPESSOAL") # mysql
USERPESSOAL = os.environ.get("USERPESSOAL") # root
PASSPESSOAL = os.environ.get("PASSPESSOAL") # dinossauro12
DBPESSOAL_URL = os.environ.get("DBPESSOAL_URL") # localhost/mais_fit

connect_string = f'{DBPESSOAL}://{USERPESSOAL}:{PASSPESSOAL}@{DBPESSOAL_URL}'
config = {
    'db.url': connect_string,
    'db.echo':'False'
}