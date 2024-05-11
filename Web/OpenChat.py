from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import NamesRef
import NormalLogin

def SendPrivMsg():
    """
    Function to send a private message to another user.

    This function logs in using predefined credentials, opens the chat, fills in the recipient's name, subject, and body
    of the message, and sends the message.

    Args:
        None

    Returns:
        None
    """
    # Login using predefined credentials
    driver = NormalLogin.login(NamesRef.login_username, NamesRef.login_password)
    sleep(5)

    # Click on the button to open the chat
    open_chat_btn = driver.find_element(By.XPATH, NamesRef.open_chat_btn)
    open_chat_btn.click()
    sleep(5)

    # Fill in recipient's name
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, NamesRef.msg_to_field)))
    msg_to = driver.find_element(By.XPATH, NamesRef.msg_to_field)
    msg_to.send_keys(NamesRef.msg_receiver_name)

    # Fill in message subject
    msg_subject = driver.find_element(By.XPATH, NamesRef.msg_subject_field)
    msg_subject.send_keys("Msg Subject testing")

    # Fill in message body
    msg_body = driver.find_element(By.XPATH, NamesRef.msg_content_field)
    msg_body.send_keys("Msg Body Testing")

    # Click on the send button
    msg_submit = driver.find_element(By.XPATH, NamesRef.msg_send_btn)
    msg_submit.click()

    sleep(5)
    driver.quit()

def OpenInbox():
    """
    Function to navigate to the user's inbox and view different types of messages.

    This function logs in using predefined credentials, opens the chat, and navigates through the inbox to view
    different types of messages.

    Args:
        None

    Returns:
        None
    """
    # Login using predefined credentials
    driver = NormalLogin.login(NamesRef.login_username, NamesRef.login_password)
    sleep(5)

    # Click on the button to open the chat
    open_chat_btn = driver.find_element(By.XPATH, NamesRef.open_chat_btn)
    open_chat_btn.click()
    sleep(3)

    # Click on the inbox section
    inbox_section = driver.find_element(By.XPATH, NamesRef.inbox_section)
    inbox_section.click()
    sleep(3)

    # Click on different inbox categories to view messages
    inbox_All = driver.find_element(By.XPATH, NamesRef.inbox_All)
    inbox_All.click()
    sleep(3)

    inbox_unread = driver.find_element(By.XPATH, NamesRef.inbox_unread)
    inbox_unread.click()
    sleep(3)

    inbox_messages = driver.find_element(By.XPATH, NamesRef.inbox_messages)
    inbox_messages.click()
    sleep(3)

    inbox_comment_replies = driver.find_element(By.XPATH, NamesRef.inbox_comment_replies)
    inbox_comment_replies.click()
    sleep(3)

    inbox_post_replies = driver.find_element(By.XPATH, NamesRef.inbox_post_replies)
    inbox_post_replies.click()
    sleep(3)

    inbox_username_mentions = driver.find_element(By.XPATH, NamesRef.inbox_username_mentions)
    inbox_username_mentions.click()
    sleep(3)

    driver.quit()

def OpenSent():
    """
    Function to navigate to the user's sent messages.

    This function logs in using predefined credentials, opens the chat, and navigates to the sent messages section.

    Args:
        None

    Returns:
        None
    """
    # Login using predefined credentials
    driver = NormalLogin.login(NamesRef.login_username, NamesRef.login_password)
    sleep(5)

    # Click on the button to open the chat
    open_chat_btn = driver.find_element(By.XPATH, NamesRef.open_chat_btn)
    open_chat_btn.click()
    sleep(3)

    # Click on the sent messages section
    sent_msgs = driver.find_element(By.XPATH, NamesRef.sent_msgs_section)
    sent_msgs.click()
    sleep(3)

    driver.quit()
