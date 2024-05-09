from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from time import sleep
import NamesRef


def login(username, password):
    """
    Function to login to Sarakel.

    This function initializes the Chrome WebDriver, navigates to the Sarakel login page, fills in the username and
    password fields, and submits the login form.

    Args:
        username (str): The username or email for logging in.
        password (str): The password for logging in.

    Returns:
        None
    """
    # Initialize Chrome WebDriver
    driver = webdriver.Chrome()

    # Navigate to Sarakel.
    driver.get("http://www.sarakel.me/")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, NamesRef.login_button)))

    # Find and click on the login button
    login_button = driver.find_element(By.XPATH, NamesRef.login_button)
    login_button.click()

    # Wait until the login fields appear
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, NamesRef.login_field)))

    # Find the username and password fields
    username_field = driver.find_element(By.ID, NamesRef.login_field)
    password_field = driver.find_element(By.ID, NamesRef.password_field)

    # Clear the fields
    username_field.clear()
    password_field.clear()

    # Fill in the fields with provided username and password
    username_field.send_keys(username)
    password_field.send_keys(password)


    # Submit the login form
    submit_login_button = driver.find_element(By.XPATH, NamesRef.submit_login_button)
    submit_login_button.click()
    sleep(3)

    # Check if login was successful
    try:
        # Look for the error message
        error_message = driver.find_element(By.XPATH, "//div[contains(text(), 'Invalid username or password.')]")
        print("Login failed:", error_message.text)
        driver.quit()
        return False
    except NoSuchElementException:
        # No error message found, login successful
        print("Login successful!")
        driver.quit()
        return True


def test_login():
    """
    Function to test different login scenarios.

    This function tests various scenarios for logging in to Sarakel.

    Args:
        None

    Returns:
        None
    """
    # Valid login
    print("Testing valid login...")
    login(NamesRef.login_username, NamesRef.login_password)

    # Invalid username
    print("Testing invalid username...")
    login("InvalidUsername", NamesRef.login_password)

    # Invalid password
    print("Testing invalid password...")
    login(NamesRef.login_username, "InvalidPassword")

    # Blank username
    print("Testing blank username...")
    login("", NamesRef.login_password)

    # Blank password
    print("Testing blank password...")
    login(NamesRef.login_username, "")

    # Blank username and password
    print("Testing blank username and password...")
    login("", "")

    # Password with leading/trailing spaces
    print("Testing password with leading/trailing spaces...")
    login(NamesRef.login_username, "  " + NamesRef.login_password + "  ")
