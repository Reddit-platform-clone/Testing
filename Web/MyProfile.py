from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
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

    # Wait until profile icon appears, then click on it to show the settings
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, NamesRef.profile_icon)))

    # Find the profile icon element
    avatar_img = driver.find_element(By.XPATH, NamesRef.profile_icon)

    # Create an ActionChains object to perform mouse hover
    actions = ActionChains(driver)

    # Hover over the profile icon
    actions.move_to_element(avatar_img).perform()

    sleep(3)

    # Test View Profile option
    view_profile = driver.find_element(By.XPATH, NamesRef.view_profile)
    view_profile.click()
    sleep(3)

    # Test Overview Section
    Overview_button = driver.find_element(By.XPATH, NamesRef.profile_overview_button)
    Overview_button.click()
    sleep(3)

    # Test Posts Section
    Posts_button = driver.find_element(By.XPATH, NamesRef.profile_posts_button)
    Posts_button.click()
    sleep(3)

    # Test Comments Section
    Comments_button = driver.find_element(By.XPATH, NamesRef.profile_comments_button)
    Comments_button.click()
    sleep(3)

    # Test Saved Section
    Saved_button = driver.find_element(By.XPATH, NamesRef.profile_saved_button)
    Saved_button.click()
    sleep(3)

    # Test Hidden Section
    Hidden_button = driver.find_element(By.XPATH, NamesRef.profile_hidden_button)
    Hidden_button.click()
    sleep(3)

    # Test Upvoted Section
    Upvoted_button = driver.find_element(By.XPATH, NamesRef.profile_upvoted_button)
    Upvoted_button.click()
    sleep(3)

    # Test Downvoted Section
    Downvoted_button = driver.find_element(By.XPATH, NamesRef.profile_downvoted_button)
    Downvoted_button.click()
    sleep(3)

    # Redirect to create post section
    create_post = driver.find_element(By.XPATH, NamesRef.Create_Post_section_in_profile)
    create_post.click()
    sleep(5)

    # Return to profile page to continue script
    # Find the profile icon element
    avatar_img = driver.find_element(By.XPATH, NamesRef.profile_icon)

    # Hover over the profile icon
    actions = ActionChains(driver)
    actions.move_to_element(avatar_img).perform()
    sleep(3)

    # Test View Profile option again
    view_profile = driver.find_element(By.XPATH, NamesRef.view_profile)
    view_profile.click()
    sleep(3)

    # Go to edit profile section
    edit_profile = driver.find_element(By.XPATH, NamesRef.edit_profile_section_in_profile)
    edit_profile.click()
    sleep(5)

    # Close the browser window
    driver.close()
