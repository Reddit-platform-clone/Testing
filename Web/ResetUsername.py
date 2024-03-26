from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep


# Initialize Chrome WebDriver
driver = webdriver.Chrome()
# Open the URL
driver.get("https://www.reddit.com/username/")
sleep(5)

#Used date for testing
email = "TestingTeam2@yopmail.com"

def resetUsername(email):
    # get email field
    email_field = driver.find_element(By.CSS_SELECTOR, "input[name='email']")
    email_field.clear()

    #send the data to the field
    email_field.send_keys(email)

    #submitting the form
    submit_button = driver.find_element(By.CSS_SELECTOR, "input[type='submit']")
    submit_button.click()

    sleep(5)
    driver.quit()

