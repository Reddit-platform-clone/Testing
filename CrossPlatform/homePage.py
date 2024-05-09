from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.common import AppiumOptions
import initialization
from time import sleep


driver = webdriver.Remote(initialization.url, options=AppiumOptions().load_capabilities(initialization.desired_caps))
driver.implicitly_wait(10)

def join_community():
    """"
  User joins a community through the Circles tab.
  Clicks on the Circles tab and then clicks on the join button existed in the list of circles.
  Finally, closes the driver.
    """
    driver.find_element(by=AppiumBy.XPATH, value="""//android.view.View[@content-desc="Communities
Tab 2 of 5"]""").click()
    sleep(3)
    driver.find_element(by=AppiumBy.XPATH, value=initialization.join_Xpath).click()
    driver.quit()

def change_posts():
    """
  Switches between home and popular posts.
  Clicks on the "home" element identified by 'home_Xpath', waits 5 seconds.
  Then clicks on the "popular" element identified by 'pop_Xpath', waits 5 seconds, and closes the driver.
  """
    driver.find_element(by=AppiumBy.XPATH, value="//android.view.View[@content-desc='sarakel']").click()
    sleep(5)

    driver.find_element(by=AppiumBy.XPATH, value=initialization.home_Xpath).click()
    sleep(5)
    driver.quit()

def post_settings():
    """
  Accesses post settings menu and save a post.
  Clicks on the element identified by 'set_post' (post settings). Waits 3 seconds.
  Then clicks on the element that he wants to (Save or Hide or Block Account or Report).
  Finally, closes the driver.
  """
    driver.find_element(by=AppiumBy.XPATH, value=initialization.set_post).click()
    sleep(3)

    driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Save").click() # Hide - Block Account - Report

def upvote():
    """
  Upvotes a post.
  Clicks on the element identified by 'upvote_post_Xpath' to upvote the post.
  """
    driver.find_element(by=AppiumBy.XPATH, value=initialization.upvote_post_Xpath).click()
    sleep(3)

def downvote():
    """
  Downvote a post.
  Clicks on the element identified by 'downvote_post_Xpath' to downvote the post.
  """
    driver.find_element(by=AppiumBy.XPATH, value=initialization.downvote_post_Xpath).click() 
    sleep(2)   

def comment():
    """
  Comments on a post.
  Clicks on the element identified by 'upvote_comment_Xpath' (might be upvote depending on the app). Waits 2 seconds.
  Then clicks on the element identified by 'downvote_comment_Xpath' (might be downvote depending on the app). Waits 5 seconds.
  Clicks on the comment field identified by 'comment_Xpath', waits 2 seconds, and enters the text "I think so". Waits 1 second.
  Finally, clicks on the element identified by 'post_comment_Xpath' to send the comment.
  """
    driver.find_element(by=AppiumBy.XPATH, value=initialization.comment_Xpath).click()
    sleep(2)

    comments = driver.find_element(by=AppiumBy.XPATH, value=initialization.add_comment_Xpath)
    comments.click()
    sleep(1)
    comments.send_keys("ALAHLY top")
    sleep(1)

    driver.hide_keyboard()
    sleep(1)

    driver.find_element(by=AppiumBy.XPATH, value=initialization.post_comment_Xpath).click()

def reply():
    driver.find_element(by=AppiumBy.XPATH, value=initialization.comment_Xpath).click()
    sleep(2)

    driver.find_element(by=AppiumBy.XPATH, value=initialization.upvote_comment_Xpath).click()
    sleep(2)

    driver.find_element(by=AppiumBy.XPATH, value=initialization.downvote_comment_Xpath).click()
    sleep(2)

    settings = driver.find_element(by=AppiumBy.XPATH, value=initialization.settings_comment_Xpath)
    settings.click()
    sleep(1)
    driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Save Comment").click()  # Block User or Report Comment
    sleep(2)

    driver.find_element(by=AppiumBy.XPATH, value=initialization.reply_Xpath).click()
    sleep(1)

    replies = driver.find_element(by=AppiumBy.XPATH, value=initialization.reply_Xpath)
    replies.click()
    sleep(2)
    replies.send_keys("You are right")

def share():
    """
  Shares a post to profile.
  Clicks on the element identified by 'share_Xpath' to open the share menu. Waits 2 seconds.
  """
    driver.find_element(by=AppiumBy.XPATH, value=initialization.share_Xpath).click()
    sleep(2)   

def chat():
    """
  Sends a message in a chat conversation.
  Clicks on the Chat tab.
  Clicks on the message field, enters the text "We are ready", and sends the message.
  Finally, closes the driver.
  """
    driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="""Chat
Tab 4 of 5""").click()
    sleep(3)

    driver.find_element(by=AppiumBy.XPATH, value=initialization.chat_Xpath).click()
    sleep(1)

    message = driver.find_element(by=AppiumBy.XPATH, value=initialization.message_Xpath)
    message.click()
    sleep(1)
    message.send_keys("We are ready")
    sleep(2)
    driver.find_element(by=AppiumBy.XPATH, value=initialization.send_Xpath).click()
    sleep(2)
    driver.quit()

def inbox():
    """
  Composes and sends a message in the Inbox.
  Clicks on the Inbox tab and then clicks on compose a new message.
  Clicks on the recipient field (send_to_Xpath), enters the recipient name "bahey1", clicks on the title field, 
  enters the title "Yala discord", and enters the message body "2oly ghayarto eh" in the message field.
  Finally, clicks on the send message element and closes the driver.
  """
    driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="""Inbox
Tab 5 of 5""").click()
    sleep(3)

    driver.find_element(by=AppiumBy.XPATH, value=initialization.compose_mess_Xpath).click()
    sleep(2)

    sendmessage = driver.find_element(by=AppiumBy.XPATH, value=initialization.send_to_Xpath)
    sendmessage.click()
    sleep(1)
    sendmessage.send_keys("bahey1")

    titlemessage = driver.find_element(by=AppiumBy.XPATH, value=initialization.title_Xpath)
    titlemessage.click()
    sleep(1)
    titlemessage.send_keys("Yala discord")
    sleep(1)

    bodymessage = driver.find_element(by=AppiumBy.XPATH, value=initialization.body_Xpath)
    bodymessage.click()
    sleep(1)
    bodymessage.send_keys("2oly ghayarto eh")
    sleep(1)

    driver.find_element(by=AppiumBy.XPATH, value=initialization.sendmess_Xpath).click()

# Uncomment the function you want
# change_posts()
# join_community()
# upvote()
# downvote()
# comment()
# reply()
# share()
# open_profile()
# edit_profile()
# chat()
# inbox()
# post_settings()
