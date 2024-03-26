from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep


# Initialize Chrome WebDriver
driver = webdriver.Chrome()
# Open the URL
driver.get("https://www.reddit.com/password/")
sleep(5)

#data to test with it
username = "TestingTeam2025"
email = "TestingTeam2@yopmail.com"

def resetPassword(email, username):
    #get username and email fields
    email_field = driver.find_element(By.CSS_SELECTOR, "input[name='email']")
    username_field = driver.find_element(By.CSS_SELECTOR, "input[name='username']")

    #checking fields are clear
    email_field.clear()
    username_field.clear()

    #Sending email & username to their fields
    email_field.send_keys(email)
    username_field.send_keys(username)

    #press enter to submit
    email_field.send_keys(Keys.RETURN)
    sleep(5)

    driver.quit()
