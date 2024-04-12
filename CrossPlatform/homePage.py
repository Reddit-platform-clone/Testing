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

def comment():
    driver.find_element(by=AppiumBy.XPATH, value=initialization.upvote_comment_Xpath).click()
    sleep(2)
    driver.find_element(by=AppiumBy.XPATH, value=initialization.downvote_comment_Xpath).click()
    sleep(5)

    driver.find_element(by=AppiumBy.XPATH, value=initialization.comment_Xpath).click()
    sleep(2)

    comments = driver.find_element(by=AppiumBy.XPATH, value=initialization.add_comment_Xpath)
    comments.click()
    sleep(1)
    comments.send_keys("I think so")
    sleep(1)

    driver.find_element(by=AppiumBy.XPATH, value=initialization.post_comment_Xpath).click()


def reply():
    driver.find_element(by=AppiumBy.XPATH, value=initialization.reply_Xpath).click()
    sleep(1)

    replies = driver.find_element(by=AppiumBy.XPATH, value=initialization.reply_Xpath)
    replies.click()
    sleep(2)
    replies.send_keys("You are right")

def share():
    driver.find_element(by=AppiumBy.XPATH, value=initialization.share_Xpath).click()
    sleep(2)

    driver.find_element(by=AppiumBy.XPATH, value=initialization.share_profile_Xpath).click()
    sleep(3)

    driver.find_element(by=AppiumBy.XPATH, value=initialization.share_post_Xpath).click()
    sleep(2)    

def open_profile():
    driver.find_element(by=AppiumBy.XPATH, value=initialization.profile_Xpath).click()
    sleep(2)

    driver.find_element(by=AppiumBy.XPATH, value=initialization.my_profile_Xpath).click()
    sleep(2)

    driver.find_element(by=AppiumBy.XPATH, value=initialization.edit_profile_Xpath).click()
    sleep(2)

def edit_profile():
    open_profile()
    sleep(1)

    Dname = driver.find_element(by=AppiumBy.XPATH, value=name_Xpath)
    Dname.click()
    sleep(1)
    Dname.send_keys("Youssef Emad")
    sleep(1)

    about = driver.find_element(by=AppiumBy.XPATH, value=initialization.about_Xpath)
    about.click()
    sleep(1)
    about.send_keys("I am an undergraduate biomedical engineer")
    sleep(1)

    driver.find_element(by=AppiumBy.XPATH, value=initialization.visibility_Xpath).click()
    sleep(1)
    driver.find_element(by=AppiumBy.XPATH, value=initialization.visibility_Xpath).click()
    sleep(1)

    driver.find_element(by=AppiumBy.XPATH, value=initialization.active_comm_Xpath).click()
    sleep(1)
    driver.find_element(by=AppiumBy.XPATH, value=initialization.active_comm_Xpath).click()
    sleep(1)

    links = driver.find_element(by=AppiumBy.XPATH, value=initialization.social_link_Xpath)
    links.click()
    sleep(1)
    which = driver.find_element(by=AppiumBy.XPATH, value=initialization.choose_link_Xpath)
    which.click()
    sleep(1)
    which.send_keys("any community")
    
    driver.quit()    

# Uncomment the function you want
# change_posts()
# join_community()
# upvote()
# comment()
# reply()
# share()
# open_profile()
# edit_profile()
