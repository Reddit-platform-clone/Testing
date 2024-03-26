from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import NamesRef



# Function to handle login
def login(username, password):
    # Initialize Chrome WebDriver
    driver = webdriver.Chrome()

    # Open the URL
    driver.get("https://www.reddit.com/")
    sleep(5)

    #get login button the click on it
    login_button = driver.find_element(By.ID, NamesRef.loginButton)
    login_button.click()
    sleep(2)

    #wait until fields appear
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "login-username")))

    #get username and password fields
    username_field = driver.find_element(By.ID, "login-username")
    password_field = driver.find_element(By.ID, "login-password")

    #make sure fields are clear
    username_field.clear()
    password_field.clear()

    #filling fields with data
    username_field.send_keys(username)
    password_field.send_keys(password)

    #submitting the form
    password_field.send_keys(Keys.RETURN)

    #detecting if the login successfull or not
    try:
        success_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//faceplate-toast[@type='success']")))
        print("Success message found.")
    except TimeoutException:
        print("Success message not found within timeout.")

    driver.quit()

# Testing different cases
def test_login():
    # Valid login
    print("Testing valid login...")
    login(NamesRef.login_username, NamesRef.login_password)

    # Invalid username
    print("Testing invalid username...")
    login("InvalidUsername", NamesRef.login_password)

    # Invalid password
    print("Testing invalid password...")
    login(NamesRef.login_username, "InvalidPassword")

    # Blank username
    print("Testing blank username...")
    login("", NamesRef.login_password)

    # Blank password
    print("Testing blank password...")
    login(NamesRef.login_username, "")

    # Blank username and password
    print("Testing blank username and password...")
    login("", "")

    # Password with leading/trailing spaces
    print("Testing password with leading/trailing spaces...")
    login(NamesRef.login_username, "  " + NamesRef.login_password + "  ")

