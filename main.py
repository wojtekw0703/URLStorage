from database import Database
from sys import argv
from os import getenv
from dotenv import load_dotenv
load_dotenv()


if len(argv) == 2 and argv[1] == "setup":
    '''
    Initialization of the database
    Usage: python main.py setup
    '''
    print('Tworze tabele')
    db = Database(getenv("DB_NAME"))
    db.create_table('CREATE TABLE urls (id INTEGER PRIMARY KEY AUTOINCREMENT, category TEXT, url TEXT)')

if len(argv) == 4 and argv[1] == 'add':
    '''
    Adding new resource
    Usage:  pythonmain.py add http://wojciechwydmuch.com
    '''
    print('Dodaje nowy adres url')
    category = argv[2]
    url = argv[3]
    db = Database(getenv("DB_NAME"))
    db.insert('urls', None, category, url)

if len(argv) == 3 and argv[1] == 'list':
    print('Lista linkow z kategorii:')
    category = argv[2]
    db = Database(getenv("DB_NAME"))
    links = db.fetch_all('urls',category=category)
    for link in links:
        print(link)
