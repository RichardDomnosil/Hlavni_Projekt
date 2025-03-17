from flask import Blueprint, request, flash, redirect, render_template, url_for
from app.db import db_execute

bp = Blueprint('register', __name__, url_prefix='/register')

@bp.route('/', methods=['GET', 'POST'])
def register():
    """
    Slouží k registraci uživatelů.
    Při POST ověřuje data v DB a přesměrovává, jinak zobrazí formulář.
    :return: Tato funkce slouží k registraci.
    """
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        phone = request.form['phone']

        # SQL dotaz pro kontrolu, zda již existuje uživatelské jméno nebo email
        check_command = "SELECT id FROM users WHERE username = ? OR email = ?"
        check_result = db_execute(check_command, (username, email))

        if check_result:
            flash("Uživatelské jméno nebo email již existuje", "warning")
            return render_template('register.html')

        # Pokud neexistuje, provede registraci uživatele
        insert_command = "INSERT INTO users (username, password, email, phone) VALUES (?, ?, ?, ?)"
        db_execute(insert_command, (username, password, email, phone))

        flash("Registrace úspěšná", "success")
        return redirect(url_for('login.login'))

    return render_template('register.html')
