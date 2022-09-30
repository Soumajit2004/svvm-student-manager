import wtforms
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, SelectField
from wtforms.validators import DataRequired, Length, NumberRange


class StudentSearchForm(FlaskForm):
    name = StringField("Student Name", validators=[DataRequired()])
    submit = SubmitField("Search")


class StudentEditAddForm(FlaskForm):
    name = StringField('Student Name', validators=[DataRequired(), Length(min=3, max=100)])
    grade = IntegerField("Grade", validators=[DataRequired(), NumberRange(min=1, max=12)])
    roll_no = IntegerField("Roll No", validators=[DataRequired(), NumberRange(min=1, max=100)])
    father_name = StringField("Father's Name", validators=[DataRequired(), Length(min=3, max=100)])
    mother_name = StringField("Mother's Name", validators=[DataRequired(), Length(min=3, max=100)])
    father_mobile_no = StringField("Father's Mobile No", validators=[DataRequired(), Length(min=10, max=10)])
    mother_mobile_no = StringField("Mother's Mobile No", validators=[DataRequired(), Length(min=10, max=10)])
    address = StringField("Address", validators=[DataRequired(), Length(max=500)])
    submit = SubmitField("Save")


class MarksEditForm(FlaskForm):
    exam_s = StringField("Select Exam")
    sci = IntegerField('Science', validators=[])
    eng = IntegerField('English', validators=[])
    math = IntegerField('Mathematics', validators=[])
    ssc = IntegerField('Social Science', validators=[])
    ben = IntegerField('Bengali', validators=[])
    comp = IntegerField('Computer', validators=[])
    submit = SubmitField("Save")
