import os
import shutil

# for folderName, subFolders, fileNames in os.walk('C:\\file_explore'):
#     print("The current folder is " + folderName)

my_return = os.walk('C:\\file_explore')

for item in my_return:
    #Pulls items in the third position (files). Renames all files with "orig_" at the start. 
    for filename in item[2]:
        temp_filename = "orig_" + filename
        shutil.move(os.path.join(item[0], filename), os.path.join(item[0], temp_filename))

#Generates a tuple for each folder, the first item is the folder you are in, the second item is all subfolders within that folder, the third is all the files in the folder
# ('C:\\file_explore', ['stuff', 'test'], ['customer_export.txt', 'idea.pptx', 'logo-footer.png', 'new_file.txt', 'notes.txt'])
# ('C:\\file_explore\\stuff', ['other_folder'], ['notes.txt'])
# ('C:\\file_explore\\stuff\\other_folder', [], [])
# ('C:\\file_explore\\test', [], [])