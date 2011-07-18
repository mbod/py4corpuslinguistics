'''
Python for Corpus Linguistics Workshop
University of Birmingham 19 July 2011

Task 1 - Word frequency list for a single file

'''

import re
import os
from corpus_utils import *

distribution = {}


# 1. set values for the location of the article directory
article_dir = '../data/GTech_text/articles'
file_name = 'GTech13.txt'

file_path= os.path.join(article_dir, file_name)


# 2. load contents of a file into a string value named text
text = open(file_path, mode='r', encoding='utf-8').read()

# 3.split the value into a list of tokens using whitespace as delimitation
forms = text.split()

# 4. apply normalization to tokens in list to:
#    a. transform to lower case
tokens_lower = [item.lower() for item in forms]
 
#    b. remove trailing punctuation
tokens = [re.sub('^\W+|\W+$','', item) for item in tokens_lower]

# 5. get the types
types = set(tokens)

# 6. count the total number of types and tokens and calculate type-token ratio
token_cnt = len(tokens)
type_cnt = len(types)

TTR = (type_cnt / token_cnt) * 100

print(file_name, type_cnt, token_cnt, TTR)


# 7. create a frequency distribution (all types and their token counts)
for item in types:
	item_freq = tokens.count(item)

	try:
		distribution[item] += item_freq
	except:
		distribution[item] = item_freq

# 8. sort and display a frequency list
#    a. alphabetical
alpha_dist = sorted(distribution.items())

#    b. frequency
freq_dist = sorted(distribution.items(), key=lambda x: x[1])


# 9. write out the frequency lists to the output directory
output_directory = '../output/wordlists'

#    a. output alphabetical wordlist
output_path = os.path.join(output_directory, 'articles_wordlist_alpha.txt')
write_list_to_file(output_path, alpha_dist)

#    b. output alphabetical wordlist
output_path = os.path.join(output_directory, 'articles_wordlist_freq.txt')
write_list_to_file(output_path, freq_dist)
