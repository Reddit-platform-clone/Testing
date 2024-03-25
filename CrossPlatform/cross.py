import pytest
from appium import webdriver
from locators import desired_caps, url
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.common import AppiumOptions
from time import sleep
from typing import Any, Dict

driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(desired_caps))
driver.implicitly_wait(10)

# VALID SIGN UP WITH EMAIL

driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Continue with email").click()
sleep(3)

driver.find_element(by=AppiumBy.XPATH,
                    value="//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.EditText[1]").click()
sleep(1)
driver.find_element(by=AppiumBy.XPATH,
                    value="//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.EditText[1]").send_keys("youssefemad@hotmail.com")
sleep(3)
driver.find_element(by=AppiumBy.XPATH,
                    value="//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.EditText[2]").click()
sleep(1)
driver.find_element(by=AppiumBy.XPATH,
                    value="//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.EditText[2]").send_keys(
    "eMAD1234")
sleep(3)
driver.implicitly_wait(10)

driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Continue").click()
sleep(3)

driver.find_element(by=AppiumBy.XPATH, value="//android.widget.EditText").click()
sleep(1)
driver.find_element(by=AppiumBy.XPATH, value="//android.widget.EditText").send_keys("ValidSignUp")
sleep(3)

driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Continue").click()

driver.quit()
