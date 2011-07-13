import os
import re

#1. specify location of input directory
dir_path = '../output/simpleGTech_split/comments'

#2. loop through all the files in the directory
for file_name in os.listdir(dir_path):

    #3. provide a bit of feedback so we know where we are
    print(file_name)
    
    #4. combine the file name with the directory path
    file_path = os.path.join(dir_path, file_name)

    #5. open the file for reading, read file, close file
    text = open(file_path, mode='r', encoding='utf-8').read()
    
    #6. split comments
    comment_list = re.split('<ul class="comment b2" .+?>', text)

    #7 specify the files directory and basic file name for output
    
    comments_dir = '../output/simpleGTech_split/separated_comments'
    base_file_name = file_name[:file_name.rfind('.')]

    #8. loop through the list of comments with a counter
    for i, comment in enumerate(comment_list[1:]):

        #9. set file name for the current comment using base file name and counter i
        comments_file = base_file_name + '_{0}.txt'.format(i + 1)
        
        file_path = os.path.join(comments_dir, comments_file)

        #10. write the comment to the file
        open(file_path, mode='w', encoding='utf-8').write(comment)


            
        
