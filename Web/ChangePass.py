from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import NamesRef

# Initialize Chrome WebDriver
driver = webdriver.Chrome()
# Open the URL
driver.get("https://www.reddit.com/")
sleep(5)

#data to test with it
email = "TestingTeam2@yopmail.com"
old_password = "Testing@2026"
new_password = "Testing@2027"

def ChangePassword(the_email, old_password, new_password):

   #login first before changing password
   login(the_email, old_password)

   # wait until profile icon appear then press on it to show the settings
   WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//*[@id='expand-user-drawer-button']/span/span/span/span/img")))
   profile_icon = driver.find_element(By.XPATH, "//*[@id='expand-user-drawer-button']/span/span/span/span/img")
   profile_icon.click()
   sleep(2)

   #get setting button the press on it
   setting_button = driver.find_element(By.XPATH, "//*[@id='user-drawer-content']/ul[3]/faceplate-tracker/li/a/span[1]/span[2]/span[1]")
   setting_button.click()

   #wait until change password button appear then press on it
   WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//*[@id='AppRouter-main-content']/div/div[2]/div[1]/div[2]/div[2]/div/button")))
   changepassbutton = driver.find_element(By.XPATH, "//*[@id='AppRouter-main-content']/div/div[2]/div[1]/div[2]/div[2]/div/button")
   changepassbutton.click()
   sleep(10)

   #wait for the password fields to appear
   #Then getting the fields for old, new and confirm password
   WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[id='old_password']")))
   old_password_field = driver.find_element(By.CSS_SELECTOR, "input[id='old_password']")
   new_password_field = driver.find_element(By.CSS_SELECTOR, "input[id='password']")
   confirm_newpassword_field = driver.find_element(By.CSS_SELECTOR, "input[id='password2']")

   #checking the fields are clear
   old_password_field.clear()
   new_password_field.clear()
   confirm_newpassword_field.clear()

   #filling the password fields with data
   old_password_field.send_keys(old_password)
   new_password_field.send_keys(new_password)
   confirm_newpassword_field.send_keys(new_password)

   #get the save button then press on it
   save_button = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/form/fieldset[5]/button")
   save_button.click()
   sleep(10)

   driver.close()

def login(username, password):

   #get login button then press on it
   login_button = driver.find_element(By.ID, NamesRef.loginButton)
   login_button.click()
   sleep(2)

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

   sleep(5)
