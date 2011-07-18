'''
Python for Corpus Linguistics Workshop
University of Birmingham 19 July 2011

Task 1 - Word frequency list for a single file

'''

import re

distribution = {}


# 1. load contents of a file into a string value named text

text = open('../data/GTech_text/articles/GTech13.txt').read()

# 2.split the value into a list of tokens using whitespace as delimitation

forms = text.split()

# 3. apply normalization to tokens in list to:
#    a. transform to lower case

tokens_lower = [item.lower() for item in forms]
 
#    b. remove trailing punctuation

tokens = [re.sub('^\W+|\W+$','', item) for item in tokens_lower]

# 4. get the types

types = set(tokens)

# 5. count the total number of types and tokens and calculate type-token ratio

token_cnt = len(tokens)
type_cnt = len(types)

TTR = (type_cnt / token_cnt) * 100

print("TTR", TTR)


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
freq_dist = sorted(distribution.items, key=lambda x: x[1])




