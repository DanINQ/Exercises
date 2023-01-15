import os
import random
from flask import Flask, request
from flask_wtf import FlaskForm
from wtforms import validators, IntegerField
from wtforms.validators import ValidationError


random.seed(int(os.environ['FLASK_RANDOM_SEED']))
number = [random.randint(1,10),]


app = Flask(__name__)
app.config.update(DEBUG=True,
	WTF_CSRF_ENABLED=False,
	SECRET_KEY='Secret key innit')


# class SomeForm(FlaskForm):
#     num = IntegerField(label='Number')
# 
#     def validate_num(form, field):
#         if field.data != number[-1]:
#             raise ValidationError


@app.route('/', methods=['GET'])
def get_the_num():
    number.append(random.randint(1,10))
    return 'Number guessed!'


@app.route('/guess', methods=['POST'])
def post_the_num():
    try:
        if int(request.form['num']) > number[-1]:
            return '<'
        elif int(request.form['num']) < number[-1]:
            return '>'
        else:
            number.append(random.randint(1,10))
            return '= New number guessed!'
    except:
        return 'Please enter the correct data!'

    # form = SomeForm(request.form)
    # if form.validate():
    #     number.append(random.randint(1,10))
    #     return 'Right! New number is guessed!'
    # 
    # else:
    #     return 'Wrong!'


app.run()

print(os.environ['FLASK_RANDOM_SEED'])
