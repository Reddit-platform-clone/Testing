from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import NamesRef
from selenium.common.exceptions import NoSuchElementException
import random
import string


# Data to test with it
username = NamesRef.login_username

def resetPassword(username):
    """
    Function to reset the password on Sarakel.

    This function initializes the Chrome WebDriver, navigates to the password reset page on Sarakel, fills in the
    username field, and submits the form.

    Args:
        email (str): The email associated with the Sarakel account
        username (str): The username associated with the Sarakel account.

    Returns:
        None
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

    password_href = driver.find_element(By.XPATH, NamesRef.reset_password_href)
    password_href.click()

    # Get email and username fields
    username_field = driver.find_element(By.XPATH, NamesRef.username_field)

    # Send username
    username_field.send_keys(username)

    # Submit the form
    submit_button = driver.find_element(By.XPATH, NamesRef.reset_password_submit_button)
    submit_button.click()


    sleep(3)
    # Check if Reset Password was successful
    try:
        # Look for the error message
        error_message = driver.find_element(By.XPATH, "//div[contains(text(), 'reset email sent')]")
        print("Reset Password successful", error_message.text)
        driver.quit()
        return True
    except NoSuchElementException:
        # No error message found,
        print("Reset Password failed")
        driver.quit()
        return False
def createFakeUsername():
    """
    Function to generate a random Username.

    Returns:
        str: Randomly generated Username.
    """
    # Generate a random string of letters and digits for the username
    fake_username = ''.join(random.choices(string.ascii_letters + string.digits, k=10))

    return fake_username

def resetPasswordWrongUsername():
    """
    Function to reset the password on Sarakel.

    This function initializes the Chrome WebDriver, navigates to the password reset page on Sarakel, fills
     username field with wrong username, and submits the form.

    Args:
        email (str): The email associated with the Sarakel account
        username (str): The username associated with the Sarakel account.

    Returns:
        None
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

    password_href = driver.find_element(By.XPATH, NamesRef.reset_password_href)
    password_href.click()

    # Get username field
    username_field = driver.find_element(By.XPATH, NamesRef.username_field)

    # Send username
    wrong_username = createFakeUsername()
    username_field.send_keys(wrong_username)

    # Submit the form
    submit_button = driver.find_element(By.XPATH, NamesRef.reset_password_submit_button)
    submit_button.click()


    sleep(3)
    # Check if Reset Password was successful
    try:
        # Look for the error message
        error_message = driver.find_element(By.XPATH, "//div[contains(text(), 'invalid username')]")
        print("Reset Password successful with wrong username", error_message.text)
        driver.quit()
        return True
    except NoSuchElementException:
        # No error message found,
        print("Reset Password failed with wrong username")
        driver.quit()
        return False

