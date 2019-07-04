def make_list_files(schema_file, inicial, final, intervalo):
	list_files = []
	for N in range(inicial, final, intervalo):
		list_files.append(schema_file.format(N))

	return list_files 