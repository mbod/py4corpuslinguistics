import os
import re

#1. specify location of input directory
dir_path = '../output/simpleGTech_split/comments'
file_name = 'wwf-pdf-file-format-printed_GTech42_comments.txt'

file_path = os.path.join(dir_path, file_name)

#2. read the file into a string
text = open(file_path, mode='r', encoding='utf-8').read()

#3. split the comments
comment_list = re.split('<ul class="comment b2" .+?>', text)

#4 specify the files directory and basic file name for output

comments_dir = '../output/simpleGTech_split/separated_comments'
base_file_name = file_name[:-4]

#5. loop through the list of comments with a counter
for i, comment in enumerate(comment_list[1:]):

    #6. set file name for the current comment using base file name and counter i
    comments_file = base_file_name + '_{0}.txt'.format(i + 1)
    
    file_path = os.path.join(comments_dir, comments_file)

    #7. write the comment to the file
    open(file_path, mode='w', encoding='utf-8').write(comment)
            
        
