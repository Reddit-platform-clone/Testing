import appium
from appium import webdriver
from locators import desired_caps, appium_server_url
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
# from appium.webdriver.common.touch_action import TouchAction
import time

driver = webdriver.Remote(appium_server_url, options=AppiumOptions().desired_caps)

# Locate phone number login button by ACCESSIBILITY_ID
phone_number_login_button = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Continue with phone number")
phone_number_login_button.click()
time.sleep(30)

phone_number_field = driver.find_element(by=AppiumBy.XPATH, value="//*[text='Enter phone number']").send_keys("01100000008")
time.sleep(30)

continue_button = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="continue_button_id").click()
time.sleep(30)

verification_code_field = driver.find_element(by=AppiumBy.XPATH, value="//*[text='Enter verification code']").send_keys("658383")
continue_button = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="continue_button_id").click()
time.sleep(30)

skip_button = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Skip").click()
time.sleep(30)

# touch = TouchAction(driver)
# touch.press(x=315, y=975).move_to(x=338,y=476).release().perform()
# time.sleep(30)

# for i in range(5):
#      touch = TouchAction(driver)
#      touch.press(x=315, y=975).move_to(x=338, y=476).release().perform()
# time.sleep(30)

interests = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Music").click()
time.sleep(10)