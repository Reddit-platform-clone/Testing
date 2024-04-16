from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import NamesRef

def login(username, password):
    """
    Function to login to Reddit.

    This function initializes the Chrome WebDriver, navigates to the Reddit login page, fills in the username and
    password fields, and submits the login form.

    Args:
        username (str): The username or email for logging in.
        password (str): The password for logging in.

    Returns:
        None
    """
    # Initialize Chrome WebDriver
    driver = webdriver.Chrome()

    # Open the URL
    driver.get("https://www.reddit.com/")
    sleep(5)

    # Get the login button and click on it
    login_button = driver.find_element(By.ID, NamesRef.login_button)
    login_button.click()
    sleep(2)

    # Wait until the fields appear
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "login-username")))

    # Get the username and password fields
    username_field = driver.find_element(By.ID, "login-username")
    password_field = driver.find_element(By.ID, "login-password")

    # Make sure fields are clear
    username_field.clear()
    password_field.clear()

    # Fill in the fields with data
    username_field.send_keys(username)
    password_field.send_keys(password)

    # Submit the form
    password_field.send_keys(Keys.RETURN)

    # Detect if the login is successful or not
    try:
        success_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//faceplate-toast[@type='success']")))
        print("Success message found.")
    except TimeoutException:
        print("Success message not found within timeout.")

    # Quit the browser
    driver.quit()

def test_login():
    """
    Function to test different login scenarios.

    This function tests various scenarios for logging in to Reddit.

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
