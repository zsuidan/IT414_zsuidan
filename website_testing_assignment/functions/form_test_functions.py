from selenium import webdriver
import shutil

my_browser = webdriver.Chrome("chromedriver.exe")
my_browser.get("https://ool-content.walshcollege.edu/CourseFiles/IT/IT414/MASTER/Week04/WI20-website-testing-sites/assignment/index.php")

def close_browser():
    #Closes the test browser
    my_browser.close()

def test_correct_form():
    #Tests correct form with proper email and phone number with dashes
    first_name_field = my_browser.find_element_by_id("firstName")
    first_name_field.send_keys("Zachary")

    last_name_field = my_browser.find_element_by_id("lastName")
    last_name_field.send_keys("Suidan")

    email_field = my_browser.find_element_by_id("emailAddress")
    email_field.send_keys("zsuidan97@gmail.com")

    phone_field = my_browser.find_element_by_id("phoneNumber")
    phone_field.send_keys("248-123-4567")

    my_browser.save_screenshot("images/correct_form.png")

    submit_button = my_browser.find_element_by_id("my_submit")
    submit_button.click()

    form_submitted = my_browser.find_element_by_tag_name("h1")
    if form_submitted.text == "Thank You!":
        shutil.move('images/correct_form.png', 'images/passed_correct_form.png')

    back_button = my_browser.find_element_by_tag_name("a")
    back_button.click()

def test_correct_form_2():
    #Tests correct form with an empty email and phone number without dashes
    first_name_field = my_browser.find_element_by_id("firstName")
    first_name_field.send_keys("Zachary")

    last_name_field = my_browser.find_element_by_id("lastName")
    last_name_field.send_keys("Suidan")

    phone_field = my_browser.find_element_by_id("phoneNumber")
    phone_field.send_keys("2481234567")

    my_browser.save_screenshot("images/correct_form_2.png")

    submit_button = my_browser.find_element_by_id("my_submit")
    submit_button.click()

    form_submitted = my_browser.find_element_by_tag_name("h1")
    if form_submitted.text == "Thank You!":
        shutil.move('images/correct_form_2.png', 'images/passed_correct_form_2.png')

    back_button = my_browser.find_element_by_tag_name("a")
    back_button.click()

def test_no_first_name():
    #Tests a first name not being entered
    last_name_field = my_browser.find_element_by_id("lastName")
    last_name_field.send_keys("Suidan")

    email_field = my_browser.find_element_by_id("emailAddress")
    email_field.send_keys("zsuidan97@gmail.com")

    phone_field = my_browser.find_element_by_id("phoneNumber")
    phone_field.send_keys("248-123-4567")

    my_browser.save_screenshot("images/no_first_name.png")

    submit_button = my_browser.find_element_by_id("my_submit")
    submit_button.click()

    browser_alert = my_browser.switch_to.alert
    alert_text = browser_alert.text
    browser_alert.accept()

    if "First name is required" in alert_text:
        shutil.move('images/no_first_name.png', 'images/passed_no_first_name.png')

    last_name_field.clear()
    email_field.clear()
    phone_field.clear()


def test_short_first_name():
    #Tests a first name being too short
    first_name_field = my_browser.find_element_by_id("firstName")
    first_name_field.send_keys("Za")

    last_name_field = my_browser.find_element_by_id("lastName")
    last_name_field.send_keys("Suidan")

    email_field = my_browser.find_element_by_id("emailAddress")
    email_field.send_keys("zsuidan97@gmail.com")

    phone_field = my_browser.find_element_by_id("phoneNumber")
    phone_field.send_keys("248-123-4567")

    my_browser.save_screenshot("images/short_first_name.png")

    submit_button = my_browser.find_element_by_id("my_submit")
    submit_button.click()

    browser_alert = my_browser.switch_to.alert
    alert_text = browser_alert.text
    browser_alert.accept()

    if "Please check the length of the First name field" in alert_text:
        shutil.move('images/short_first_name.png', 'images/passed_short_first_name.png')
    
    first_name_field.clear()
    last_name_field.clear()
    email_field.clear()
    phone_field.clear()


def test_long_first_name():
    #Tests a first name being too long
    first_name_field = my_browser.find_element_by_id("firstName")
    first_name_field.send_keys("Zacharyyyyy")

    last_name_field = my_browser.find_element_by_id("lastName")
    last_name_field.send_keys("Suidan")

    email_field = my_browser.find_element_by_id("emailAddress")
    email_field.send_keys("zsuidan97@gmail.com")

    phone_field = my_browser.find_element_by_id("phoneNumber")
    phone_field.send_keys("248-123-4567")

    my_browser.save_screenshot("images/long_first_name.png")

    submit_button = my_browser.find_element_by_id("my_submit")
    submit_button.click()

    browser_alert = my_browser.switch_to.alert
    alert_text = browser_alert.text
    browser_alert.accept()

    if "Please check the length of the First name field" in alert_text:
        shutil.move('images/long_first_name.png', 'images/passed_long_first_name.png')
    
    first_name_field.clear()
    last_name_field.clear()
    email_field.clear()
    phone_field.clear()

