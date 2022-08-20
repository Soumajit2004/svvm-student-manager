from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, EmailField
from wtforms.validators import DataRequired, URL, Email


class StudentSearchForm(FlaskForm):
    name = StringField("Student Name", validators=[DataRequired()])
    submit = SubmitField("Search")
