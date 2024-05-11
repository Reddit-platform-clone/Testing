from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import NamesRef
import WebsiteDriverInit


def login(username = NamesRef.login_username, password = NamesRef.login_password):
    """
    Function to log in to Sarakel using provided credentials.

    This function initializes the WebDriver, navigates to the Sarakel website, locates the login button, fills in the
    username and password fields, and submits the login form.

    Args:
        username (str): The username or email for logging in.
        password (str): The password for logging in.

    Returns:
        WebDriver: The WebDriver instance after successful login.
    """

    # Initialize the WebDriver
    driver = WebsiteDriverInit.init()

    # Navigate to Sarakel
    driver.get("http://www.sarakel.me/")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, NamesRef.login_button)))

    # Find and click on the login button
    login_button = driver.find_element(By.XPATH, NamesRef.login_button)
    login_button.click()

    # Wait until the login fields appear
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, NamesRef.login_field_Normal)))

    # Find the username and password fields
    username_field = driver.find_element(By.XPATH, NamesRef.login_field_Normal)
    password_field = driver.find_element(By.XPATH, NamesRef.password_field_Normal)

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
        print("Default Login failed:", error_message.text)
        driver.quit()
        return False
    except NoSuchElementException:
        # No error message found, login successful
        print("Login successful!")
        return driver
