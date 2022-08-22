import wtforms
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, TextAreaField
from wtforms.validators import DataRequired, Length


class StudentSearchForm(FlaskForm):
    name = StringField("Student Name", validators=[DataRequired()])
    submit = SubmitField("Search")


class StudentEditAddForm(FlaskForm):
    name = StringField('Student Name', validators=[DataRequired()])
    grade = IntegerField("Grade", validators=[DataRequired()]),
    roll_no = IntegerField("Roll No", validators=[DataRequired(), Length(max=4)])
    father_name = StringField("Father's Name", validators=[DataRequired()])
    mother_name = StringField("Mother's Name", validators=[DataRequired()])
    father_mobile_no = IntegerField("Father's Mobile No", validators=[DataRequired(), Length(max=10)])
    mother_mobile_no = IntegerField("Mother's Mobile No", validators=[DataRequired(), Length(max=10)])
    address = StringField("Address", validators=[DataRequired(), Length(max=500)]),
    submit = SubmitField("Save")
