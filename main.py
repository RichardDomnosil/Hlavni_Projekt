from app import app, login, register
from app.db import create_db
from os import path

if __name__ == "__main__":
    if not path.exists(app.config["DATABASE"]):  # Pokud DB neexistuje, vytvoří ji
        create_db()
        print("Inicializace DB")

app.register_blueprint(login.bp)
app.register_blueprint(register.bp)

if __name__ == "__main__":
    app.run(debug=True)  # Spuštění aplikace