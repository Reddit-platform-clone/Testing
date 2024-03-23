from appium import webdriver
from typing import Any, Dict

desired_caps: Dict[str, Any] = {
  'platformName': 'Android',
  'deviceName': 'YourDeviceName',
  'appPackage': 'com.reddit.reddit',
}

appium_server_url = 'http://localhost:4723'
  