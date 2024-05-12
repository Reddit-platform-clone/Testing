
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
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
    search_bar.click()
    sleep(5)

    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, NamesRef.users_search_bar)))
    user_search_bar = driver.find_element(By.XPATH, NamesRef.users_search_bar)

    # Create an ActionChains object to perform mouse hover
    actions = ActionChains(driver)

    # Hover over the user avatar
    actions.move_to_element(user_search_bar).perform()

    user_search_bar.send_keys("hafez")
    sleep(5)


    first_result = driver.find_element(By.XPATH, NamesRef.first_user_profile)
    first_result.click()
    sleep(5)
    ########## Functionality under construction ###############

    # Close the browser window
    driver.close()
OtherProfile()