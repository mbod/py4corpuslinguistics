import os

#1. specify locations of directory and files for input
dir_path = '../data/simpleGTech/'
file_name = 'wwf-pdf-file-format-printed_GTech42.txt'

file_path = os.path.normpath(dir_path + file_name)

#2. open the input file for reading, read the file, close the file
f = open(file_path, 'r')
text = f.read()
f.close()

#3. extract the article section
start_of_article = '<div id="articleHeader">'
end_of_article = '<div class="eight-col discussion content-comment-list">'
article = text[text.find(start_of_article):text.find(end_of_article)]

#4. specify the location and name for writing article out to file
article_dir = '../output/articles/'
article_file = file_name[:file_name.rfind('.')] + '_article.txt'

file_path = os.path.normpath(article_dir + article_file)

#5. write the article section out to a file
f = open(file_path, 'w')
f.write(article)
f.flush()
f.close()

#6. extract the comments section
start_of_comments = '<div class="eight-col discussion content-comment-list">'
comments = text[text.find(start_of_comments):]

#7. specify the location and name for writing article out to file
comments_dir = '../output/comments/'
comments_file = file_name[:file_name.rfind('.')] + '_comments.txt'

file_path = os.path.normpath(comments_dir + comments_file)

#8. write the comments section out to a file
f = open(file_path, 'w')
f.write(comments)
f.flush()
f.close()





