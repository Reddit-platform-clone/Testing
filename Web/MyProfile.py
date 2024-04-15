from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import NamesRef

# Initialize Chrome WebDriver
driver = webdriver.Chrome()
# Open the URL
driver.get("https://www.reddit.com/")
sleep(5)


def MyProfile():
    login(NamesRef.login_username, NamesRef.login_password)


    # wait until profile icon appear then press on it to show the settings
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, NamesRef.Profile_Icon)))
    profile_icon = driver.find_element(By.XPATH, NamesRef.Profile_Icon)
    profile_icon.click()
    sleep(2)

    view_profile = driver.find_element(By.XPATH, NamesRef.View_Profile)
    view_profile.click()
    sleep(3)

    Overview_button = driver.find_element(By.XPATH, NamesRef.Profile_Overview_button)
    Overview_button.click()
    sleep(5)

    Posts_button = driver.find_element(By.XPATH, NamesRef.Profile_Posts_button)
    Posts_button.click()
    sleep(5)

    Comments_button = driver.find_element(By.XPATH, NamesRef.Profile_Comments_button)
    Comments_button.click()
    sleep(5)

    Saved_button = driver.find_element(By.XPATH, NamesRef.Profile_Saved_button)
    Saved_button.click()
    sleep(5)

    Hidden_button = driver.find_element(By.XPATH, NamesRef.Profile_Hidden_button)
    Hidden_button.click()
    sleep(5)

    Upvoted_button = driver.find_element(By.XPATH, NamesRef.Profile_Upvoted_button)
    Upvoted_button.click()
    sleep(5)

    Downvoted_button = driver.find_element(By.XPATH, NamesRef.Profile_Downvoted_button)
    Downvoted_button.click()
    sleep(5)


    driver.close()



def login(username, password):

   #get login button then press on it
   login_button = driver.find_element(By.ID, NamesRef.loginButton)
   login_button.click()

   #wait untill fields to appear
   WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "login-username")))

   #get the fields for username & password
   username_field = driver.find_element(By.ID, "login-username")
   password_field = driver.find_element(By.ID, "login-password")

   #make sure fields are clear
   username_field.clear()
   password_field.clear()

   #filling the fields with data
   username_field.send_keys(username)
   password_field.send_keys(password)

   #submitting the form
   password_field.send_keys(Keys.RETURN)

MyProfile()