from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys
from time import sleep

#Data to test with it
the_email = "TestingTeam@yopmail.com"
the_password = "Testing@2025"
the_username = "TestingTeam2025"

# Initialize Chrome WebDriver
driver = webdriver.Chrome()

# Open the URL
driver.get("https://www.reddit.com/")

# Get and print the title
title = driver.title
print("Website Title:", title)
print(driver.current_url)

def ValidLogin():
    login = driver.find_element(By.ID, "login-button")
    login.click()

    sleep(2)
    login_Username = driver.find_element(By.ID, "login-username")
    login_Username.send_keys(the_username)

    login_password = driver.find_element(By.ID, "login-password")
    login_password.send_keys(the_password)
    sleep(2)
    login_password.send_keys(Keys.RETURN)

    # Locate the element containing the success message

    #under construction#####################
    #success_msg_element = WebDriverWait(driver,20).until(lambda x: x.find_element(By.CLASS_NAME, "alert-success"))

    # Get the text of the success message
    # success_msg = success_msg_element.text
    # print("Success message:", success_msg)
    driver.close()

def WrongUsername():
    login = driver.find_element(By.ID, "login-button")
    login.click()

    sleep(5)
    login_Username = driver.find_element(By.ID, "login-username")
    login_Username.send_keys("WrongOne")

    login_password = driver.find_element(By.ID, "login-password")
    login_password.send_keys(the_password)
    sleep(5)
    login_password.send_keys(Keys.RETURN)
    sleep(10)
    driver.close()

def WrongPass():
    login = driver.find_element(By.ID, "login-button")
    login.click()

    sleep(5)
    login_Username = driver.find_element(By.ID, "login-username")
    login_Username.send_keys(the_username)

    login_password = driver.find_element(By.ID, "login-password")
    login_password.send_keys("WrongPassword")
    sleep(5)
    login_password.send_keys(Keys.RETURN)
    sleep(10)
    driver.close()

def BlanckUsername():
    login = driver.find_element(By.ID, "login-button")
    login.click()

    sleep(5)
    login_Username = driver.find_element(By.ID, "login-username")
    login_Username.send_keys("")

    login_password = driver.find_element(By.ID, "login-password")
    login_password.send_keys(the_password)
    sleep(5)
    login_password.send_keys(Keys.RETURN)
    sleep(10)
    driver.close()

def BlanckPassword():
    login = driver.find_element(By.ID, "login-button")
    login.click()

    sleep(5)
    login_Username = driver.find_element(By.ID, "login-username")
    login_Username.send_keys(the_username)

    login_password = driver.find_element(By.ID, "login-password")
    login_password.send_keys("")
    sleep(5)
    login_password.send_keys(Keys.RETURN)
    sleep(10)
    driver.close()

def BlanckBoth():
    login = driver.find_element(By.ID, "login-button")
    login.click()

    sleep(5)
    login_Username = driver.find_element(By.ID, "login-username")
    login_Username.send_keys("")

    login_password = driver.find_element(By.ID, "login-password")
    login_password.send_keys("")
    sleep(5)
    login_password.send_keys(Keys.RETURN)
    sleep(10)
    driver.close()

#Testing The Valid Case
ValidLogin()
