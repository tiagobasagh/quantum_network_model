# default libraries 
import csv 

# local libraries
from config import stored_path


def get_data(name):
	data = []
	with open(stored_path.format(name)) as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',')
		for row in csv_reader:
			data.append(row)
	
	return data

def make_list_files(schema_file, inicial, final, intervalo):
	list_files = []
	for N in range(inicial, final, intervalo):
		list_files.append(schema_file.format(N))

	return list_files 