def test_no_last_name():
    #Tests a last name not being entered
    first_name_field = my_browser.find_element_by_id("firstName")
    first_name_field.send_keys("Zachary")

    email_field = my_browser.find_element_by_id("emailAddress")
    email_field.send_keys("zsuidan97@gmail.com")

    phone_field = my_browser.find_element_by_id("phoneNumber")
    phone_field.send_keys("248-123-4567")

    my_browser.save_screenshot("images/no_last_name.png")

    submit_button = my_browser.find_element_by_id("my_submit")
    submit_button.click()

    browser_alert = my_browser.switch_to.alert
    alert_text = browser_alert.text
    browser_alert.accept()

    if "Last name is required" in alert_text:
        shutil.move('images/no_last_name.png', 'images/passed_no_last_name.png')

    first_name_field.clear()
    email_field.clear()
    phone_field.clear()

def test_short_last_name():
    #Tests a last name being too short
    first_name_field = my_browser.find_element_by_id("firstName")
    first_name_field.send_keys("Zachary")

    last_name_field = my_browser.find_element_by_id("lastName")
    last_name_field.send_keys("S")

    email_field = my_browser.find_element_by_id("emailAddress")
    email_field.send_keys("zsuidan97@gmail.com")

    phone_field = my_browser.find_element_by_id("phoneNumber")
    phone_field.send_keys("248-123-4567")

    my_browser.save_screenshot("images/short_last_name.png")

    submit_button = my_browser.find_element_by_id("my_submit")
    submit_button.click()

    browser_alert = my_browser.switch_to.alert
    alert_text = browser_alert.text
    browser_alert.accept()

    if "Please check the length of the Last name field" in alert_text:
        shutil.move('images/short_last_name.png', 'images/passed_short_last_name.png')
    
    first_name_field.clear()
    last_name_field.clear()
    email_field.clear()
    phone_field.clear()

def test_long_last_name():
    #Tests a last name being too long
    first_name_field = my_browser.find_element_by_id("firstName")
    first_name_field.send_keys("Zachary")

    last_name_field = my_browser.find_element_by_id("lastName")
    last_name_field.send_keys("Suidannnnnnnnnnn")

    email_field = my_browser.find_element_by_id("emailAddress")
    email_field.send_keys("zsuidan97@gmail.com")

    phone_field = my_browser.find_element_by_id("phoneNumber")
    phone_field.send_keys("248-123-4567")

    my_browser.save_screenshot("images/long_last_name.png")

    submit_button = my_browser.find_element_by_id("my_submit")
    submit_button.click()

    browser_alert = my_browser.switch_to.alert
    alert_text = browser_alert.text
    browser_alert.accept()

    if "Please check the length of the Last name field" in alert_text:
        shutil.move('images/long_last_name.png', 'images/passed_long_last_name.png')
    
    first_name_field.clear()
    last_name_field.clear()
    email_field.clear()
    phone_field.clear()

def test_incorrect_email():
    #Tests an email missing an @
    first_name_field = my_browser.find_element_by_id("firstName")
    first_name_field.send_keys("Zachary")

    last_name_field = my_browser.find_element_by_id("lastName")
    last_name_field.send_keys("Suidan")

    email_field = my_browser.find_element_by_id("emailAddress")
    email_field.send_keys("zsuidan97gmail.com")

    phone_field = my_browser.find_element_by_id("phoneNumber")
    phone_field.send_keys("248-123-4567")

    my_browser.save_screenshot("images/incorrect_email_1.png")

    submit_button = my_browser.find_element_by_id("my_submit")
    submit_button.click()

    browser_alert = my_browser.switch_to.alert
    alert_text = browser_alert.text
    browser_alert.accept()

    if "Your email address is in an incorrect format" in alert_text:
        shutil.move('images/incorrect_email_1.png', 'images/passed_incorrect_email_1.png')
    
    first_name_field.clear()
    last_name_field.clear()
    email_field.clear()
    phone_field.clear()

def test_incorrect_email_2():
    #Tests an email missing a period
    first_name_field = my_browser.find_element_by_id("firstName")
    first_name_field.send_keys("Zachary")

    last_name_field = my_browser.find_element_by_id("lastName")
    last_name_field.send_keys("Suidan")

    email_field = my_browser.find_element_by_id("emailAddress")
    email_field.send_keys("zsuidan97@gmailcom")

    phone_field = my_browser.find_element_by_id("phoneNumber")
    phone_field.send_keys("248-123-4567")

    my_browser.save_screenshot("images/incorrect_email_2.png")

    submit_button = my_browser.find_element_by_id("my_submit")
    submit_button.click()

    browser_alert = my_browser.switch_to.alert
    alert_text = browser_alert.text
    browser_alert.accept()

    if "Your email address is in an incorrect format" in alert_text:
        shutil.move('images/incorrect_email_2.png', 'images/passed_incorrect_email_2.png')
    
    first_name_field.clear()
    last_name_field.clear()
    email_field.clear()
    phone_field.clear()

