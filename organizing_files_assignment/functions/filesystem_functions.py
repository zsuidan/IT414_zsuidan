import platform
import os
import shutil
import send2trash
import zipfile
import re

def processLogs():
    #Copies script folder to root directory under a folder named log_processing
    root_fs = getRoot()
    shutil.copytree('./organizing_files_assignment', str(root_fs) + '/log_processing', dirs_exist_ok=True)

    #Unzips the file containing the logs into a logs folder in the root directory
    log_zip = zipfile.ZipFile(str(root_fs) + "/log_processing/text_files/access_logs.zip")
    log_zip.extractall(str(root_fs) + "/logs")

    #Regex for the patterns being searched for
    log_regex = re.compile(r'\/wp-login\.php\?action=register|\.\.\/|install|select')

    my_logs = os.walk(str(root_fs) + "/logs")

    #Opens a text file for writing matching search items
    matches = open(str(root_fs) + "/logs/matches.txt", 'w')

    for log in my_logs:
        #Pulls individual log files and processes them
        for file in log[2]:
            log_path = os.path.join(log[0], file)
            log_file = open(log_path)

            results = log_regex.findall(log_file.read())
            print("Results for " + file + str(results))

            matches.write(str(results))

            log_file.close()

            if results:
                temp_filename = "processed_" + file
                shutil.move(log_path, os.path.join(log[0], temp_filename))
            # else:
            #     send2trash.send2trash(log[0])
    
    matches.close()

    #Creates a results zip which contains contents of the processed logs folder
    results_zip = zipfile.ZipFile(str(root_fs) + "/log_processing/text_files/results.zip", 'w')
    
    for foldername, subfolders, filenames in os.walk(str(root_fs) + "/logs"):
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