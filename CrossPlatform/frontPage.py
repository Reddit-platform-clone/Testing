import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.common import AppiumOptions
import initialization
from time import sleep

driver = webdriver.Remote(initialization.url, options=AppiumOptions().load_capabilities(initialization.desired_caps))
driver.implicitly_wait(10)

def signup_email():
    """
  Signs up for an account using a valid email and password.
  Clicks on the "Continue with email" button and enters a valid email address in the email field.
  Enters a valid password in the password field and clicks on "Continue".
  Fills in the username field and clicks on "Continue" again.
  Re-enters the email address and a valid password, then clicks on "Continue" to complete signup.
  Finally, hides the keyboard and closes the driver.
  """
    driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Continue with email").click()
    sleep(3)

    email_field = driver.find_element(by=AppiumBy.XPATH, value=initialization.value_Xpath_signup)
    email_field.click()
    sleep(1)
    email_field.send_keys('youssefemad@hotmail.com')
    sleep(3)
    pass_field = driver.find_element(by=AppiumBy.XPATH, value=initialization.pass_Xpath_signup)
    pass_field.click()
    sleep(1)
    pass_field.send_keys("eMAD1234")
    sleep(3)
    driver.implicitly_wait(10)

    driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Continue").click()
    sleep(3)

    username = driver.find_element(by=AppiumBy.XPATH, value=initialization.username_Xpath_signup)
    username.click()
    sleep(1)
    username.send_keys("asas")
    sleep(3)

    driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Continue").click()
    sleep(2)
    email_field = driver.find_element(by=AppiumBy.XPATH, value=initialization.value_Xpath_signup)
    email_field.click()
    sleep(1)
    email_field.send_keys('youssefemad@hotmail.com')
    sleep(3)
    pass_field = driver.find_element(by=AppiumBy.XPATH, value=initialization.pass_Xpath_login)
    pass_field.click()
    sleep(1)
    pass_field.send_keys("eMAD1234")
    sleep(1)

    driver.hide_keyboard()
    driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Continue").click()
    sleep(10)
    driver.quit()


def signup_wrongemail():
    """
  Attempts to sign up with an invalid email format.
  Clicks on the "Continue with email" button and enters an email address in a wrong format in the email field.
  Enters a valid password in the password field and clicks on "Continue".
  (The signup process likely fails due to the invalid email format.)
  Finally, closes the driver.
  """
    driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Continue with email").click()
    sleep(3)

    email_field = driver.find_element(by=AppiumBy.XPATH, value=initialization.value_Xpath_signup)
    email_field.click()
    sleep(1)
    email_field.send_keys('youssefemadhotmail.com')
    sleep(3)

    pass_field = driver.find_element(by=AppiumBy.XPATH, value=initialization.pass_Xpath_signup)
    pass_field.click()
    pass_field.send_keys("eMAD1234")
    sleep(3)
    driver.implicitly_wait(10)

    driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Continue").click()
    sleep(3)

    driver.quit()


def signup_invalidpass():
    """
  Attempts to sign up with an invalid password (too short).
  Clicks on the "Continue with email" button and enters a valid email address in the email field.
  Enters an invalid password (shorter than allowed) in the password field and clicks on "Continue".
  (The signup process likely fails due to the invalid password.)
  Finally, closes the driver.
  """
    driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Continue with email").click()
    sleep(3)

    email_field = driver.find_element(by=AppiumBy.XPATH, value=initialization.value_Xpath_signup)
    email_field.click()
    sleep(1)
    email_field.send_keys('youssefemad@hotmail.com')
    sleep(3)

    pass_field = driver.find_element(by=AppiumBy.XPATH, value=initialization.pass_Xpath_signup)
    pass_field.click()
    sleep(1)
    pass_field.send_keys("eMAD12")
    sleep(3)
    driver.implicitly_wait(10)

    driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Continue").click()
    sleep(3)

    driver.quit()


def login():
    """
  Logs in to an existing account with valid credentials.
  Clicks on the "Login" button and enters a valid email address in the email field.
  Enters the corresponding password in the password field and clicks on "Continue".
  Hides the keyboard and closes the driver.
  """
    driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Login").click()
    sleep(3)

    email_field = driver.find_element(by=AppiumBy.XPATH, value=initialization.value_Xpath_signup)
    email_field.click()
    sleep(1)
    email_field.send_keys('ayhaga')
    sleep(3)
    pass_field = driver.find_element(by=AppiumBy.XPATH, value=initialization.pass_Xpath_login)
    pass_field.click()
    sleep(1)
    pass_field.send_keys("12345678")
    sleep(3)
    
    driver.hide_keyboard()
    sleep(1)
    driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Continue").click()
    sleep(3)

    driver.quit()

