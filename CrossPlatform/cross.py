import random
import string
from appium import webdriver
from locators import desired_caps, appium_server_url
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
# from appium.webdriver.common.touch_action import TouchAction
import time

driver = webdriver.Remote(appium_server_url, options= AppiumOptions().load_capabilities(desired_caps))

################################################ CONTINUE WITH PHONE NUMBER ##########################
def Phone_login():
 phone_number_login_button = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Continue with phone number")
 phone_number_login_button.click()
 time.sleep(10)

 phone_number_field = driver.find_element(by=AppiumBy.XPATH, value="//*[text='Enter phone number']")
 phone_number_field.send_keys("01100000008")
 time.sleep(5)
 time.sleep(3)

 continue_button = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Continue")
 continue_button.click()
 time.sleep(30)

 verification_code_field = driver.find_element(by=AppiumBy.XPATH, value="//*[text='Enter verification code']")
 verification_code_field.send_keys("658383")

 continue_button = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Continue")
 continue_button.click()
 time.sleep(30)

 skip_button = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Skip")
 skip_button.click()
 time.sleep(30)

# touch = TouchAction(driver)
# touch.press(x=315, y=975).move_to(x=338,y=476).release().perform()
# time.sleep(30)

# for i in range(5):
#      touch = TouchAction(driver)
#      touch.press(x=315, y=975).move_to(x=338, y=476).release().perform()
# time.sleep(30)

 interests = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Music")
 interests.click()
 time.sleep(5)

 continue_button = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Continue")
 continue_button.click()
 time.sleep(10)
##############################################  LOGOUT  ##############################################
 


############################################ SIGN UP/ LOG IN #########################################



 ############################################# RANDOM EMAIL ##########################################
def createEmail():
    # Generate a random string of letters and digits for the username with right inputs 
    username = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    email = username + '@gmail.com'
    return email,username

def createWrongEmail():
    # Generate a random string of letters and digits for the username but wrong inputs 
    username = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    email = username
    return email,username

############################################# CONTINUE WITH GOOGLE ###################################
def Google_login():
 Google_login_button = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Continue with google account")
 Google_login_button.click()
 time.sleep(30)

 email_field = driver.find_element(by=AppiumBy.XPATH, value="//*[text='Enter email address']")
 email_field.send_keys("emad@gmail.com")
 time.sleep(3)