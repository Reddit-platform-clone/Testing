from selenium.webdriver.common.by import By
from time import sleep
import NamesRef
import NormalLogin


def NavFeatures():
    """
    Function to navigate through various features on Sarakel after login.

    This function logs in using predefined credentials and navigates to the home page, Test navigation bar,
    opens the chat, and opens the
    inbox.

    Args:
        None.

    Returns:
        None.
    """
    driver = NormalLogin.login(NamesRef.login_username, NamesRef.login_password)

    # Click on the Home button
    Home_button = driver.find_element(By.XPATH, NamesRef.Home_button)
    Home_button.click()
    sleep(2)

    # Click on the open chat button
    open_chat_button = driver.find_element(By.XPATH, NamesRef.open_chat)
    open_chat_button.click()
    sleep(2)

    # Click on the open inbox button
    open_inbox_button = driver.find_element(By.XPATH, NamesRef.open_inbox)
    open_inbox_button.click()
    sleep(2)

    # Close the browser window
    driver.quit()
