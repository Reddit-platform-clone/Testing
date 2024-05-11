from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import NamesRef
import NormalLogin


def Logout():
    """
    Function to log out from Sarakel.

    This function logs in using predefined credentials, hovers over the user avatar to reveal the logout button,
    clicks on the logout button, and verifies successful logout.

    Returns:
        None
    """
    driver = NormalLogin.login(NamesRef.login_username, NamesRef.login_password)
    sleep(3)

    # Find the user avatar element
    avatar_img = driver.find_element(By.XPATH, NamesRef.profile_icon)

    # Create an ActionChains object to perform mouse hover
    actions = ActionChains(driver)

    # Hover over the user avatar
    actions.move_to_element(avatar_img).perform()

    # Find and click the logout button
    logout = driver.find_element(By.XPATH, NamesRef.logout_btn)
    logout.click()

    try:
        # Wait until the login button appears after logout
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, NamesRef.login_button)))
        print("Logged out successfully")
    except NoSuchElementException as e:
        print("Error: Failed to logout.")
        print(e)

    sleep(5)
    driver.quit()
