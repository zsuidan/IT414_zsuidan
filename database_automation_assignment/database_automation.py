from classes.database_access import DB_Connect
import csv
import json
from bs4 import BeautifulSoup

#Connects to the database being used
my_db = DB_Connect('root', '', 'database_automation_assignment')

my_result = my_db.executeSelectQuery("SELECT * FROM addresses")

print(my_result)

#Prompts user for the file of the table they would like to import and the file type
imported_table = input("Please enter the name of the file you want to import (no extension): ")
imported_file_type = input("Please enter the file type (CSV, JSON, or XML): ")

#Verifies the entered file type is csv, json, or xml and prompts user to enter again if not
correct_type = False
while not correct_type:
    if imported_file_type.lower() == "csv" or imported_file_type.lower() == "json" or imported_file_type.lower() == "xml":
        correct_type = True
    else:
        imported_file_type = input("Invalid file type. Please enter CSV, JSON, or XML: ")

#If the file type is csv, executes the following
if imported_file_type.lower() == "csv":
    try:
        with open("text_files/" + imported_table + ".csv") as csv_file:
            #Clears existing data in working table
            my_db.executeQuery("TRUNCATE addresses_working")

            #Reads data from csv file and adds it to a list
            csvReader = csv.reader(csv_file)
            csv_data = list(csvReader)
            
            #Fills working table with imported csv data. Skips first row containing headers.
            row_count = 1
            while row_count < len(csv_data):
                my_db.executeQuery("INSERT INTO addresses_working (first_name, last_name, street, city, state, zip) VALUES ('" + csv_data[row_count][0] + "','" + csv_data[row_count][1] + "','" + csv_data[row_count][2] + "','" + csv_data[row_count][3] + "','" + csv_data[row_count][4] + "','" + csv_data[row_count][5] + "')")
                row_count += 1

            #Swaps the data of the addresses and addresses_working tables
            my_db.executeQuery("START TRANSACTION")
            my_db.executeQuery("RENAME TABLE database_automation_assignment.addresses TO database_automation_assignment.addresses_old")
            my_db.executeQuery("RENAME TABLE database_automation_assignment.addresses_working TO database_automation_assignment.addresses")
            my_db.executeQuery("COMMIT")

            my_db.executeQuery("START TRANSACTION")
            my_db.executeQuery("RENAME TABLE database_automation_assignment.addresses_old TO database_automation_assignment.addresses_working")
            my_db.executeQuery("COMMIT")
    except:
        print("File not found.")
#If the file type is json, executes the following
elif imported_file_type.lower() == "json":
    try: 
        with open("text_files/" + imported_table + ".json") as json_file:
            #Clears existing data in working table
            my_db.executeQuery("TRUNCATE addresses_working")

            json_data = json.load(json_file)

            #Fills working table with imported csv data
            for row in json_data:
                my_db.executeQuery("INSERT INTO addresses_working (first_name, last_name, street, city, state, zip) VALUES ('" + row['first_name'] + "','" + row['last_name'] + "','" + row['street'] + "','" + row['city'] + "','" + row['state'] + "','" + row['zip'] + "')")

            #Swaps the data of the addresses and addresses_working tables
            my_db.executeQuery("START TRANSACTION")
            my_db.executeQuery("RENAME TABLE database_automation_assignment.addresses TO database_automation_assignment.addresses_old")
            my_db.executeQuery("RENAME TABLE database_automation_assignment.addresses_working TO database_automation_assignment.addresses")
            my_db.executeQuery("COMMIT")

            my_db.executeQuery("START TRANSACTION")
            my_db.executeQuery("RENAME TABLE database_automation_assignment.addresses_old TO database_automation_assignment.addresses_working")
            my_db.executeQuery("COMMIT")
    except:
        print("File not found.")
#If the file type is xml, executes the following
elif imported_file_type.lower() == "xml":
    try:
        with open("text_files/" + imported_table + ".xml") as xml_file:
            my_db.executeQuery("TRUNCATE addresses_working")
            xml_parse = BeautifulSoup(xml_file, "xml")
    except:
        print("File not found.")