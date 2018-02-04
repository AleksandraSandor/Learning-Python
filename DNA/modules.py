import time


def save_file(name, file):
	f = open(name, "wb")
	try:
		f.write(bytes(file))
	finally:
		f.close()


def load_file(name):
	f = open(name, "rb")
	try:
		file = f.read()
	finally:
		f.close()
	start_convert_time = time.time()
	file = list(file)
	convert_time = time.time() - start_convert_time
	return file, convert_time


def load_file_char(name):
	f = open(name, "r")
	try:
		file = f.read()
	finally:
		f.close()
	return file


def save_file_char(name, file):
	f = open(name, "w")
	try:
		f.write(str(file))
	finally:
		f.close()
