from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import NamesRef


def googleOauth():
    """
    Perform OAuth authentication using Google account.

    This function initializes the Chrome WebDriver, opens the Sarakel website, clicks on the login button,
    clicks on the Google OAuth button, handles the new window/tab, enters Google account credentials, and completes
    the authentication process. It prints an error message if authentication fails.

    Returns:
        None
    """
    try:
        # Initialize the Chrome WebDriver
        driver = webdriver.Chrome()

        # Open the Sarakel website
        driver.get("http://www.sarakel.me/")
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, NamesRef.login_button)))

        # Find and click on the login button
        login_button = driver.find_element(By.XPATH, NamesRef.login_button)
        login_button.click()

        # Find and click on the button/link to start OAuth authentication
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, NamesRef.google_button)))
        oauth_button = driver.find_element(By.XPATH, NamesRef.google_button)
        oauth_button.click()

        sleep(10)  # Wait for the OAuth popup to appear

        # After clicking on the OAuth authentication button, handle the new window/tab
        main_window = driver.current_window_handle
        all_windows = driver.window_handles

        # Switch to the new window/tab
        new_window = [window for window in all_windows if window != main_window][0]
        driver.switch_to.window(new_window)

        # Enter Google account credentials
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, NamesRef.oauth_email_field)))
        email_field = driver.find_element(By.XPATH, NamesRef.oauth_email_field)
        email_field.send_keys(NamesRef.gmail_account)
        email_field.send_keys(Keys.RETURN)

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, NamesRef.oauth_password_field)))
        password_field = driver.find_element(By.XPATH, NamesRef.oauth_password_field)
        password_field.send_keys(NamesRef.gmail_password)
        password_field.send_keys(Keys.RETURN)

        # Wait for authentication to complete
        sleep(7)

        # Print success message
        print("OAuth authentication successful.")

    except Exception as e:
        # Print error message if authentication fails
        print("Error during OAuth authentication:", str(e))

    finally:
        # Close the WebDriver
        driver.quit()
