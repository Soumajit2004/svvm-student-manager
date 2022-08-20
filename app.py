import os
from functools import wraps

from flask_bootstrap import Bootstrap
from flask import Flask
from flask import render_template, request, redirect, url_for, session
from form import StudentSearchForm
from sql_connections import get_students

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY", os.urandom(32))

bootstrap = Bootstrap(app)


@app.route("/", methods=["GET"])
def dashboard():
    return render_template("dashboard.html", nav_title="Dashboard")


@app.route("/students", methods=["GET"])
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
