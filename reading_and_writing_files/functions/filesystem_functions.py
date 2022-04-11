import platform
import os
import shutil
from pathlib import Path

def copyFolder():
    #Obtains root path and changes directory to it
    my_path = getPath()
    os.chdir(my_path)

    #Asks user for which folder they would like to copy and what folder to copy the contents to
    folder_to_copy = input("\nWhat is the name of the folder you would like to copy?: ")
    folder_to_copy_to = input("What is the name of the folder you wish to copy to?: ")

    copied_folder_path = Path(my_path, folder_to_copy)
    folder_copied_to_path = Path(my_path, folder_to_copy_to)

    #If the folder being copied exists, the rest of the function is carried out otherwise an error message is displayed
    if copied_folder_path.exists():
        #Opens log file for folder copied to
        log_file = open(f'log.txt', 'w')

        #Checks if the folder being copied to exists and creates it if it does not
        if not folder_copied_to_path.exists():
            os.makedirs(folder_copied_to_path)
            log_file.write(str(folder_copied_to_path) + " was created successfully.\n")

        #Copies contents of folder being copied to the folder being copied to
        file_list = os.listdir(copied_folder_path)

        for file_item in file_list:

            file_path = os.path.join(copied_folder_path, file_item)

            #Handles copying files
            if os.path.isfile(file_path):
                #Obtains size of the file
                temp_file_size = os.path.getsize(file_path)
                temp_file_divide = temp_file_size / 1000000000

                #Files below 1 GB in size are copied and those over 1 GB are skipped
                if temp_file_divide < 1:
                    shutil.copy2(file_path, folder_copied_to_path)
                    log_file.write(str(file_item) + " was copied successfully to " + str(folder_copied_to_path) + "\n")
                else: 
                    log_file.write(str(file_item) + " was passed over for being over 1 GB in size.\n")
            
            #Handles copying folders
            else:
                if os.path.isdir(folder_copied_to_path / file_item):
                    shutil.rmtree(folder_copied_to_path / file_item)
                    shutil.copytree(copied_folder_path / file_item, folder_copied_to_path / file_item)
                else:
                    shutil.copytree(copied_folder_path / file_item, folder_copied_to_path / file_item)
                
                log_file.write(str(file_item) + " was copied successfully to " + str(folder_copied_to_path) + "\n")
        
        #Closes log file and transfers it to destination folder
        log_file.close()

        if os.path.isfile(folder_copied_to_path / "log.txt"):
            os.remove(folder_copied_to_path / "log.txt")
            shutil.move("log.txt", folder_copied_to_path)
        else:
            shutil.move("log.txt", folder_copied_to_path)
        
        print("\nFolder copied successfully.")

    else:
        print("\n" + str(copied_folder_path) + " does not exist.")

# def createFolder():

#     my_path = getPath()

#     new_folder = input("What is the name of the folder you would like to create?: ")
#     os.makedirs(os.path.join(my_path, new_folder))

# def drawmenu():
    
#     print("What would you like to do?")
#     print("To show all files, enter 'S'")
#     print("To create a new folder, enter 'N'")
#     print("To copy a file, enter 'C'")

def getPath():

    my_system = platform.system()

    if my_system == "Windows":
        root_fs = "C:\\"
    else:
        root_fs = "/"

    return root_fs


# def showFiles():

#     my_path = getPath()

#     os.chdir(my_path)
#     print("Printing the contents of " + os.getcwd())

#     file_list = os.listdir(my_path)

#     for file_item in file_list:
#         if os.path.isfile(os.path.join(my_path, file_item)):
#             temp_file_size = os.path.getsize(os.path.join(my_path, file_item))
#             temp_file_divide = temp_file_size / 1000000

#             if temp_file_divide < 1:
#                 print(file_item + " | " + str(temp_file_size) + " bytes")
#             else: 
#                 print(file_item + " | " + str(temp_file_divide) + " MB")
        
#         else:
#             print(file_item + " | " + "folder")

#     print(my_path)