def test_incorrect_email_3():
    #Tests an email without a user
    first_name_field = my_browser.find_element_by_id("firstName")
    first_name_field.send_keys("Zachary")

    last_name_field = my_browser.find_element_by_id("lastName")
    last_name_field.send_keys("Suidan")

    email_field = my_browser.find_element_by_id("emailAddress")
    email_field.send_keys("@gmail.com")

    phone_field = my_browser.find_element_by_id("phoneNumber")
    phone_field.send_keys("248-123-4567")

    my_browser.save_screenshot("images/incorrect_email_3.png")

    submit_button = my_browser.find_element_by_id("my_submit")
    submit_button.click()

    browser_alert = my_browser.switch_to.alert
    alert_text = browser_alert.text
    browser_alert.accept()

    if "Your email address is in an incorrect format" in alert_text:
        shutil.move('images/incorrect_email_3.png', 'images/passed_incorrect_email_3.png')
    
    first_name_field.clear()
    last_name_field.clear()
    email_field.clear()
    phone_field.clear()

def test_no_phone():
    #Tests no phone being entered
    first_name_field = my_browser.find_element_by_id("firstName")
    first_name_field.send_keys("Zachary")

    last_name_field = my_browser.find_element_by_id("lastName")
    last_name_field.send_keys("Suidan")

    email_field = my_browser.find_element_by_id("emailAddress")
    email_field.send_keys("zsuidan97@gmail.com")

    my_browser.save_screenshot("images/no_phone.png")

    submit_button = my_browser.find_element_by_id("my_submit")
    submit_button.click()

    browser_alert = my_browser.switch_to.alert
    alert_text = browser_alert.text
    browser_alert.accept()

    if "Phone number is required" in alert_text:
        shutil.move('images/no_phone.png', 'images/passed_no_phone.png')
    
    first_name_field.clear()
    last_name_field.clear()
    email_field.clear()

def test_incorrect_phone():
    #Tests a phone number being too short
    first_name_field = my_browser.find_element_by_id("firstName")
    first_name_field.send_keys("Zachary")

    last_name_field = my_browser.find_element_by_id("lastName")
    last_name_field.send_keys("Suidan")

    email_field = my_browser.find_element_by_id("emailAddress")
    email_field.send_keys("zsuidan97@gmail.com")

    phone_field = my_browser.find_element_by_id("phoneNumber")
    phone_field.send_keys("123-4567")

    my_browser.save_screenshot("images/incorrect_phone.png")

    submit_button = my_browser.find_element_by_id("my_submit")
    submit_button.click()

    browser_alert = my_browser.switch_to.alert
    alert_text = browser_alert.text
    browser_alert.accept()

    if "Your phone number is an incorrect format" in alert_text:
        shutil.move('images/incorrect_phone.png', 'images/passed_incorrect_phone.png')
    
    first_name_field.clear()
    last_name_field.clear()
    email_field.clear()
    phone_field.clear()

def test_incorrect_phone_2():
    #Tests a phone number being 11 digits long
    first_name_field = my_browser.find_element_by_id("firstName")
    first_name_field.send_keys("Zachary")

    last_name_field = my_browser.find_element_by_id("lastName")
    last_name_field.send_keys("Suidan")

    email_field = my_browser.find_element_by_id("emailAddress")
    email_field.send_keys("zsuidan97@gmail.com")

    phone_field = my_browser.find_element_by_id("phoneNumber")
    phone_field.send_keys("12345678910")

    my_browser.save_screenshot("images/incorrect_phone_2.png")

    submit_button = my_browser.find_element_by_id("my_submit")
    submit_button.click()

    browser_alert = my_browser.switch_to.alert
    alert_text = browser_alert.text
    browser_alert.accept()

    if "Your phone number is an incorrect format" in alert_text:
        shutil.move('images/incorrect_phone_2.png', 'images/passed_incorrect_phone_2.png')
    
    first_name_field.clear()
    last_name_field.clear()
    email_field.clear()
    phone_field.clear()

def test_incorrect_phone_3():
    #Tests a phone number being too long
    first_name_field = my_browser.find_element_by_id("firstName")
    first_name_field.send_keys("Zachary")

    last_name_field = my_browser.find_element_by_id("lastName")
    last_name_field.send_keys("Suidan")

    email_field = my_browser.find_element_by_id("emailAddress")
    email_field.send_keys("zsuidan97@gmail.com")

    phone_field = my_browser.find_element_by_id("phoneNumber")
    phone_field.send_keys("123-456-78910")

    my_browser.save_screenshot("images/incorrect_phone_3.png")

    submit_button = my_browser.find_element_by_id("my_submit")
    submit_button.click()

    browser_alert = my_browser.switch_to.alert
    alert_text = browser_alert.text
    browser_alert.accept()

    if "Your phone number is an incorrect format" in alert_text:
        shutil.move('images/incorrect_phone_3.png', 'images/passed_incorrect_phone_3.png')
    
    first_name_field.clear()
    last_name_field.clear()
    email_field.clear()
    phone_field.clear()