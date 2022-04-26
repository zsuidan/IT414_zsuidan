from functions.form_test_functions import *
from selenium import webdriver

#Sets browser to the contact form being tested
my_browser = webdriver.Chrome("chromedriver.exe")
my_browser.get("https://ool-content.walshcollege.edu/CourseFiles/IT/IT414/MASTER/Week04/WI20-website-testing-sites/assignment/index.php")

#Runs a series of first name tests
test_no_first_name(my_browser)
test_short_first_name(my_browser)
test_long_first_name(my_browser)

#Runs a series of last name tests
test_no_last_name(my_browser)
test_short_last_name(my_browser)
test_long_last_name(my_browser)

#Runs a series of email tests
test_incorrect_email(my_browser)
test_incorrect_email_2(my_browser)
test_incorrect_email_3(my_browser)

#Runs a series of phone tests
test_no_phone(my_browser)
test_incorrect_phone(my_browser)
test_incorrect_phone_2(my_browser)
test_incorrect_phone_3(my_browser)

#Runs a test for a fully correct form
test_correct_form(my_browser)
test_correct_form_2(my_browser)

#Closes testing browser
my_browser.close()