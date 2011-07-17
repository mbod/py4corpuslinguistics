import os

#1. specify location of the directory that has all the files in it
dir_path = '../data/simpleGTech'

#2. loop through all the files in the directory
for file_name in os.listdir(dir_path):

    #3. provide a bit of feedback so we know where we are
    print(file_name)

    #4. combine the file name with the directory path
    file_path = os.path.join(dir_path, file_name)
                                                                                    

    #5. open the file for reading, read the file, close the file
    text = open(file_path, mode='r', encoding='utf-8').read()

    #6. extract the article section
    start_of_article = '<div id="articleHeader">'
    end_of_article = '<div class="eight-col discussion content-comment-list">'

    article = text[text.find(start_of_article):text.find(end_of_article)]

    #7. specify the location and name for writing article out to file
    article_dir = '../output/simpleGTech_split/articles'
    article_file = file_name[:-4] + '_article.txt'

    file_path = os.path.join(article_dir, article_file)

    #8. write the article section out to a file
    open(file_path, mode='w', encoding='utf-8').write(article)
                                                                                    

    #9. extract the comments section
    start_of_comments = '<div id="discussion-comments">'

    comments = text[text.find(start_of_comments):]

    #10. specify the location and name for writing article out to file
    comments_dir = '../output/simpleGTech_split/comments/'
    comments_file = file_name[:-4] + '_comments.txt'

    file_path = os.path.join(comments_dir, comments_file)

    #11. write the comments section out to a file
    open(file_path, mode='w', encoding='utf-8').write(comments)





