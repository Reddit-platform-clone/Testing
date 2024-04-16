from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import NamesRef
import NormalLogin

def CreateCommunity():
    """
    Function to create a new community on Reddit.

    This function logs in using predefined credentials, navigates to the community creation page, fills in the necessary
    details, and submits the form to create a new community.

    Args:
        None

    Returns:
        None
    """
    driver = NormalLogin.login(NamesRef.login_username, NamesRef.login_password)

    sleep(5)

    # Wait until the navigation bar button appears and click on it
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, NamesRef.nav_bar_button)))
    nav_bar_button = driver.find_element(By.XPATH, NamesRef.nav_bar_button)
    sleep(2)
    nav_bar_button.click()
    sleep(6)

    # Click on the button to create a community
    Create_Community_button = driver.find_element(By.XPATH, NamesRef.create_community_button)
    Create_Community_button.click()
    sleep(5)

    # Find the community name field and fill it
    Community_name_field = driver.find_element(By.XPATH, NamesRef.community_name_field)
    Community_name_field.send_keys("Testing community")

    # Find the submit button and click on it
    Community_Submit = driver.find_element(By.XPATH, NamesRef.community_submit)
    Community_Submit.click()

    sleep(10)
    driver.quit()

CreateCommunity()
