from selenium.webdriver.common.by import By
from time import sleep
import NamesRef
import NormalLogin

def CreateCommunity():
    """
    Function to create a new community on Sarakel.

    This function logs in using predefined credentials, navigates to the community creation page, fills in the necessary
    details, and submits the form to create a new community.

    Args:
        None

    Returns:
        None
    """
    # Login using predefined credentials
    driver = NormalLogin.login(NamesRef.login_username, NamesRef.login_password)

    sleep(3)

    # Click on the button to create a community
    Create_Community_button = driver.find_element(By.XPATH, NamesRef.create_community_button)
    Create_Community_button.click()
    sleep(5)

    # Find the community name field and fill it
    Community_name_field = driver.find_element(By.XPATH, NamesRef.community_name_field)
    Community_name_field.send_keys("Testing community")

    # Locate the radio button element by its ID and click on it
    radio_button = driver.find_element(By.XPATH, NamesRef.community_radio_btn)
    radio_button.click()

    # Locate the checkbox element and click on it to toggle its state
    checkbox = driver.find_element(By.XPATH, NamesRef.community_check_box)
    checkbox.click()

    sleep(3)

    # Find the submit button and click on it to create the community
    Community_Submit = driver.find_element(By.XPATH, NamesRef.community_submit)
    Community_Submit.click()

    sleep(10)
    driver.quit()
