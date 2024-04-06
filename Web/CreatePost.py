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

def CreatePost():
    login(NamesRef.login_username, NamesRef.login_password)

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, NamesRef.Create_Button)))
    create_button = driver.find_element(By.XPATH, NamesRef.Create_Button)
    create_button.click()

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, NamesRef.Title_field)))
    title_field = driver.find_element(By.XPATH, NamesRef.Title_field)
    title_field.send_keys("Testing Title")

    post_body = driver.find_element(By.XPATH, NamesRef.Post_Body_field)
    post_body.send_keys("Testing the body field ")

    Submit_Button = driver.find_element(By.XPATH, NamesRef.Post_Submit_Button)
    Submit_Button.click()

    sleep(5)
    driver.quit()



def login(username, password):

   print("1")
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

CreatePost()