from functions.regex_functions import *
import pyperclip

#ctrl + / comments out highlighted lines
# date_ok = False

# while not date_ok:
#     date = input("Please input the date: ")
#     date_ok = isValidDate(date)

# date_string = input("Please input some text: ")

date_string = str(pyperclip.paste())

my_dates = findAllDates(date_string)

print(my_dates)

output_string = ""

for date in my_dates:
    output_string = output_string + date + "\n"

pyperclip.copy(output_string)