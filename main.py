from app import app, login, register, saloon
from app.db import create_db
from os import path

def inicializace_db():
    """Vytvoří databázi, pokud ještě neexistuje."""
    if not path.exists(app.config["DATABASE"]):
        create_db()
        print("Inicializace DB")

def registrace_modulu():
    """Registruje jednotlivé části aplikace (blueprinty)."""
    app.register_blueprint(login.bp)
    app.register_blueprint(register.bp)
    app.register_blueprint(saloon.bp)

def spustit_aplikaci():
    """Spustí Flask aplikaci v debug režimu."""
    app.run(debug=True)

if __name__ == "__main__":
    """Hlavní vstupní bod aplikace."""
    inicializace_db()
    registrace_modulu()
    spustit_aplikaci()
