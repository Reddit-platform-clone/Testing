from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import NamesRef
import NormalLogin


def OtherProfile():
    """
    Function to navigate to another user's profile on Sarakel.

    This function logs in using predefined credentials, searches for another user's profile by username, and navigates
    to that profile page.

    Args:
        None

    Returns:
        None
    """
    # Log in using predefined credentials
    driver = NormalLogin.login(NamesRef.login_username, NamesRef.login_password)

    # Wait for some time to ensure the page is loaded
    sleep(10)

    # Wait until the search bar appears and then search for the specified username
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, NamesRef.search_bar)))
    search_bar = driver.find_element(By.XPATH, NamesRef.search_bar)
    search_bar.clear()
    sleep(5)
    search_bar.send_keys("Mission_Anteater1023")
    search_bar.send_keys(Keys.RETURN)

    ########## Functionality under construction ###############

    # Close the browser window
    driver.close()
