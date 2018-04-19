from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired

class SubmitForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    message = TextAreaField('Message', validators=[DataRequired()])
