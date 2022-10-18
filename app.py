import os
from flask_wtf.csrf import CSRFProtect
from data import sub_codes_map, exam_code_map
from flask_bootstrap import Bootstrap
from flask import Flask
from flask import render_template, request, redirect, url_for, session
from form import StudentSearchForm, StudentEditAddForm, MarksEditForm
from sql_connections import get_students, register_student, validate_new_student, \
    get_student_details, delete_student_sql, update_student_details, update_student_marks

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY", os.urandom(32))

bootstrap = Bootstrap(app)
csrf = CSRFProtect(app)

csrf.init_app(app)


@app.route("/about")
def about():
    return render_template("about.html", nav_title="About Project")


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


@app.route("/students/new", methods=["GET", "POST"])
def new_students():
    form = StudentEditAddForm()

    if request.method == "POST":
        error = "Class and Roll No combination already exists"
        if form.validate_on_submit() & validate_new_student(form.grade.data, form.roll_no.data):
            register_student(name=form.name.data,
                             grade=form.grade.data,
                             father_name=form.father_name.data,
                             mother_name=form.mother_name.data,
                             father_phone=form.father_mobile_no.data,
                             mother_phone=form.mother_mobile_no.data,
                             roll=form.roll_no.data,
                             address=form.address.data)

            return render_template("success.html", nav_title="New Student")
        else:
            if form.errors:
                error = f"{[i for i in form.errors.values()][0][0]}  :  {[i for i in form.errors.keys()][0]}"

        return render_template("student_edit_register.html", nav_title="Register Student", form=form, error=error)

    return render_template("student_edit_register.html", nav_title="Register Student", form=form)


@app.route("/students/<int:student_id>", methods=["GET"])
def student(student_id):
    student_details = get_student_details(student_id)

    return render_template("student_profile.html",
                           data=student_details["details"][0],
                           marks_data=student_details["marks"],
                           exam_codes=exam_code_map,
                           nav_title="Student Profile")


@app.route("/students/<int:student_id>/edit", methods=["GET", "POST"])
def edit_student(student_id):
    student_details = get_student_details(student_id)["details"]
    form = StudentEditAddForm()

    if request.method == "POST":
        error = "An error occurred"
        if form.validate_on_submit():
            update_student_details(student_id=student_id,
                                   name=form.name.data,
                                   father_name=form.father_name.data,
                                   mother_name=form.mother_name.data,
                                   father_phone=form.father_mobile_no.data,
                                   mother_phone=form.mother_mobile_no.data,
                                   address=form.address.data)

            return render_template("success.html", nav_title="New Student")
        else:
            if form.errors:
                error = f"{[i for i in form.errors.values()][0][0]}  :  {[i for i in form.errors.keys()][0]}"

        return render_template("student_edit_register.html",
                               nav_title="Edit Student",
                               form=form,
                               error=error,
                               edit_data=student_details[0])

    return render_template("student_edit_register.html",
                           nav_title="Edit Student",
                           form=form,
                           edit_data=student_details[0])


@app.route("/students/<int:student_id>/edit-marks", methods=["GET", "POST"])
def edit_student_marks(student_id):
    form = MarksEditForm()
    exam = request.args.get("exam")

    if exam is None:
        return redirect(f"/students/{student_id}/edit-marks?exam=mt_1")

    if request.method == "POST":
        update_student_marks(student_id=student_id,
                             exam_id=exam,
                             marks_map=[(sub[0], form.data[sub[0]]) for sub in sub_codes_map])

        return redirect(f"/students/{student_id}/edit-marks?exam={exam}")

    student_details = get_student_details(student_id)

    return render_template("edit_student_marks.html",
                           nav_title="Edit Marks",
                           form=form,
                           sub_codes=sub_codes_map,
                           exam_code=exam_code_map,
                           marks_data=student_details["marks"][str(exam)],
                           selected_exam=exam,
                           data=student_details["details"][0])


@app.route("/students/<int:student_id>/delete", methods=["GET"])
def delete_student(student_id):
    delete_student_sql(student_id)

    return redirect(url_for("students"))


@app.errorhandler(404)
def own_404_page(error):
    return redirect(url_for("students"))
