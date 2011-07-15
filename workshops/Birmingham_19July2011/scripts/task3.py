'''
Python for Corpus Linguistics Workshop
University of Birmingham 19 July 2011

Task 3 - Word search and KWIC display from a directory of files

'''

import os
import re

# 1. create an empty dictionary named index
index={}
text_list=[]

# 2. set location of input file directory in a value named in_directory
in_directory = '../data/simpleGTech_text/articles'

# 3. create a list named in_files containing all text files in in_directory
in_files = [file for file in os.listdir(in_directory) if file.endswith('.txt')]

# 4. loop over each of the files in in_files
for file_pos,file in enumerate(in_files):
	print('Generating a word list for ', file)

	text = open(os.path.join(in_directory,file)).read()

	# 2.split the value into a list of tokens using whitespace as delimitation

	forms = text.split()
	text_list.append(forms)

	# 3. apply normalization to tokens in list to:
	#    a. transform to lower case 
	#    b. remove trailing punctuation

	tokens = [re.sub('^\W+|\W$','',item.lower()) for item in forms]

	# x. count the total number of types and tokens and calculate type-token ratio

	for token_pos, token in enumerate(tokens): 

		try:
			index[token].append((file_pos,token_pos))
		except:
			index[token] = [(file_pos,token_pos)]


span = 4
search_term = "internet"
search_hits = index[search_term]
number_of_hits = len(search_hits)

for hit_number,hit in enumerate(search_hits):
	file = hit[0]
	node_pos = hit[1]
	node_form = text_list[file][node_pos]

	left = text_list[file][max(0,node_pos-span):node_pos]

	right = text_list[file][node_pos+1:node_pos+1+span]


	print("%i\t%s\t%s\t%s\t%s" % (hit_number,' '.join(left),node_form,' '.join(right), in_files[file]))

'''
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
'''
