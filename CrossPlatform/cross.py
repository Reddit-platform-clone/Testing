import pytest
from initialization import desired_caps, url
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.common import AppiumOptions
from time import sleep

driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(desired_caps))
driver.implicitly_wait(10)

# Locators: 
value_Xpath_signup = "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.EditText[1]"
username_Xpath_signup = "//android.widget.EditText"

# VALID SIGN UP WITH EMAIL
def signup_email():
    driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Continue with email").click()
    sleep(3)

    email_field = driver.find_element(by=AppiumBy.XPATH, value=value_Xpath_signup)
    email_field.click()
    sleep(1)
    email_field.send_keys('youssefemad@hotmail.com')
    sleep(3)

    pass_field = driver.find_element(by=AppiumBy.XPATH, value=value_Xpath_signup)
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


#signup_email()  # if you want to test continue with email process uncomment this
