# + Реализовать две функции: write_to_file(data) и read_file_data().
# Которые соотвественно: пишут данные в файл и читают данные из файла.

def read_file_data(file):
	with open(file) as f:
		return f.read()

def write_to_file(file, data, mode='w'):
	with open(file, mode=mode) as f:
		f.write(data)
