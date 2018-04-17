from flask_wtf import Form
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired

class SubmitForm(Form):
    username = StringField('Username', validators=[DataRequired()])
    message = TextAreaField('Message', validators=[DataRequired()])
