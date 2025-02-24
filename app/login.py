from flask import Blueprint, request, flash, redirect, render_template, url_for

bp = Blueprint('login', __name__, url_prefix='/login')

USERS = {
    "admin": "student",
}

@bp.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in USERS and USERS[username] == password:
            flash("Login successful")
            return redirect(url_for('index'))
            return render_template('index.html', username=username)

        else:
            error = flash("Login unsuccessful", "warning")
            return render_template('login.html', error=error)

    return render_template('login.html')