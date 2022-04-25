from selenium import webdriver

my_browser = webdriver.Chrome("chromedriver.exe")
my_browser.get("https://ool-content.walshcollege.edu/CourseFiles/IT/IT414/MASTER/Week04/WI20-website-testing-sites/demonstration/")

#Obtains email field and enters email
email_field = my_browser.find_element_by_id("inputEmail")
email_field.send_keys("admin@myhome.com")

#Obtains password field and enters password
password_field = my_browser.find_element_by_id("inputPassword")
password_field.send_keys("superSecure")

#Obtains submit button and clicks button
submit_button = my_browser.find_element_by_id("my_submit")
submit_button.click()

#Closes the  alert
error_alert = my_browser.switch_to.alert
error_alert.accept()

#Clears password field and enters correct password
password_field.clear()
password_field.send_keys("superSecur3")

#Clicks submit again
submit_button.click()

#Finds all checkboxes 
checkboxes = my_browser.find_elements_by_tag_name("input[type='checkbox']")

#Goes through each checkbox, clicking it if it has a value of Galaxy J-7 or Galaxy-Tab-A-2016
for item in checkboxes:
    item_val = item.get_attribute("value")
    if item_val == "Galaxy J-7" or item_val == "Galaxy-Tab-A-2016":
        item.click()

#Obtains save button and clicks it
save_button = my_browser.find_element_by_id("save_button")
save_button.click()

#Obtains text from the alert stating blocked devices then closes it
block_alert = my_browser.switch_to.alert
block_text = block_alert.text
block_alert.accept()

#If these devices are in the alert, saves a screenshot of the page
if "Galaxy J-7" in block_text and "Galaxy-Tab-A-2016" in block_text:
    my_browser.save_screenshot("screenshot.png")

#Finds all buttons on the page
page_buttons = my_browser.find_elements_by_tag_name("button")

#If the button text is Logout, the button is clicked and the loop ends
for button in page_buttons:
    if button.text == "Logout":
        button.click()
        break

#Closes test browser
my_browser.close()