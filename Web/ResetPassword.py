from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import NamesRef

# Initialize Chrome WebDriver
driver = webdriver.Chrome()
# Open the URL
driver.get("https://www.reddit.com/password/")
sleep(5)

# Data to test with it
username = "TestingTeam2025"
email = "TestingTeam2@yopmail.com"

def resetPassword(email, username):
    """
    Function to reset the password on Reddit.

    This function initializes the Chrome WebDriver, navigates to the password reset page on Reddit, fills in the email
    and username fields, and submits the form.

    Args:
        email (str): The email associated with the Reddit account.
        username (str): The username associated with the Reddit account.

    Returns:
        None
    """
    # Get email and username fields
    email_field = driver.find_element(By.CSS_SELECTOR, NamesRef.email_field)
    username_field = driver.find_element(By.CSS_SELECTOR, NamesRef.username_field)

    # Check fields are clear
    email_field.clear()
    username_field.clear()

    # Send email and username to their fields
    email_field.send_keys(email)
    username_field.send_keys(username)

    # Press enter to submit
    email_field.send_keys(Keys.RETURN)
    sleep(5)

    # Quit the browser
    driver.quit()

# Execute the function
resetPassword(email, username)
