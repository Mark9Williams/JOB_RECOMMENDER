from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms.validators import DataRequired

class ProfileUpdateForm(FlaskForm):
    resume = TextAreaField('Resume', validators=[DataRequired()])
    skills = TextAreaField('Skills', validators=[DataRequired()])
    experience = TextAreaField('Experience', validators=[DataRequired()])
    job_preferences = TextAreaField('Job Preferences', validators=[DataRequired()])
    submit = SubmitField('Update Profile')
