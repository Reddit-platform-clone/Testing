from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import NamesRef
import NormalLogin

def CreatePost():
    """
    Function to create a new post on Reddit.

    This function logs in using predefined credentials, navigates to the page for creating a new post, fills in the
    title and body fields, and submits the post.

    Args:
        None

    Returns:
        None
    """
    driver = NormalLogin.login(NamesRef.login_username, NamesRef.login_password)

    # Wait until the create button appears and click on it
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, NamesRef.Create_Button)))
    create_button = driver.find_element(By.XPATH, NamesRef.Create_Button)
    create_button.click()

    # Fill in the title field
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, NamesRef.Title_field)))
    title_field = driver.find_element(By.XPATH, NamesRef.Title_field)
    title_field.send_keys("Testing Title")

    # Fill in the post body field
    post_body = driver.find_element(By.XPATH, NamesRef.Post_Body_field)
    post_body.send_keys("Testing the body field ")

    # Click on the submit button
    Submit_Button = driver.find_element(By.XPATH, NamesRef.Post_Submit_Button)
    Submit_Button.click()

    sleep(5)
    driver.quit()
