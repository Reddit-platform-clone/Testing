from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
import NamesRef
import NormalLogin

def ChangeEmail(current_email, new_email, the_password):
   """
   Function to change the email of a Sarakel account.

   This function logs in using the provided credentials, navigates to the settings,
   accesses the change email section, fills in the old and new email fields, and saves the changes.

   Args:
       current_email (str): The current email of the Sarakel account.
       new_email (str): The new email to set for the Sarakel account.
       the_password (str): The password for the Sarakel account.

   Returns:
       None
   """
   # Login first before changing the email
   driver = NormalLogin.login(current_email, the_password)

   # Wait until the profile icon appears, then click on it to show the settings
   WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, NamesRef.profile_icon)))
   profile_icon = driver.find_element(By.XPATH, NamesRef.profile_icon)
   profile_icon.click()
   sleep(2)

   # Find and click on the settings button
   setting_button = driver.find_element(By.XPATH, NamesRef.setting_button)
   setting_button.click()

   # Wait until the change email button appears, then click on it
   WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, NamesRef.change_email_button)))
   change_email_button = driver.find_element(By.XPATH, NamesRef.change_email_button)
   change_email_button.click()
   sleep(10)

   # Find the field for entering the new email
   new_email_field = driver.find_element(By.XPATH, NamesRef.new_email_field)

   # Clear the new email field before entering the new email
   new_email_field.clear()

   # Enter the new email in the field
   new_email_field.send_keys(new_email)

   # Find and click on the save button
   save_button = driver.find_element(By.XPATH, NamesRef.save_email_button)
   save_button.click()
   sleep(3)

   # Now test if the email change was successful
   flag = NormalLogin.login(new_email, the_password)

   if flag == False:
      print("Change Email failed. Email didn't change.")
      driver.close()
   else:
      flag.close()
      print("Change Email Success. Email did change.")
      driver.close()
