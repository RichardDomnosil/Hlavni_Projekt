import sqlite3
from os import path

DB_PATH = "database.sqlite"

def connect_db(db_path=DB_PATH):
    """
    Připojí se k SQLite databázi.
    """
    try:
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row  # Přidáno pro správný přístup k sloupcům
        return conn
    except:
        print("Nepodařilo se připojit k databázi.")
        return None

def create_db(path=DB_PATH):
    """
    Vytvoří databázi podle scheme.sql.
    """
    conn = connect_db(path)
    if conn:
        with open("scheme.sql", "r") as file:
            conn.executescript(file.read())
        conn.commit()
        conn.close()

def db_execute(command, params=False, path=DB_PATH):
    """
    Spustí SQL příkaz a vrátí výsledek.
    """
    conn = connect_db(path)
    result = conn.execute(command, params).fetchall() if params else conn.execute(command).fetchall()
    conn.commit()
    conn.close()
    return result
