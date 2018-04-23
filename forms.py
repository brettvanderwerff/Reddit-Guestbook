from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, Length

class SubmitForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(max=20)])
    message = TextAreaField('Message', validators=[DataRequired(), Length(max=100)])
    recaptcha = RecaptchaField()
