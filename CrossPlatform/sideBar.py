from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.common import AppiumOptions
import initialization
from time import sleep


driver = webdriver.Remote(initialization.url, options=AppiumOptions().load_capabilities(initialization.desired_caps))
driver.implicitly_wait(10)

def open_profile():
    """
  Opens the user profile and goes to edit profile section.
  Clicks on the element identified by 'profile_Xpath' to open the profile tab. Waits 2 seconds.
  Clicks on the element identified by 'my_profile_Xpath' to access the user profile. Waits 2 seconds.
  """
    driver.find_element(by=AppiumBy.XPATH, value=initialization.sideBar_Xpath).click()
    sleep(2)

    driver.find_element(by=AppiumBy.XPATH, value=initialization.my_profile_Xpath).click()
    sleep(2)

    driver.find_element(by=AppiumBy.XPATH, value=initialization.edit_profile_Xpath).click()
    sleep(2)

def saved():
    driver.find_element(by=AppiumBy.XPATH, value=initialization.sideBar_Xpath).click()
    sleep(2)

    driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Saved").click()
    sleep(5)

    driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value=initialization.savedComment_ID).click()
    sleep(2)

    driver.quit()


def history():
    driver.find_element(by=AppiumBy.XPATH, value=initialization.sideBar_Xpath).click()
    sleep(2)

    driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="History").click()
    sleep(5)
    driver.quit()


def social():
    driver.find_element(by=AppiumBy.XPATH, value=initialization.sideBar_Xpath).click()
    sleep(2)

    driver.find_element(by=AppiumBy.XPATH, value=initialization.my_profile_Xpath).click()
    sleep(2)

    driver.find_element(by=AppiumBy.XPATH, value=initialization.social_Xpath).click()
    sleep(2)

    driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Facebook").click()
    sleep(1)

    driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Add").click()
    sleep(2)
    driver.quit()

def settings():
    driver.find_element(by=AppiumBy.XPATH, value=initialization.sideBar_Xpath).click()
    sleep(2)

    driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Settings").click()
    sleep(2)

    driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Update email address").click()
    sleep(1)
    email = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.EditText")
    email.click()
    email.send_keys("youssefemad@hotmail.com")

    driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Continue").click()
    sleep(4)

    driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Change password").click()
    sleep(1)

    old = driver.find_element(by=AppiumBy.XPATH, value=initialization.oldpass_Xpath)
    old.click()
    sleep(1)
    old.send_keys("1234567890")
    sleep(1)

    new = driver.find_element(by=AppiumBy.XPATH, value=initialization.newpass_Xpath)
    new.click()
    sleep(1)
    new.send_keys("123456789")

    conf = driver.find_element(by=AppiumBy.XPATH, value=initialization.confpass_Xpath)
    conf.click()
    sleep(1)
    conf.send_keys("123456789")

    driver.find_element(by=AppiumBy.XPATH, value=initialization.changepass_Xpath).click()
    sleep(4)

    driver.find_element(by=AppiumBy.XPATH, value="//android.view.View[@content-desc='Gender']").click()
    driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Male").click()
    sleep(1)

    chat = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="""Chat and messaging permisions""")
    chat.click()
    sleep(1)
    driver.find_element(by=AppiumBy.XPATH, value=initialization.anyy_Xpath).click()
    sleep(1)
    driver.find_element(by=AppiumBy.XPATH, value=initialization.older_Xpath).click()
    sleep(1)
    driver.find_element(by=AppiumBy.XPATH, value=initialization.nobody_Xpath).click()
    sleep(1)
    driver.find_element(by=AppiumBy.XPATH, value=initialization.noomess_Xpath).click()
    sleep(1)
    driver.find_element(by=AppiumBy.XPATH, value=initialization.back_Xpath).click()
    sleep(1)


def logout():
    driver.find_element(by=AppiumBy.XPATH, value=initialization.profilee_Xpath).click()
    sleep(1)
    driver.find_element(by=AppiumBy.XPATH, value=initialization.logout_Xpath).click()
    sleep(3)

    driver.quit()

# Uncomment the function you want:

# saved()
# history()
# social()
# settings()
# logout()
