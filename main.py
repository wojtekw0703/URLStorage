from sys import argv
import sqlite3
from os import getenv
from dotenv import load_dotenv
load_dotenv()


class Database:
    def __init__(self,database_name):
        self.connection = sqlite3.connect(database_name)
        self.cursor = self.connection.cursor()

    def __del__(self):
        self.connection.close()

    def create_table(self, sql: str):
        self.cursor.execute(sql)
        self.connection.commit()

    def insert(self, table, *values):
        self.cursor.execute(f"INSERT INTO {table} VALUES ({','.join(['?' for _ in values])})",values)
        self.connection.commit()

if len(argv) == 2 and argv[1] == "setup":
    print('Tworze tabele')
    db = Database(getenv("DB_NAME"))
    db.create_table('CREATE TABLE urls (id INTEGER PRIMARY KEY AUTOINCREMENT, category TEXT, url TEXT)')

if len(argv) == 4 and argv[1] == 'add':
    print('Dodaje nowy adres url')
    category = argv[2]
    url = argv[3]
    db = Database(getenv("DB_NAME"))
    db.insert('urls', None, category, url)

