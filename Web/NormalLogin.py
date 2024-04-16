from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import NamesRef
import WebsiteDriverInit


def login(username, password):
    """
    Function to log in to Reddit using provided credentials.

    This function initializes the WebDriver, navigates to the Reddit website, locates the login button, fills in the
    username and password fields, and submits the login form.

    Args:
        username (str): The username or email for logging in.
        password (str): The password for logging in.

    Returns:
        WebDriver: The WebDriver instance after successful login.
    """

    # Initialize the WebDriver
    driver = WebsiteDriverInit.init()

    # Navigate to Reddit
    driver.get("https://www.reddit.com/")
    sleep(5)

    # Find and click on the login button
    login_button = driver.find_element(By.ID, NamesRef.login_button)
    login_button.click()

    # Wait until the login fields appear
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "login-username")))

    # Find the username and password fields
    username_field = driver.find_element(By.ID, "login-username")
    password_field = driver.find_element(By.ID, "login-password")

    # Clear the fields
    username_field.clear()
    password_field.clear()

    # Fill in the fields with provided username and password
    username_field.send_keys(username)
    password_field.send_keys(password)

    # Submit the login form
    password_field.send_keys(Keys.RETURN)

    return driver
