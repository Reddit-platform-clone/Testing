import pytest
from initialization import desired_caps, url
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.common import AppiumOptions
from time import sleep

driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(desired_caps))
driver.implicitly_wait(10)

# locators
value_Xpath_signup = "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.EditText[1]"
pass_Xpath_signup = "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.EditText[2]"
pass_Xpath_login = "//android.widget.ScrollView/android.widget.EditText[2]"
username_Xpath_signup = "//android.widget.EditText"
fp_Xpath = "//android.widget.EditText"


# VALID SIGN UP WITH EMAIL
def signup_email():
    driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Continue with email").click()
    sleep(3)

    email_field = driver.find_element(by=AppiumBy.XPATH, value=value_Xpath_signup)
    email_field.click()
    sleep(1)
    email_field.send_keys('youssefemad@hotmail.com')
    sleep(3)

    pass_field = driver.find_element(by=AppiumBy.XPATH, value=pass_Xpath_signup)
    pass_field.click()
    sleep(1)
    pass_field.send_keys("eMAD1234")
    sleep(3)
    driver.implicitly_wait(10)

    driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Continue").click()
    sleep(3)

    username = driver.find_element(by=AppiumBy.XPATH, value=username_Xpath_signup)
    username.click()
    sleep(1)
    username.send_keys("ValidSignUp")
    sleep(3)

    driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Continue").click()

    driver.quit()


def signup_wrongemail():
    driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Continue with email").click()
    sleep(3)

    email_field = driver.find_element(by=AppiumBy.XPATH, value=value_Xpath_signup)
    email_field.click()
    sleep(1)
    email_field.send_keys('youssefemadhotmail.com')
    sleep(3)

    pass_field = driver.find_element(by=AppiumBy.XPATH, value=pass_Xpath_signup)
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

    email_field = driver.find_element(by=AppiumBy.XPATH, value=value_Xpath_signup)
    email_field.click()
    sleep(1)
    email_field.send_keys('youssefemad@hotmail.com')
    sleep(3)

    pass_field = driver.find_element(by=AppiumBy.XPATH, value=pass_Xpath_signup)
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

    email_field = driver.find_element(by=AppiumBy.XPATH, value=value_Xpath_signup)
    email_field.click()
    sleep(1)
    email_field.send_keys('youssefemad@hotmail.com')
    sleep(3)
    pass_field = driver.find_element(by=AppiumBy.XPATH, value=pass_Xpath_login)
    pass_field.click()
    sleep(1)
    pass_field.send_keys("eMAD1234")
    sleep(3)

    driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Continue").click()
    sleep(3)

    driver.quit()


def login_fp():
    driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Login").click()
    sleep(3)

    email_field = driver.find_element(by=AppiumBy.XPATH, value=value_Xpath_signup)
    email_field.click()
    sleep(1)
    email_field.send_keys('youssefemad@hotmail.com')
    sleep(3)

    forgot_pass = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Forgot password?')
    forgot_pass.click()
    sleep(3)

    email_or_user_field = driver.find_element(by=AppiumBy.XPATH, value=fp_Xpath)
    email_or_user_field.click()
    sleep(1)
    email_or_user_field.send_keys('youssefemad@hotmail.com')
    sleep(2)

    driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Reset Password").click()
    driver.quit()

# Uncomment the function you want
# signup_email()
# signup_wrongemail()
# signup_invalidpass()
# login()
# login_fp()
