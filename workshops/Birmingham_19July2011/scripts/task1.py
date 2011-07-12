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

idx=-1
for i in range(0,freq_of_the):
	idx = tokens.index('the',idx+1)
	#print(' '.join(forms[idx-4:idx]), '\t',forms[idx], '\t', ' '.join(forms[idx+1:idx+5]))

idx=-1
for i in range(0,freq_of_internet):
	idx = tokens.index('internet',idx+1)
	#print(' '.join(forms[idx-4:idx]), '\t',forms[idx], '\t', ' '.join(forms[idx+1:idx+5]))


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

# 9. create a simple index recording word positions
index = {}
for type in types:
    index[type] = [pos for pos, word in enumerate(tokens) if word==type]

# 10. search for a word and produce a simple KWIC display

search_term = "internet"
span = 4

for node in index[search_term]:
    left = ' '.join(forms[max(node-4,0):node])
    right = ' '.join(forms[node+1 : min(node+4,len(forms))])
    print("%s\t%s\t%s" % (left,forms[node],right))
