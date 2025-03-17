from flask import Blueprint, request, flash, redirect, render_template, url_for, session
from app.db import db_execute

bp = Blueprint('login', __name__, url_prefix='/login')


@bp.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        command = "SELECT username FROM users WHERE username = ? AND password = ?"
        result = db_execute(command, (username, password))

        if result:
            flash("Login successful", "success")
            session['username'] = username
            return redirect(url_for('index'))
        else:
            flash("Login unsuccessful", "warning")
            return render_template('login.html')

    return render_template('login.html')

@bp.route("/users")
def user_list():
    command = "SELECT username, password FROM users"
    result = db_execute(command)
    return render_template("user.html", result=result)

@bp.route('/logout')
def logout():
    session.pop('username', None)
    flash("You have been logged out", "info")
    return redirect(url_for('login.login'))
