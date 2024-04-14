import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.common import AppiumOptions
import initialization
from time import sleep

driver = webdriver.Remote(initialization.url, options=AppiumOptions().load_capabilities(initialization.desired_caps))
driver.implicitly_wait(10)


# VALID SIGN UP WITH EMAIL
def signup_email():
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


def complete_process():
    driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Login").click()
    sleep(3)

    email_field = driver.find_element(by=AppiumBy.XPATH, value=initialization.value_Xpath_signup)
    email_field.click()
    sleep(1)
    email_field.send_keys('youssefemad@hotmail.com')
    sleep(3)
    pass_field = driver.find_element(by=AppiumBy.XPATH, value=initialization.pass_Xpath_login)
    pass_field.click()
    sleep(1)
    pass_field.send_keys("eMAD1234")
    sleep(3)

    driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Continue").click()
    sleep(3)

    create_public_circle()
    sleep(10)

    driver.quit()


def login_fp():
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
    circled = driver.find_element(by=AppiumBy.XPATH, value=initialization.menu_Xpath_home)
    circled.click()
    sleep(2)

    driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Create a circle").click()
    sleep(1)

    creating = driver.find_element(by=AppiumBy.XPATH, value=initialization.createC_Xpath)
    creating.click()
    sleep(1)
    creating.send_keys("Software Testing")
    sleep(2)

    driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Create circle").click()
    sleep(1)


def create_private_circle():
    circled = driver.find_element(by=AppiumBy.XPATH, value=initialization.menu_Xpath_home)
    circled.click()
    sleep(2)

    driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Create a circle").click()
    sleep(1)

    creating = driver.find_element(by=AppiumBy.XPATH, value=initialization.createC_Xpath)
    creating.click()
    sleep(1)
    creating.send_keys("Software Testing")
    sleep(2)

    driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Public").click()
    sleep(1)
    driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Private").click()
    sleep(1)

    driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Create circle").click()
    sleep(1)


def create_post():
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
# complete_process()
# create_private_circle()
# create_public_circle()
