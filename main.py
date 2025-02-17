from flask import Flask, render_template, request

app = Flask(__name__)

USERS = {
    "admin": "student",
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in USERS and USERS[username] == password:
            return render_template('index.html', username=username)

        else:
            error = "Špatné uživatelské jméno nebo heslo!"
            return render_template('login.html', error=error)

    return render_template('login.html')

@app.route('/index')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
