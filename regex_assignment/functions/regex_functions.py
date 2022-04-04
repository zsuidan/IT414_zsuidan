import re

def findAllCoords(passed_string):
    #Coord can either be negative or positive. Coords start with up to 3 digits followed by a decimal then up to 5 digits after. 
    #The second coord is separated by a comma and follows the same rules.
    coordRegex = re.compile(r'-?\d{1,3}.\d{1,5}, -?\d{1,3}.\d{1,5}')
    coordList = coordRegex.findall(passed_string)
    coord_return_list = []

    #Fixes formatting for found coords. For each coord in the list, each tuple in the date gets added to a string.
    for coord in coordList:
        temp_coord = ""

        for item in coord:
            temp_coord = temp_coord + str(item)

        coord_return_list.append(temp_coord)

    return coord_return_list

def findAllDollars(passed_string):
    #Coord can either be negative or positive. Coords start with up to 3 digits followed by a decimal then up to 5 digits after. 
    #The second coord is separated by a comma and follows the same rules.
    dollarsRegex = re.compile(r'\$\d{0,3},?\d{1,3}\.?\d{0,2}')
    dollarsList = dollarsRegex.findall(passed_string)
    dollars_return_list = []

    #Fixes formatting for found coords. For each coord in the list, each tuple in the date gets added to a string.
    for dollars in dollarsList:
        temp_coord = ""

        for item in dollars:
            temp_coord = temp_coord + str(item)

        dollars_return_list.append(temp_coord)

    return dollars_return_list

def findAllCards(passed_string):
    #Coord can either be negative or positive. Coords start with up to 3 digits followed by a decimal then up to 5 digits after. 
    #The second coord is separated by a comma and follows the same rules.
    cardRegex = re.compile(r'\d{2,16} ?\d{2,16} ?\d{2,16} ?\d{2,16}')
    cardList = cardRegex.findall(passed_string)
    card_return_list = []

    #Fixes formatting for found coords. For each coord in the list, each tuple in the date gets added to a string.
    for card in cardList:
        temp_card = ""

        for item in card:
            temp_card = temp_card + str(item)

        card_return_list.append(temp_card)

    return card_return_list

def isValidCoord(passed_coord):
    #Coord can either be negative or positive. Coords start with up to 3 digits followed by a decimal then up to 5 digits after. 
    #The second coord is separated by a comma and follows the same rules.
    coordRegex = re.compile(r'-?\d{1,3}.\d{1,5}, -?\d{1,3}.\d{1,5}')
    coordTest = coordRegex.search(passed_coord)

    if coordTest is None:
        print("You did not enter a proper coord")
        return False
    else:
        if passed_coord == coordTest.group():
            print("You did enter a proper coord")
            return True
        else:
            print("You did not enter a proper coord")
            return False

def isValidDollars(passed_dollars):
    #Dollar value must have a dollar sign in front, followed by up to 3 numbers, followed by an optional comma, followed by up to 3 more numbers, 
    #followed by a decimal and 2 more numbers
    dollarsRegex = re.compile(r'\$\d{0,3},?\d{1,3}\.?\d{0,2}')
    dollarsTest = dollarsRegex.search(passed_dollars)

    if dollarsTest is None:
        print("You did not enter a proper coord")
        return False
    else:
        if passed_dollars == dollarsTest.group():
            print("You did enter a proper coord")
            return True
        else:
            print("You did not enter a proper coord")
            return False

def isValidCard(passed_card):
    #Credit Card number can be up to 4 groups of 2-16 numbers separated by optional spaces. 
    cardRegex = re.compile(r'\d{2,16} ?\d{2,16} ?\d{2,16} ?\d{2,16}')
    cardTest = cardRegex.search(passed_card)

    if cardTest is None:
        print("You did not enter a proper coord")
        return False
    else:
        if passed_card == cardTest.group():
            print("You did enter a proper coord")
            return True
        else:
            print("You did not enter a proper coord")
            return False