from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
import NamesRef
import NormalLogin

def ChangePassword(the_email, old_password, new_password):
   """
   Function to change the password of a Sarakel account.

   This function logs in using the provided credentials, navigates to the settings,
   accesses the change password section, fills in the old and new password fields, and saves the changes.

   Args:
       the_email (str): The email of the Sarakel account.
       old_password (str): The old password of the Sarakel account.
       new_password (str): The new password to set for the Sarakel account.

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

   # Find and click on the settings button
   setting_button = driver.find_element(By.XPATH, NamesRef.setting_button)
   setting_button.click()

   # Wait until the change password button appears, then click on it
   WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, NamesRef.change_pass_button)))
   change_pass_button = driver.find_element(By.XPATH, NamesRef.change_pass_button)
   change_pass_button.click()
   sleep(10)

   # Find the field for entering the new password
   new_password_field = driver.find_element(By.XPATH, NamesRef.new_password_field)

   # Clear the new password field before entering the new password
   new_password_field.clear()

   # Enter the new password in the field
   new_password_field.send_keys(new_password)

   # Find and click on the save button
   save_button = driver.find_element(By.XPATH, NamesRef.save_password_button)
   save_button.click()
   sleep(3)

   # Now test if the password change was successful
   flag = NormalLogin.login(the_email, new_password)

   if flag == False:
      print("Change password failed. Password didn't change.")
      driver.close()
   else:
      print("Change password success. Password has been changed.")
      flag.close()
      driver.close()
