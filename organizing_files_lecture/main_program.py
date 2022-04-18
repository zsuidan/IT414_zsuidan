from os import rename
from functions.filesystem_functions import *

program_running = True

while program_running:

    drawmenu()

    my_option = input("What is your selection?: ")

    if my_option.lower() == "s":
        showFiles()
    elif my_option.lower() == "n":
        createFolder()
    elif my_option.lower() == "c":
        copyFile()
    elif my_option.lower() == "r":
        renameFile()
    elif my_option.lower() == "m":
        moveFile()
    elif my_option.lower() == "d":
        deleteFile()

    done_running = input("Would you like to do something else? (Y/N): ")

    if done_running.lower() == "n":
        program_running = False