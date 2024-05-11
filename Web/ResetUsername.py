from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from time import sleep
import NamesRef
import random
import string


# Used data for testing
email = NamesRef.login_email

def resetUsername(email):
    """
    Function to reset the username on Sarakel.

    This function initializes the Chrome WebDriver, navigates to the username reset page on Sarakel, fills in the email
    field, and submits the form.

    Args:
        email (str): The email associated with the Sarakel account.

    Returns:
        True/False Based on test.
    """
    # Initialize Chrome WebDriver
    driver = webdriver.Chrome()
    # Open the URL
    driver.get("https://www.sarakel.me/")
    sleep(5)

    # Find and click on the login button
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, NamesRef.login_button)))
    login_button = driver.find_element(By.XPATH, NamesRef.login_button)
    login_button.click()

    username_href = driver.find_element(By.XPATH, NamesRef.reset_username_href)
    username_href.click()

    # Get email field
    email_field = driver.find_element(By.XPATH, NamesRef.email_field)
    email_field.clear()

    # Send the email data to the field
    email_field.send_keys(email)

    # Submit the form
    submit_button = driver.find_element(By.XPATH, NamesRef.reset_username_submit_button)
    submit_button.click()

    sleep(3)

    # Check if Reset Username was successful
    try:
        # Look for the error message
        error_message = driver.find_element(By.XPATH, "//div[contains(text(), 'reset email sent')]")
        print("Reset Username successful", error_message.text)
        driver.quit()
        return True
    except NoSuchElementException:
        # No error message found,
        print("Reset Username failed")
        driver.quit()
        return False

def createFakeEmail():
    """
    Function to generate a random email address.

    Returns:
        str: Randomly generated email address.
    """
    # Generate a random string of letters and digits for the username
    username = ''.join(random.choices(string.ascii_letters + string.digits, k=10))

    # Add a domain name
    the_email = username + '@yopmail.com'
    return the_email

def resetUsernameWrongEmail():
    """
    Function to reset the username on Sarakel.

    This function initializes the Chrome WebDriver, navigates to the username reset page on Sarakel, fills in the email
    field with wrong data, and submits the form.

    Args:
        email (str): The email associated with the Sarakel account.

    Returns:
                True/False Based on test.
    """
    # Initialize Chrome WebDriver
    driver = webdriver.Chrome()
    # Open the URL
    driver.get("https://www.sarakel.me/")
    sleep(5)

    # Find and click on the login button
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, NamesRef.login_button)))
    login_button = driver.find_element(By.XPATH, NamesRef.login_button)
    login_button.click()

    username_href = driver.find_element(By.XPATH, NamesRef.reset_username_href)
    username_href.click()

    # Get email field
    email_field = driver.find_element(By.XPATH, NamesRef.email_field)
    email_field.clear()

    # Send the fake email data to the field
    fake_email = createFakeEmail()
    email_field.send_keys(fake_email)

    # Submit the form
    submit_button = driver.find_element(By.XPATH, NamesRef.reset_username_submit_button)
    submit_button.click()

    sleep(3)

    # Check if Reset Username was successful
    try:
        # Look for the error message
        error_message = driver.find_element(By.XPATH, "//div[contains(text(), 'Email is not registered')]")
        print("Reset Username with wrong mail successful", error_message.text)
        driver.quit()
        return True
    except NoSuchElementException:
        # No error message found
        print("Reset Username failed with false data")
        driver.quit()
        return False





