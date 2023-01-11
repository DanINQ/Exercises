from flask import Flask, request

from threading import Lock
# pip install flask-WTF
from flask_wtf import FlaskForm
from wtforms import StringField, validators
from wtforms.validators import ValidationError
import re, datetime

class ContactForm(FlaskForm):
    name = StringField(label='Name', validators=[
        validators.Length(min=4, max=25)
    ])
    email = StringField(label='E-mail', validators=[
        validators.Length(min=6, max=35),
        validators.Email()
    ])
    job = StringField(label='JOB', validators=[
        validators.Length(min=1, max=35),
        validators.DataRequired()
    ])
    bday = StringField(label='Birthday', validators = [
        validators.Length(min=10, max=15)
    ])

    def validate_job(form, field):                        # Проверяет есть ли переданная работа в списке
        if field.data not in ['IT', 'Bank', 'HR']:
            raise ValidationError("That's not the job we need.")

    def validate_bday(form, field):          # Проверяет совпадает ли переданный месяц рождения с текущим месяцем
        bday_match = re.match(r'\d\d-\d\d-\d{4}', str(field.data))
        if bday_match != None:
            bday_date = bday_match.string
        else:
            raise ValidationError

        month = bday_date.split('-')[1]
        if month != str(datetime.datetime.now().month).rjust(2,'0'):
            raise ValidationError


app = Flask(__name__)
app.config.update(
    DEBUG=True,
    SECRET_KEY='This key must be secret!',
    WTF_CSRF_ENABLED=False,
)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        print(request.form)
        form = ContactForm(request.form)
        print(form.validate())

        if form.validate():
            return ('valid', 200)
        else:
            return ('invalid', 400)

    if request.method == 'GET':
        return 'hello world!', 200


if __name__ == '__main__':
    app.run()
