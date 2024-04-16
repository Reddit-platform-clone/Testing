from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import NamesRef
import NormalLogin


def MyProfile():
    """
    Function to navigate to the user's profile page and interact with various profile options.

    This function logs in using predefined credentials, navigates to the user's profile, and tests various profile options.

    Args:
        None

    Returns:
        None
    """

    # Login using predefined credentials
    driver = NormalLogin.login(NamesRef.login_username, NamesRef.login_password)

    # wait until profile icon appears, then click on it to show the settings
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, NamesRef.profile_icon)))
    profile_icon = driver.find_element(By.XPATH, NamesRef.profile_icon)
    profile_icon.click()
    sleep(2)

    # Tests view profile
    view_profile = driver.find_element(By.XPATH, NamesRef.view_profile)
    view_profile.click()
    sleep(3)

    # Tests Overview Section
    Overview_button = driver.find_element(By.XPATH, NamesRef.profile_overview_button)
    Overview_button.click()
    sleep(3)

    # Tests Posts Section
    Posts_button = driver.find_element(By.XPATH, NamesRef.profile_posts_button)
    Posts_button.click()
    sleep(3)

    # Tests Comments Section
    Comments_button = driver.find_element(By.XPATH, NamesRef.profile_comments_button)
    Comments_button.click()
    sleep(3)

    # Tests Saved Section
    Saved_button = driver.find_element(By.XPATH, NamesRef.profile_saved_button)
    Saved_button.click()
    sleep(3)

    # Tests Hidden Section
    Hidden_button = driver.find_element(By.XPATH, NamesRef.profile_hidden_button)
    Hidden_button.click()
    sleep(3)

    # Tests Upvoted Section
    Upvoted_button = driver.find_element(By.XPATH, NamesRef.profile_upvoted_button)
    Upvoted_button.click()
    sleep(3)

    # Tests Downvoted Section
    Downvoted_button = driver.find_element(By.XPATH, NamesRef.profile_downvoted_button)
    Downvoted_button.click()
    sleep(3)

    # Close the browser window
    driver.close()


MyProfile()
