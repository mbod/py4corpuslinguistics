import os

#1. specify locations of directory and files for input
dir_path = '../data/simpleGTech'
file_name = 'wwf-pdf-file-format-printed_GTech42.txt'

file_path = os.path.join(dir_path, file_name)


#2. read the input file into a string
text = open(file_path, mode='r', encoding='utf-8').read()

#3. extract the article section
start_of_article = '<div id="articleHeader">'
end_of_article = '<div class="eight-col discussion content-comment-list">'

article = text[text.find(start_of_article):text.find(end_of_article)]

#4. specify the location and name for writing article out to file
article_dir = '../output/simpleGTech_split/articles'
article_file = file_name[:-4] + '_article.txt'

file_path = os.path.join(article_dir, article_file)

#5. write the article section out to a file
open(file_path, mode='w').write(article)

#6. extract the comments section
start_of_comments = '<div id="discussion-comments">'

comments = text[text.find(start_of_comments):]

#7. specify the location and name for writing article out to file
comments_dir = '../output/simpleGTech_split/comments/'
comments_file = file_name[:-4] + '_comments.txt'

file_path = os.path.join(comments_dir, comments_file)

#8. write the comments section out to a file
open(file_path, mode='w').write(comments)



