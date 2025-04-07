from flask import Blueprint, render_template, request, redirect, flash, url_for, session
from functools import wraps
from app.db import db_execute

saloon_bp = Blueprint("saloon", __name__)

def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if "username" not in session:
            flash("Musíš být přihlášený", "warning")
            return redirect(url_for("login.login"))
        return func(*args, **kwargs)
    return wrapper

# Výpis aut
@saloon_bp.route("/cars")
def show_cars():
    result = db_execute("SELECT * FROM cars")
    return render_template("saloon.html", result=result)

# Přidání auta
@saloon_bp.route("/add-car", methods=["GET", "POST"])
@login_required
def add_car():
    if request.method == "POST":
        brand = request.form["brand"]
        engine = request.form["engine"]
        model = request.form["model"]

        try:
            db_execute("INSERT INTO cars (brand, engine, model) VALUES (?, ?, ?)",
                       (brand, engine, model))
            flash("Auto bylo přidáno.", "success")
        except:
            flash("Nepodařilo se přidat auto (značka už existuje?).", "danger")

        return redirect(url_for("saloon.show_cars"))

    return render_template("add_car.html")

@saloon_bp.route("/delete-car/<int:id>", methods=["POST"])
@login_required
def delete_car(id):
    try:
        db_execute("DELETE FROM cars WHERE id = ?", (id,))
        flash("Auto bylo smazáno.", "success")
    except:
        flash("Chyba při mazání auta.", "danger")
    return redirect(url_for("saloon.show_cars"))