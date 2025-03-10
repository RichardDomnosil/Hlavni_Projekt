import sqlite3
from app import app, login, db
from os import path

from click import command

DB_PATH = "database.sqlite"

def connect_db(db_path=DB_PATH):
    try:
        conn = sqlite3.connect(db_path)
        return conn
    except:
        print("Nepodařílo se připojit k databázi.")
        return None

def create_db(path=DB_PATH):
    conn = connect_db(path)
    if conn:
        script = "scheme.sql"
        with open(script, "r") as file:
            conn.executescript(file.read())
        conn.commit()
        conn.close()


def db_execute(command, params=False ,path=DB_PATH):
    conn = connect_db(path)
    if params:
        result = conn.execute(command, params).fetchall()
    else:
        result = conn.execute(command).fetchall()
    cursor = conn.cursor()
    result = cursor.execute(command).fetchall()
    conn.commit()
    conn.close()
    return result

