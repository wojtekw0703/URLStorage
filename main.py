from database import Database
from sys import argv
from os import getenv
from dotenv import load_dotenv
load_dotenv()

def setup():
    print('Tworze tabele')
    db = Database(getenv("DB_NAME"))
    db.create_table('CREATE TABLE urls (id INTEGER PRIMARY KEY AUTOINCREMENT, category TEXT, url TEXT)')

def add(category: str,url: str):
    print('Dodaje nowy adres url')
    db = Database(getenv("DB_NAME"))
    db.insert('urls', None, category, url)

def fetch_categories():
    print('Lista kategorii:')
    db = Database(getenv("DB_NAME"))
    categories = db.fetch_distinct('urls', 'category')
    for name in categories:
        print(name)


def index(category: str):
    print(f'Lista linkow z kategorii {category}:')
    db = Database(getenv("DB_NAME"))
    links = db.fetch_all('urls',category=category)
    for link in links:
        print(link[2])


if len(argv) == 2 and argv[1] == "setup":
    '''
    Initialization of the database
    Usage: python main.py setup
    '''
    setup()

if len(argv) == 2 and argv[1] == 'categories':
    fetch_categories()


if len(argv) == 4 and argv[1] == 'add':
    '''
    Adding new resource
    Usage:  pythonmain.py add http://wojciechwydmuch.com
    '''
    add(category=argv[2],url=argv[3])



if len(argv) == 3 and argv[1] == 'list':
    '''
    Listing resources in category
    Usage: python main.py list podstawy
    '''
    index(category = argv[2])
