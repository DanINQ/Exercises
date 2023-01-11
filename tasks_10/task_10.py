from flask import Flask, request
import json
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators

app = Flask(__name__)
app.config.update(
    DEBUG=True,
    SECRET_KEY='This key must be secret!',
    WTF_CSRF_ENABLED=False,
)



class SomeForm(FlaskForm):
	email = StringField(label='Email', validators=[validators.DataRequired(), validators.Email(message='Unvalid Email')])
	password = PasswordField(label='Password',
	validators=[validators.Length(min=6, max=20, message='Min password length - 6, max - 20')])
	confirm = PasswordField(label='Confirm password',
	validators=[validators.EqualTo('password', message='Passwords must be equal')])



# 1. По адресу /locales должен возвращаться массив в формате json с тремя локалями: ['ru', 'en', 'it']
@app.route('/locales')
def locales_func():
	locales = ['ru', 'en', 'it']
	a = json.dumps(locales)
	return a



# 2. По адресу /sum/<int:first>/<int:second> должен получать в url-адресе два числа, возвращать их сумму
@app.route('/sum/<int:num1>/<int:num2>')
def sum(num1,num2):
	return str(num1 + num2)



# 3. По адресу /greet/<user_name> должен получать имя пользователя, возвращать текст 'Hello, имя_которое_прислали'
@app.route('/greet/<string:user_name>')
def greet(user_name):
	return 'Hello, ' + user_name



# 4. По адресу /form/user должен принимать POST запрос с параментрами: email, пароль и подтверждение пароля. Необходимо валидировать email, что обязательно присутствует, валидировать пароли, что они минимум 6 символов в длину и совпадают. Возрващать пользователю json вида: 
#  "status" - 0 или 1 (если ошибка валидации),
#  "errors" - список ошибок, если они есть,
#  или пустой список.
@app.route('/form/user', methods=['POST'])
def form_user():
	print(request.form, '\n')
	form = SomeForm(request.form)
	print(form.validate())
	return_value = {'status': 0, 'errors' : [form.errors[i] for i in form.errors]}
	if not form.validate():
		return_value['status'] = 1
	return json.dumps(return_value)



# 5. По адресу /serve/<path:filename> должен возвращать содержимое запрашиваемого файла из папки ./files. Файлы можно туда положить любые текстовые. А если такого нет - 404.
@app.route('/serve/<path:filename>')
def file_return(filename):
	try:
	    with open('files/'+str(filename)) as f:
	    	a = f.read()
	    	return json.dumps(a)
	except FileNotFoundError:
		return ('Unvalid path', 404)


app.run()