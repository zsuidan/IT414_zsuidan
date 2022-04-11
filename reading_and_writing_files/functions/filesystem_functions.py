import platform
import os
import shutil
from pathlib import Path

def copyFolder():
    """Allows a user to copy the contents of a specified folder into another folder. 
    Files over 1 GB in size are not copied and a log file detailing what was copied is generated at the destination folder.
    """
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

def getPath():
    """Obtains the root directory based on the user's operating system.

    Returns:
        root_fs - the root directory of the user based on their system
    """

    my_system = platform.system()

    if my_system == "Windows":
        root_fs = "C:\\"
    else:
        root_fs = "/"

    return root_fs