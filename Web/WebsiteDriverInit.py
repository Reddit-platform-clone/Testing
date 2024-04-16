from selenium import webdriver

def init():
    """
    Initialize the Chrome WebDriver.

    This function initializes the Chrome WebDriver for Testing with Selenium automation.

    Args:
        None

    Returns:
        WebDriver: The WebDriver instance for Chrome.
    """
    # Initialize Chrome WebDriver
    driver = webdriver.Chrome()
    return driver
