'''
Python for Corpus Linguistics Workshop
University of Birmingham 19 July 2011

Task 2 - Word frequency list from a directory of files

'''

import os
import re

# 1. create an empty dictionary named freq_dist
frequency_dist={}

# 2. set location of input file directory in a value named in_directory
in_directory = '../data/simpleGTech_text/articles'

# 3. create a list named in_files containing all text files in in_directory
in_files = [file for file in os.listdir(in_directory) if file.endswith('.txt')]

# 4. loop over each of the files in in_files
for file in in_files:
	print('Generating a word list for ', file)

	text = open(os.path.join(in_directory,file)).read()

	# 2.split the value into a list of tokens using whitespace as delimitation

	forms = text.split()

	# 3. apply normalization to tokens in list to:
	#    a. transform to lower case 
	#    b. remove trailing punctuation

	tokens = [re.sub('^\W+|\W$','',item.lower()) for item in forms if re.match('\w',item)]

	# x. count the total number of types and tokens and calculate type-token ratio

	for token in tokens: 

		try:
			frequency_dist[token] += 1
		except:
			frequency_dist[token] = 1


# 7. sort word list by frequency
frequency_distribution = list(frequency_dist.items())
frequency_distribution.sort(key=lambda x:x[1], reverse=True)


# 8. write frequency list out to a file
for item in frequency_distribution[0:20]:
    print(item[0],"\t",item[1])

out_directory = "../output/wordlists"    

outfile = open(os.path.join(out_directory, 'articles_wordlist_freq.txt'),'w')
for item in frequency_distribution:
    outfile.write("%s\t%i\n" % (item[0],item[1]))
outfile.close()
