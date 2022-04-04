import re

def findAllDates(passed_string):
    #Regex used for validation does not work well for searching strings. Regex goes for the minimum which leaves off the second digit and the year isn't in a group and isn't included
    #\b sets bounds, preventing issues with extra digits at the start or end
    dateRegex = re.compile(r'\b(\d)(\d){0,1}\b(-|/)(\d)(\d){0,1}(-|/)\b(\d\d\d\d)\b')
    dateList = dateRegex.findall(passed_string)
    date_return_list = []

    #Fixes formatting for found dates. For each date in the list, each tuple in the date gets added to a string.
    for date in dateList:
        temp_date = ""

        for item in date:
            temp_date = temp_date + str(item)

        date_return_list.append(temp_date)

    return date_return_list

def isValidDate(passed_date):
    #Date must have 1-2 digits for the month, followed by a dash OR forward slash, followed by 1-2 more digits, then another dash OR forward slash, then 4 digits
    dateRegex = re.compile(r'(\d){1,2}(-|/)(\d){1,2}(-|/)\d\d\d\d')
    dateTest = dateRegex.search(passed_date)

    if dateTest is None:
        print("You did not enter a proper date")
        return False
    else:
        if passed_date == dateTest.group():
            print("You did enter a proper date")
            return True
        else:
            print("You did not enter a proper date")
            return False