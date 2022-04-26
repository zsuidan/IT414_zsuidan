import shutil

def test_correct_form(my_browser):
    """Tests correct form with proper email and phone number with dashes. Stores a screenshot in images folder, adding "passed_" if the correct response is given.
    Arguments:
        my_browser -- browser page being tested
    """
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

def test_correct_form_2(my_browser):
    """Tests correct form with an empty email and phone number without dashes. Stores a screenshot in images folder, adding "passed_" if the correct response is given.
    Arguments:
        my_browser -- browser page being tested
    """
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

def test_incorrect_email(my_browser):
    """Tests an email missing an @. Stores a screenshot in images folder, adding "passed_" if the correct response is given.
    Arguments:
        my_browser -- browser page being tested
    """
   
    email_field = my_browser.find_element_by_id("emailAddress")
    email_field.send_keys("zsuidan97gmail.com")

    my_browser.save_screenshot("images/incorrect_email_1.png")

    submit_button = my_browser.find_element_by_id("my_submit")
    submit_button.click()

    browser_alert = my_browser.switch_to.alert
    alert_text = browser_alert.text
    browser_alert.accept()

    if "Your email address is in an incorrect format" in alert_text:
        shutil.move('images/incorrect_email_1.png', 'images/passed_incorrect_email_1.png')
    
    email_field.clear()

def test_incorrect_email_2(my_browser):
    """Tests an email missing a period. Stores a screenshot in images folder, adding "passed_" if the correct response is given.
    Arguments:
        my_browser -- browser page being tested
    """
    
    email_field = my_browser.find_element_by_id("emailAddress")
    email_field.send_keys("zsuidan97@gmailcom")

    my_browser.save_screenshot("images/incorrect_email_2.png")

    submit_button = my_browser.find_element_by_id("my_submit")
    submit_button.click()

    browser_alert = my_browser.switch_to.alert
    alert_text = browser_alert.text
    browser_alert.accept()

    if "Your email address is in an incorrect format" in alert_text:
        shutil.move('images/incorrect_email_2.png', 'images/passed_incorrect_email_2.png')
    
    email_field.clear()

def test_incorrect_email_3(my_browser):
    """Tests an email without a user. Stores a screenshot in images folder, adding "passed_" if the correct response is given.
    Arguments:
        my_browser -- browser page being tested
    """
   
    email_field = my_browser.find_element_by_id("emailAddress")
    email_field.send_keys("@gmail.com")

    my_browser.save_screenshot("images/incorrect_email_3.png")

    submit_button = my_browser.find_element_by_id("my_submit")
    submit_button.click()

    browser_alert = my_browser.switch_to.alert
    alert_text = browser_alert.text
    browser_alert.accept()

    if "Your email address is in an incorrect format" in alert_text:
        shutil.move('images/incorrect_email_3.png', 'images/passed_incorrect_email_3.png')
    
    email_field.clear()

def test_incorrect_phone(my_browser):
    """Tests a phone number being too short. Stores a screenshot in images folder, adding "passed_" if the correct response is given.
    Arguments:
        my_browser -- browser page being tested
    """

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
    
    phone_field.clear()

def test_incorrect_phone_2(my_browser):
    """Tests a phone number being 11 digits long. Stores a screenshot in images folder, adding "passed_" if the correct response is given.
    Arguments:
        my_browser -- browser page being tested
    """

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
    
    phone_field.clear()

def test_incorrect_phone_3(my_browser):
    """Tests a phone number being too long. Stores a screenshot in images folder, adding "passed_" if the correct response is given.
    Arguments:
        my_browser -- browser page being tested
    """
   
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
    
    phone_field.clear()

def test_long_first_name(my_browser):
    """Tests a first name being too long. Stores a screenshot in images folder, adding "passed_" if the correct response is given.
    Arguments:
        my_browser -- browser page being tested
    """
    first_name_field = my_browser.find_element_by_id("firstName")
    first_name_field.send_keys("Zacharyyyyy")

    my_browser.save_screenshot("images/long_first_name.png")

    submit_button = my_browser.find_element_by_id("my_submit")
    submit_button.click()

    browser_alert = my_browser.switch_to.alert
    alert_text = browser_alert.text
    browser_alert.accept()

    if "Please check the length of the First name field" in alert_text:
        shutil.move('images/long_first_name.png', 'images/passed_long_first_name.png')
    
    first_name_field.clear()

