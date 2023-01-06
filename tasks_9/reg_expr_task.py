import re
from read_write_task import *


# Задание на regexp. Надо найти дату, имя файла и строку, текст в логах.

file = read_file_data('ParseData.txt')

date = re.findall(r'\d.*\d:\d{2}', file)
print(date, '\n')

string = re.findall(r'[\.a-z]+:\d*', file)
print(string, '\n')

text = re.findall(r'[A-Z]+ [A-Z]+ .+;', file)
print(text, '\n')