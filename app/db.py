import sqlite3
from app import app, login, db
from os import path

from click import command

DB_PATH = "database.sqlite"

def connect_db(db_path=DB_PATH):
    try:
        conn = sqlite3.connect(db_path)
        return conn
    except sqlite3.SQLITE_ERROR:
        print("Error connecting to database")

def create_db(path=DB_PATH):
    conn = connect_db(path)
    script = "scheme.sql"
    with open(script, 'r') as file:
        print(file.read())
        conn.executescript(file.read())
    conn.commit()
    conn.close()

def db_execute(path=DB_PATH):
    conn = connect_db(path)
    result = conn.execute(command)
    conn.commit()
    conn.close()
    return resultYY

