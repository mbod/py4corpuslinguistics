def write_list_to_file(file_path, word_list):
	output = open(file_path, mode='w', encoding="utf-8")
	for item in word_list:
		output.write("%s\t%i\n" % (item[0],item[1]))
	output.close()

