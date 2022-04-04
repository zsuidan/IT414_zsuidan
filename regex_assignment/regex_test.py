from functions.regex_functions import *
import pyperclip

#Retrieves data from clipboard
raw_data_string = str(pyperclip.paste())

#Pulls coords, dollars, and credit cards from the data
my_coords = findAllCoords(raw_data_string)
my_dollars = findAllDollars(raw_data_string)
my_cards = findAllCards(raw_data_string)

#Loops through retrieved data and creates a string from it, putting each set of data onto its own line
output_string = ""

counter = 0
while counter < len(my_coords):
    output_string = output_string + str(my_coords[counter]) + " | " + str(my_dollars[counter]) + " | " + str(my_cards[counter]) + "\n"
    counter += 1

#Copies the new set of data to the clipboard
pyperclip.copy(output_string)