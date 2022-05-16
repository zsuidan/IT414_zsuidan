def importTable():
    imported_table = input("Please enter the name of the file you want to import (no extension): ")
    imported_file_type = input("Please enter the file type (CSV, JSON, or XML): ")

    correct_type = False
    while not correct_type:
        if imported_file_type.lower() == "csv" or imported_file_type.lower() == "json" or imported_file_type.lower() == "xml":
            correct_type = True
        else:
            imported_file_type = input("Invalid file type. Please enter CSV, JSON, or XML: ")


    if imported_file_type.lower() == "csv":
        with open("/text_files/" + imported_table + ".csv") as table_file:
            print("csv")
    elif imported_file_type.lower() == "json":
        with open("/text_files/" + imported_table + ".json") as table_file:
            print("json")
    elif imported_file_type.lower() == "xml":
        with open("/text_files/" + imported_table + ".json") as table_file:
            print("xml")