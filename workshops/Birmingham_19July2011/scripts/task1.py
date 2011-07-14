'''
Python for Corpus Linguistics Workshop
University of Birmingham 19 July 2011

Task 1 - Word frequency list for a single file

'''

import re


# 1. load contents of a file into a string value named text

text = open('../data/simpleGTech_text/articles/young-people-tv-mobiles-net_GTech13_article.txt').read()

# 2.split the value into a list of tokens using whitespace as delimitation

forms = text.split()

# 3. apply normalization to tokens in list to:
#    a. transform to lower case 
#    b. remove trailing punctuation

tokens = [re.sub('^\W+|\W$','',item.lower()) for item in forms]

types = set(tokens)

# 4. count the total number of types and tokens and calculate type-token ratio

token_cnt = len(tokens)
type_cnt = len(types)

# 5. count frequency of selected words
freq_of_the = tokens.count('the')
freq_of_all = tokens.count('all')
freq_of_that = tokens.count('that')
freq_of_internet = tokens.count('internet')



# 6. create a frequency distribution (all types and their token counts)
frequency_dist = [(item,tokens.count(item)) for item in types]


# 7. sort and display a frequency list
#    a. alphabetical
frequency_dist.sort()

#    b. frequency
frequency_dist.sort(key=lambda x:x[1], reverse=True)


# 8. write frequency list out to a file
for item in frequency_dist[0:20]:
    print(item[0],"\t",item[1])

outdir = "../output/wordlists"    

outfile = open(outdir + '/' + 'wordlist_freq.txt','w')
for item in frequency_dist:
    outfile.write("%s\t%i\n" % (item[0],item[1]))
outfile.close()


