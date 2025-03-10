from flask import Blueprint, request, flash, redirect, render_template, url_for
from app.db import db_execute

bp = Blueprint('login', __name__, url_prefix='/login')

USERS = {
    "admin": "student",
}

@bp.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        command = "select username from users where username = ? and password = ?"

        result = db_execute(command, (username, password))

        if username in USERS and USERS[username] == password:
            flash("Login successful")
            return redirect(url_for('index'))
            return render_template('index.html', username=username)

        else:
            error = flash("Login unsuccessful", "warning")
            return render_template('login.html', error=error)

    return render_template('login.html')

@bp.route("/users")
def user_list():
    command = "SELECT username, password FROM users"
    result = db_execute(command)
    return render_template("user.html", result=result)