def test_long_last_name(my_browser):
    """Tests a last name being too long. Stores a screenshot in images folder, adding "passed_" if the correct response is given.
    Arguments:
        my_browser -- browser page being tested
    """

    last_name_field = my_browser.find_element_by_id("lastName")
    last_name_field.send_keys("Suidannnnnnnnnnn")

    my_browser.save_screenshot("images/long_last_name.png")

    submit_button = my_browser.find_element_by_id("my_submit")
    submit_button.click()

    browser_alert = my_browser.switch_to.alert
    alert_text = browser_alert.text
    browser_alert.accept()

    if "Please check the length of the Last name field" in alert_text:
        shutil.move('images/long_last_name.png', 'images/passed_long_last_name.png')
    
    last_name_field.clear()

def test_no_first_name(my_browser):
    """Tests a first name not being entered. Stores a screenshot in images folder, adding "passed_" if the correct response is given.
    Arguments:
        my_browser -- browser page being tested
    """
    my_browser.save_screenshot("images/no_first_name.png")

    submit_button = my_browser.find_element_by_id("my_submit")
    submit_button.click()

    browser_alert = my_browser.switch_to.alert
    alert_text = browser_alert.text
    browser_alert.accept()

    if "First name is required" in alert_text:
        shutil.move('images/no_first_name.png', 'images/passed_no_first_name.png')

def test_no_last_name(my_browser):
    """Tests a last name not being entered. Stores a screenshot in images folder, adding "passed_" if the correct response is given.
    Arguments:
        my_browser -- browser page being tested
    """
    my_browser.save_screenshot("images/no_last_name.png")

    submit_button = my_browser.find_element_by_id("my_submit")
    submit_button.click()

    browser_alert = my_browser.switch_to.alert
    alert_text = browser_alert.text
    browser_alert.accept()

    if "Last name is required" in alert_text:
        shutil.move('images/no_last_name.png', 'images/passed_no_last_name.png')

def test_no_phone(my_browser):
    """Tests no phone being entered. Stores a screenshot in images folder, adding "passed_" if the correct response is given.
    Arguments:
        my_browser -- browser page being tested
    """

    my_browser.save_screenshot("images/no_phone.png")

    submit_button = my_browser.find_element_by_id("my_submit")
    submit_button.click()

    browser_alert = my_browser.switch_to.alert
    alert_text = browser_alert.text
    browser_alert.accept()

    if "Phone number is required" in alert_text:
        shutil.move('images/no_phone.png', 'images/passed_no_phone.png')

def test_short_first_name(my_browser):
    """Tests a first name being too short. Stores a screenshot in images folder, adding "passed_" if the correct response is given.
    Arguments:
        my_browser -- browser page being tested
    """
    first_name_field = my_browser.find_element_by_id("firstName")
    first_name_field.send_keys("Za")

    my_browser.save_screenshot("images/short_first_name.png")

    submit_button = my_browser.find_element_by_id("my_submit")
    submit_button.click()

    browser_alert = my_browser.switch_to.alert
    alert_text = browser_alert.text
    browser_alert.accept()

    if "Please check the length of the First name field" in alert_text:
        shutil.move('images/short_first_name.png', 'images/passed_short_first_name.png')
    
    first_name_field.clear()


def test_short_last_name(my_browser):
    """Tests a last name being too short. Stores a screenshot in images folder, adding "passed_" if the correct response is given.
    Arguments:
        my_browser -- browser page being tested
    """

    last_name_field = my_browser.find_element_by_id("lastName")
    last_name_field.send_keys("S")

    my_browser.save_screenshot("images/short_last_name.png")

    submit_button = my_browser.find_element_by_id("my_submit")
    submit_button.click()

    browser_alert = my_browser.switch_to.alert
    alert_text = browser_alert.text
    browser_alert.accept()

    if "Please check the length of the Last name field" in alert_text:
        shutil.move('images/short_last_name.png', 'images/passed_short_last_name.png')

    last_name_field.clear()