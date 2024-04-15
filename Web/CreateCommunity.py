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
sleep(2)

def CreateCommunity():
    login(NamesRef.login_username, NamesRef.login_password)

    sleep(5)
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, NamesRef.nav_bar_button)))
    nav_bar_button = driver.find_element(By.XPATH, NamesRef.nav_bar_button)
    sleep(2)
    nav_bar_button.click()
    sleep(6)


    Create_Community_button = driver.find_element(By.XPATH, NamesRef.Create_Community_button)
    Create_Community_button.click()
    sleep(5)

    Community_name_field = driver.find_element(By.XPATH,)
    Community_name_field.send_keys("Testing community")

    Community_Submit = driver.find_element(By.XPATH,)
    Community_Submit.click()

    sleep(10)
    driver.quit()



def login(username, password):

   print("1")
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


CreateCommunity()