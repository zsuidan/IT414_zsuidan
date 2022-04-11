from functions.filesystem_functions import *

program_running = True

while program_running:

    copyFolder()

    done_running = input("\nWould you like to copy something else? (Y/N): ")

    if done_running.lower() == "n":
        program_running = False