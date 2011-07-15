import os
import re


#First write a function to output the list of comments to a file

#1. name and arguements required
def output_comments(comment_list, file_name):

    #2. specify the files directory and basic file name for output
    comments_dir = '../output/simpleGTech_split/separated_comments'
    base_file_name = file_name[:-4]

    #3. loop through the list of comments with a counter
    for i, comment in enumerate(comment_list[1:]):
    
        #4. set file name for the current comment using base file name and counter i
        comments_file = base_file_name + '_%d.txt' % (i + 1)
        
        file_path = os.path.join(comments_dir, comments_file)

        #5. write the comment to the file
        open(file_path, mode='w', encoding='utf-8').write(comment) 
       
    #6. return total of the comments printed
    return i + 1



#The main script

#1. specify location of input directory
dir_path = '../output/simpleGTech_split/comments'


#2. loop through all the files in the directory
for file_name in os.listdir(dir_path):
    
    #3. combine the file name with the directory path
    file_path = os.path.join(dir_path, file_name)

    #4. open the file for reading, read file, close file
    text = open(file_path, mode='r', encoding='utf-8').read()
    
    #5. split comments
    comment_list = re.split('<ul .*?class="comment b2".*?>', text)

    #6. send the data to the function to print the comments
    comment_count = output_comments(comment_list, file_name)

    #7. print some feedback
    print('outputted %d comments from %s' % (comment_count, file_name))
            
        

