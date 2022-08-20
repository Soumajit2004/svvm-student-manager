import os
from functools import wraps

from flask_bootstrap import Bootstrap
from flask import Flask
from flask import render_template, request, redirect, url_for, session
from form import LoginForm, StudentSearchForm
from sql_connections import check_email_exists, check_valid_password, get_user_data, get_students

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY", os.urandom(32))

bootstrap = Bootstrap(app)


def protected_route(function):
    @wraps(function)
    def decorated_function(*args, **kwargs):
        if "logged_in" in session:
            return function(*args, **kwargs)

        return redirect(url_for("login"))

    return decorated_function


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

    return redirect(request.referrer)


@app.route("/dashboard", methods=["GET"])
@protected_route
def dashboard():
    return render_template("dashboard.html", nav_title="Dashboard")


@app.route("/students", methods=["GET"])
@protected_route
def students():
    form = StudentSearchForm()
    student_class = request.args.get("class")
    student_name = request.args.get("name")

    if student_class:
        all_students = get_students(student_class=student_class)
    elif student_name:
        all_students = get_students(name=student_name)
    else:
        all_students = get_students()

    return render_template("students.html", nav_title="Students", all_students=all_students, form=form)


