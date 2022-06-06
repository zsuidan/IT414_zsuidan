from bs4 import BeautifulSoup
import requests

my_url = input("Please enter a URL: ")
request = requests.get(my_url)

if request.status_code == 200:
    weather_data = open("downloads/weather_data.html", "wb")
    for data_chunk in request.iter_content(100000):
        weather_data.write(data_chunk)

my_weather_page = open("downloads/weather_data.html")
weather_soup = BeautifulSoup(my_weather_page, "lxml")

#Pulls h3 tags with a class of DetailsSummary--daypartName--2FBp2
my_days = weather_soup.findAll("h3", {"class": ["DetailsSummary--daypartName--2FBp2"]})
#Pulls div tags with a class of DetailsSummary--temperature--1Syw3
my_temps = weather_soup.findAll("div", {"class": ["DetailsSummary--temperature--1Syw3"]})
#Pulls p tags with a class of DailyContent--narrative--hplRl
my_info = weather_soup.findAll("p", {"class": ["DailyContent--narrative--hplRl"]})
#
my_location = weather_soup.find("span", {"class": ["LocationPageTitle--PresentationName--1QYny"]})

print(my_location.getText())
#Loops through pulled dates and displays only the text
counter = 0
while counter < len(my_days):
    print(my_days[counter].getText())
    hi_low_temp = my_temps[counter].findAll("span")

    #Pulls the value for high temp from the first span tag
    hi_temp_unicode = hi_low_temp[0].getText()
    hi_temp = ""
    for char in hi_temp_unicode:
        if char.isdigit():
            hi_temp = hi_temp + char
    print(hi_temp)

    #Pulls the value for low temp from the first span tag
    low_temp_unicode = hi_low_temp[2].getText()
    low_temp = ""
    for char in low_temp_unicode:
        if char.isdigit():
            low_temp = low_temp + char
    print(low_temp)

    #Pulls daily weather info
    print(my_info[counter].getText() + "\n")

    #print(my_temps[counter].getText())
    counter += 1