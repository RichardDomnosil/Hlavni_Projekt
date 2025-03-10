from app import app, login
from app.db import create_db
from os import path
app.register_blueprint(login.bp)

if __name__ == "__main__":
    print(app.config["DATABASE"])
    if not path.exists(app.config["DATABASE"]):
        createdb()
        print ("incializace database")

app.register_blueprint(login.bp)

if __name__ == "__main__":
    app.run(debug=Trues)