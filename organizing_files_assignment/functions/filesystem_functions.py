from pathlib import Path
import platform
import os
import shutil
import send2trash
import zipfile
import re

def processLogs():
    #Copies script folder to root directory under a folder named log_processing
    root_fs = getRoot()
    shutil.copytree('./organizing_files_assignment', root_fs + 'log_processing', dirs_exist_ok=True)

    #Unzips the file containing the logs into a logs folder in the root directory
    log_folder_path = Path(root_fs + "logs")
    log_zip = zipfile.ZipFile(root_fs + "/log_processing/text_files/access_logs.zip")

    if log_folder_path.exists():
        overwrite_logs = input("Logs folder already exists. Enter \"Y\" to confirm overwrite: ")
        if overwrite_logs.lower() == 'y':
            shutil.rmtree(log_folder_path)
            log_zip.extractall(root_fs + "logs")
        else:
            exit()
    else:
        log_zip.extractall(root_fs + "logs")

    #Regex for the patterns being searched for
    log_regex = re.compile(r'\/wp-login\.php\?action=register|\.\.\/|install|select|403 134')
    ip_regex = re.compile(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')

    #Performs walk on log folder
    my_logs = os.walk(root_fs + "logs")

    match_list = ""

    for log in my_logs:
        #Pulls individual log files and processes them
        for file in log[2]:
            log_path = os.path.join(log[0], file)
            search_found = False

            #If a line matches the regex search, the IP address for that line plus the file name are added to the match list
            with open(log_path) as log_file:
                for line in log_file:
                    found_search_item = log_regex.findall(line)
                    if found_search_item:
                        search_found = True
                        ip_address = ip_regex.findall(line)

                        if (str(ip_address[0]) + " " + file) not in match_list:
                            match_list += (str(ip_address[0]) + " " + file + ",\n")

            log_file.close()

            #If a match was found in a log file, the file is kept and processed_ is added to the front of the name
            if search_found:
                temp_filename = "processed_" + file
                shutil.move(log_path, os.path.join(log[0], temp_filename))
            #If a match was not found, the file and its parent folder are sent to the recycle bin
            else:  
                send2trash.send2trash(log[0])
               
               

    #Opens a text file for writing matching search items
    matches_file = open(root_fs + "logs/matches.txt", 'w')
    matches_file.write(match_list)
    matches_file.close()

    #Creates a results zip which contains contents of the processed logs folder
    results_zip = zipfile.ZipFile("./organizing_files_assignment/text_files/results.zip", 'w')
    
    for foldername, subfolders, filenames in os.walk(root_fs + "/logs"):
        # Add the current folder to the ZIP file.
        results_zip.write(foldername)
        # Add all the files in this folder to the ZIP file.
        for filename in filenames:
            results_zip.write(os.path.join(foldername, filename))
    
    results_zip.close()
    


def getRoot():

    my_system = platform.system()

    if my_system == "Windows":
        root_fs = "C:\\"
    else:
        root_fs = "/"

    final_filepath = os.path.join(root_fs)

    return final_filepath