from functools import wraps
import flask
from flask import Blueprint, request, flash, redirect, render_template, url_for, session
from app.db import db_execute

bp = Blueprint('login', __name__, url_prefix='/login')


def login_required(func):
    """Vyžaduje přihlášení uživatele."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        if "username" not in session:
            flash("Sekce pro přihlášené uživatele", "warning")
            return redirect(url_for("login.login"))
        return func(*args, **kwargs)
    return wrapper


@bp.route('/', methods=['GET', 'POST'])
def login():
    """Zpracování přihlášení uživatele."""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        result = db_execute(
            "SELECT username, role FROM users WHERE username = ? AND password = ?",
            (username, password)
        )

        if result:
            user = result[0]
            session['username'] = user['username']
            session['role'] = user['role']  # ← Uložení role do session
            flash("Login úspěšný", "success")
            return redirect(url_for('index'))
        else:
            flash("Špatné přihlašovací údaje", "warning")

    return render_template('login.html')


@bp.route("/users")
def user_list():
    """Zobrazení všech uživatelů."""
    result = db_execute("SELECT username, role, email FROM users")
    return render_template("user.html", result=result)


@bp.route('/logout')
def logout():
    """Odhlášení uživatele."""
    session.pop('username', None)
    session.pop('role', None)  # ← Odstranění role ze session
    flash("Odhlášeno", "info")
    return redirect(url_for('login.login'))


def log_required():
    """Zastaralé - ověření přihlášení uživatele."""
    if "username" not in session:
        flask.flash("Sekce pouze pro přihlášené uživatele", "warning")
        return redirect(url_for('login.login'))
