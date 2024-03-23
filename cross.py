import time
from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy

cap: Dict[str, Any] = {
    "platformName": "Android",
    "appium:platformVersion": "12",
    "appium:automationName": "UIAutomator2",
    "uiautomator2ServerInstallTimeout": 100000,
    "appium:deviceName": "adb-RF8M307ZBGE-nsY6kF._adb-tls-connect._tcp"
}

url = "http://localhost:4723"
time.sleep(30)
driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))
driver.implicitly_wait(30)

######################################### write something in search bar in chrome ###############################
opening = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Reddit")
opening.click()
time.sleep(30)

continueWithPhone = driver.find_element(by=AppiumBy.XPATH, value="//*[@text='Continue with phone number']")
continueWithPhone.click()
time.sleep(30)
