from functions.filesystem_functions import *

program_running = True

while program_running:
    #Calls function for copying a folder
    copyFolder()

    #Prompts user asking them if they would like to copy another folder
    done_running = input("\nWould you like to copy something else? (Y/N): ")

    #If N is entered, the program terminates, otherwise it continues 
    if done_running.lower() == "n":
        program_running = False