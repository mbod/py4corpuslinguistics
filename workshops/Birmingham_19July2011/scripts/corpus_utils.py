'''
Python for Corpus Linguistics Workshop
University of Birmingham 19 July 2011

Utility functions used in Tasks
'''


def write_list_to_file(file_path, word_list):

	output = open(file_path, mode='w', encoding="utf-8")

	for item in word_list:
		output.write("%s\t%i\n" % (item[0],item[1]))

	output.close()

