from flask import Flask
import os

app = Flask(__name__)

# Просто приветствие
@app.route('/hello')
def frst_def():
	return 'Sup'

# Принимать два числа, возвращать сумму
@app.route("/sum/<path:nums>")
def sec_def(nums):
	nums = nums.split('/')
	try:
		a = int(nums[1]) + int(nums[0])
	except:
		a = "Numbers pls"
	return str(a)

# Принимать три строки, возвращать самую длинную
@app.route('/max_len/<path:strs>')
def max_str_len(strs):
	strings = strs.split('/')
	b = {len(i):i for i in strings}
	a = max(b)
	return b[a]

# Введите путь до файла относительно текущей папки, проверьте, существует ли такой файл. Верните "да" или "нет"
@app.route('/check_path/<path:file_path>')
def check_path(file_path):
	 return str(os.path.exists(file_path))

app.run()