def login_fp():
    """
  Initiates the forgot password process for an account.
  Clicks on the "Login" button and enters a valid email address in the email field.
  Clicks on the "Forgot password?" element.
  Enters the email address in the email/username field and clicks on "Reset Password".
  Finally, closes the driver.
  """
    driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Login").click()
    sleep(3)

    email_field = driver.find_element(by=AppiumBy.XPATH, value=initialization.value_Xpath_signup)
    email_field.click()
    sleep(1)
    email_field.send_keys('youssefemad@hotmail.com')
    sleep(3)

    forgot_pass = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Forgot password?')
    forgot_pass.click()
    sleep(3)

    email_or_user_field = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText')
    email_or_user_field.click()
    sleep(1)
    email_or_user_field.send_keys('youssefemad@hotmail.com')
    sleep(2)

    driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Reset Password").click()
    driver.quit()


def wrong_pass():
    """
  Attempts to login with an invalid password.
  Clicks on the "Login" button and enters a valid email address in the email field.
  Enters an incorrect password in the password field and clicks on "Continue".
  (The login process likely fails due to the invalid password.)
  Finally, closes the driver.
  """
    driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Login").click()
    sleep(3)

    email_field = driver.find_element(by=AppiumBy.XPATH, value=initialization.value_Xpath_signup)
    email_field.click()
    sleep(1)
    email_field.send_keys('youssefemadhotmail.com')
    sleep(3)
    pass_field = driver.find_element(by=AppiumBy.XPATH, value=initialization.pass_Xpath_login)
    pass_field.click()
    sleep(1)
    pass_field.send_keys("eMAD1234")
    sleep(3)

    driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Continue").click()
    sleep(3)


def create_public_circle():
    """
  Creates a public circle.
  Clicks on the menu element and then on "Create a circle" to initiate circle creation.
  Enters a circle name in the creation field and clicks on "Create circle" to complete creation as a public circle.
  """
    circled = driver.find_element(by=AppiumBy.XPATH, value=initialization.menu_Xpath_home)
    circled.click()

    driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Create community").click()
    sleep(1)

    creating = driver.find_element(by=AppiumBy.XPATH, value=initialization.createC_Xpath)
    creating.click()
    sleep(1)
    creating.send_keys("SoftwareTesting")
    sleep(2)

    driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Create community").click()
    sleep(1)


def create_private_circle():
    """
  Creates a private circle.
  Clicks on the menu element and then on "Create a circle" to initiate circle creation.
  Enters a circle name in the creation field.
  Clicks on "Public" to open the selection, then clicks on "Private" to set the circle as private.
  Clicks on "Create circle" to complete creation.
  """
    circled = driver.find_element(by=AppiumBy.XPATH, value=initialization.menu_Xpath_home)
    circled.click()

    driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Create community").click()
    sleep(1)

    creating = driver.find_element(by=AppiumBy.XPATH, value=initialization.createC_Xpath)
    creating.click()
    sleep(1)
    creating.send_keys("SoftwareTesting")
    sleep(2)

    driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="public").click()
    sleep(1)
    driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="private").click()
    sleep(1)

    driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Create community").click()
    sleep(1)


def create_post():
    """
  Creates a post.
  Clicks on the "Create" tab and enters a title and body for the post.
  Clicks on "Next" to proceed to the next step of post creation.
  """
    driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Create Tab 3 of 5").click()
    sleep(1)

    title = driver.find_element(by=AppiumBy.XPATH, value=initialization.post_Xpath_title)
    title.click()
    sleep(1)
    title.send_keys("WHY?")
    sleep(2)

    body = driver.find_element(by=AppiumBy.XPATH, value=initialization.post_Xpath_body)
    body.click()
    sleep(1)
    body.send_keys("I AM FINISHED")

    driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Next").click()
    

# Uncomment the function you want
# signup_email()
# signup_wrongemail()
# signup_invalidpass()
# login()
# login_fp()
# create_private_circle()
# create_public_circle()
# create_post()
