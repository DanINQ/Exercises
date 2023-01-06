import requests
from read_write_task import *
import re



# + Реализовать следующую логику: получать при помощи requests данные сервиса https://jsonplaceholder.typicode.com/
# (сущность можно выбрать любую, например https://jsonplaceholder.typicode.com/comments),
# выводить в консоль все пары заголовки, сохранять полученный json в файл на диск

def get_jsonplaceholder():
	request = requests.get('https://jsonplaceholder.typicode.com/todos/', {'title':'illo expedita consequatur quia in'})
	body = request.content.decode('utf-8')
	write_to_file('answer.json', body, 'a')

# get_jsonplaceholder()        uncomment me



# + Обратиться с странице https://habrahabr.ru/. Получить текст страницы.
# При помощи регулярных выражений нужно получить все ссылки со страницы на другие.
# Ответить себе на вопрос удобно ли так делать?

def get_habr_links():
	request = requests.get('https://habr.com/ru/all/')
	body = request.content.decode('utf-8')
	links = re.findall(r"https[^)\"']+", body)
	return links

# links = get_habr_links()
# for i in links:               uncomment me
# 	print(i)