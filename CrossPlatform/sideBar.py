from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.common import AppiumOptions
import initialization
from time import sleep


driver = webdriver.Remote(initialization.url, options=AppiumOptions().load_capabilities(initialization.desired_caps))
driver.implicitly_wait(10)

def open_profile():
    """
  Opens the user profile and goes to edit profile section.
  Clicks on the element identified by 'profile_Xpath' to open the profile tab. Waits 2 seconds.
  Clicks on the element identified by 'my_profile_Xpath' to access the user profile. Waits 2 seconds.
  """
    driver.find_element(by=AppiumBy.XPATH, value=initialization.sideBar_Xpath).click()
    sleep(2)

    driver.find_element(by=AppiumBy.XPATH, value=initialization.my_profile_Xpath).click()
    sleep(2)

    driver.find_element(by=AppiumBy.XPATH, value=initialization.edit_profile_Xpath).click()
    sleep(2)

def saved():
    driver.find_element(by=AppiumBy.XPATH, value=initialization.sideBar_Xpath).click()
    sleep(2)

    driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Saved").click()
    sleep(5)

    driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value=initialization.savedComment_ID).click()
    sleep(2)

    driver.quit()


def history():
    driver.find_element(by=AppiumBy.XPATH, value=initialization.sideBar_Xpath).click()
    sleep(2)

    driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="History").click()
    sleep(5)
    driver.quit()


def social():
    driver.find_element(by=AppiumBy.XPATH, value=initialization.sideBar_Xpath).click()
    sleep(2)

    driver.find_element(by=AppiumBy.XPATH, value=initialization.my_profile_Xpath).click()
    sleep(2)

    driver.find_element(by=AppiumBy.XPATH, value=initialization.social_Xpath).click()
    sleep(2)

    driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Facebook").click()
    sleep(1)

    driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Add").click()
    sleep(2)
    driver.quit()