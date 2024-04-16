from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
import NamesRef

def OAuth():
    """
    Function to perform OAuth login on Reddit using Google.

    This function initializes the Chrome WebDriver, opens the Reddit login page, clicks on the Google login button,
    and initiates the OAuth process.

    Args:
        None

    Returns:
        None
    """
    # Initialize Chrome WebDriver
    driver = webdriver.Chrome()

    # Open the Reddit login page
    driver.get("https://www.reddit.com/login/")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, NamesRef.google_button)))

    # Click on the Google login button
    google_button = driver.find_element(By.XPATH, NamesRef.google_button)
    google_button.click()
    sleep(5)
    ########## Still under construction ##########

    # Quit the browser
    driver.quit()

OAuth()
