from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
import NamesRef
import NormalLogin

#data to test with it
email = "TestingTeam2@yopmail.com"
old_password = "Testing@2026"
new_password = "Testing@2027"

def ChangePassword(the_email, old_password, new_password):
   """
   Function to change the password of a Reddit account.

   This function logs in using above credentials, navigates to the settings, accesses the change password section,
   fills in the old and new password fields, and saves the changes.

   Args:
       the_email (str): The email of the Reddit account.
       old_password (str): The old password of the Reddit account.
       new_password (str): The new password to set for the Reddit account.

   Returns:
       None
   """
   # Login first before changing the password
   driver = NormalLogin.login(the_email, old_password)

   # Wait until the profile icon appears, then click on it to show the settings
   WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, NamesRef.profile_icon)))
   profile_icon = driver.find_element(By.XPATH, NamesRef.profile_icon)
   profile_icon.click()
   sleep(2)

   # Get the setting button then press on it
   setting_button = driver.find_element(By.XPATH, NamesRef.setting_button)
   setting_button.click()

   # Wait until the change password button appears, then press on it
   WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, NamesRef.change_pass_button)))
   changepassbutton = driver.find_element(By.XPATH, NamesRef.change_pass_button)
   changepassbutton.click()
   sleep(10)

   # Wait for the password fields to appear
   # Then getting the fields for old, new, and confirm password
   WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, NamesRef.old_password_field)))
   old_password_field = driver.find_element(By.CSS_SELECTOR, NamesRef.old_password_field)
   new_password_field = driver.find_element(By.CSS_SELECTOR, NamesRef.new_password_field)
   confirm_newpassword_field = driver.find_element(By.CSS_SELECTOR, NamesRef.confirm_newpassword_field)

   # Checking the fields are clear
   old_password_field.clear()
   new_password_field.clear()
   confirm_newpassword_field.clear()

   # Filling the password fields with data
   old_password_field.send_keys(old_password)
   new_password_field.send_keys(new_password)
   confirm_newpassword_field.send_keys(new_password)

   # Get the save button then press on it
   save_button = driver.find_element(By.XPATH, NamesRef.save_password_button)
   save_button.click()
   sleep(10)

   # Close the browser window
   driver.close()

