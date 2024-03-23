from appium import webdriver

desired_caps = {
  'platformName': 'Android',
  'deviceName': 'YourDeviceName',
  'appPackage': 'com.reddit.reddit',
}

appium_server_url = 'http://localhost:4723'
def init():
    driver = webdriver.Remote(appium_server_url, desired_caps)
    return driver
  