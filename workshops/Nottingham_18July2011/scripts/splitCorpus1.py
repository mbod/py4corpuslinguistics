import os

dir = '../data/simpleGTech/'
file = 'wwf-pdf-file-format-printed_GTech42.txt'

filepath = os.path.normpath(dir + file)

#open the file for reading, read the file, tidy up after yourself and close the file
f = open(dir + '/' + file, 'r')
text = f.read()
f.close()

#get the article
start = '<div id="articleHeader">'
end = '<div class="eight-col discussion content-comment-list">'

article = text[text.find(start):text.find(end)]

articledir = r'../output/simpleGTech_split/articles/'
articlefile = file[:file.rfind('.')] + '_article.txt'

f = open(articledir + articlefile, 'w')
f.write(article)
f.close()
 

#get the comments
startOfSection = '<div class="eight-col discussion content-comment-list">'

comments = text[text.find(startOfSection):]

commentsdir = r'../output/simpleGTech_split/comments/'
commentsfile = file[:file.rfind('.')] + '_comments.txt'

f = open(commentsdir + commentsfile, 'w')
f.write(comments)
f.close()





