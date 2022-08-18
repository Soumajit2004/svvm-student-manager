import os
from flask_bootstrap import Bootstrap
from flask import Flask
from flask import render_template, request, redirect, url_for, session
from form import LoginForm
from sql_connections import check_email_exists, check_valid_password, get_user_data

app = Flask(__name__)

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

bootstrap = Bootstrap(app)


@app.route('/')
def home():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()

    if request.method == "POST":
        if check_email_exists(form.email.data):
            if check_valid_password(email=form.email.data, password=form.password.data):
                data = get_user_data(email=form.email.data, password=form.password.data)
                session["logged_in"] = True
                session['id'] = data[0]
                session['name'] = data[1]
                session['email'] = data[2]

                return redirect(url_for("dashboard"))

    return render_template("login.html", form=form)


@app.route("/logout")
def logout():
    session.pop('logged_in', None)
    session.pop('id', None)
    session.pop('name', None)
    session.pop('email', None)

    return redirect(url_for('login'))


@app.route("/dashboard", methods=["GET"])
def dashboard():

    if "logged_in" in session:
        return render_template("dashboard.html", nav_title="Dashboard")

    return redirect(url_for("login"))


if __name__ == '__main__':
    app.run(debug=True)
