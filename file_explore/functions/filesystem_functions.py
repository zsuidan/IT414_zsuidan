import platform
import os
import shutil

def copyFile():
    my_path = getPath()

    file_to_copy = input("What is the name of the file you would like to copy?: ")
    folder_to_copy_to = input("What is the name of the folder you wish to copy to?: ")

    shutil.copy2(file_to_copy, folder_to_copy_to)

def createFolder():

    my_path = getPath()

    new_folder = input("What is the name of the folder you would like to create?: ")
    os.makedirs(os.path.join(my_path, new_folder))

def drawmenu():
    
    print("What would you like to do?")
    print("To show all files, enter 'S'")
    print("To create a new folder, enter 'N'")
    print("To copy a file, enter 'C'")

def getPath():

    my_system = platform.system()

    if my_system == "Windows":
        root_fs = "C:\\"
    else:
        root_fs = "/"

    final_filepath = os.path.join(root_fs, "file_explore")

    return final_filepath


def showFiles():

    my_path = getPath()

    os.chdir(my_path)
    print("Printing the contents of " + os.getcwd())

    file_list = os.listdir(my_path)

    for file_item in file_list:
        if os.path.isfile(os.path.join(my_path, file_item)):
            temp_file_size = os.path.getsize(os.path.join(my_path, file_item))
            temp_file_divide = temp_file_size / 1000000

            if temp_file_divide < 1:
                print(file_item + " | " + str(temp_file_size) + " bytes")
            else: 
                print(file_item + " | " + str(temp_file_divide) + " MB")
        
        else:
            print(file_item + " | " + "folder")

    print(my_path)