from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.common import AppiumOptions
import initialization
from time import sleep


driver = webdriver.Remote(initialization.url, options=AppiumOptions().load_capabilities(initialization.desired_caps))
driver.implicitly_wait(10)

def join_community():
    driver.find_element(by=AppiumBy.XPATH, value=initialization.join_Xpath).click()
    sleep(3)
    driver.quit()


def change_posts():
    driver.find_element(by=AppiumBy.XPATH, value="//android.widget.Spinner").click()
    sleep(5)

    driver.find_element(by=AppiumBy.XPATH, value=initialization.latest_Xpath).click()
    sleep(5)
    driver.quit()


def upvote():
    driver.find_element(by=AppiumBy.XPATH, value=initialization.upvote_Xpath).click()
    sleep(3)

# change_posts()
# join_community()
# upvote()