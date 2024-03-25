from appium import webdriver
from typing import Any, Dict

# Appium driver initialization 

desired_caps: Dict[str, Any] = {
    "platformName": "Android",
    "appium:platformVersion": "13",
    "appium:deviceName": "emulator-5554",
    "appium:automationName": "UIAutomator2",
    "appium:app": "C:\\Users\\Emad\\Desktop\\Cross-Platform-main\\sarakel\\build\\app\\outputs\\apk\\debug\\app-debug.apk"
}

url = 'http://localhost:4723'
