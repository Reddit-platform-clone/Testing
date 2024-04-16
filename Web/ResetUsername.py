from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

import NamesRef

# Initialize Chrome WebDriver
driver = webdriver.Chrome()
# Open the URL
driver.get("https://www.reddit.com/username/")
sleep(5)

# Used data for testing
email = "TestingTeam2@yopmail.com"

def resetUsername(email):
    """
    Function to reset the username on Reddit.

    This function initializes the Chrome WebDriver, navigates to the username reset page on Reddit, fills in the email
    field, and submits the form.

    Args:
        email (str): The email associated with the Reddit account.

    Returns:
        None
    """
    # Get email field
    email_field = driver.find_element(By.CSS_SELECTOR, NamesRef.email_field)
    email_field.clear()

    # Send the email data to the field
    email_field.send_keys(email)

    # Submit the form
    submit_button = driver.find_element(By.CSS_SELECTOR, NamesRef.reset_username_submit_button)
    submit_button.click()

    sleep(5)

    # Quit the browser
    driver.quit()

# Execute the function
resetUsername(email)
