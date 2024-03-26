from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from faker import Faker
import random
import string
import NamesRef


def createEmail():
    # Generate a random string of letters and digits for the username
    username = ''.join(random.choices(string.ascii_letters + string.digits, k=10))

    # Add a domain name
    email = username + '@yopmail.com'
    return email

def ceatePasword():
    char_set = string.ascii_letters + string.digits + string.punctuation
    # Generate a random password of the specified length
    password = ''.join(random.choice(char_set) for i in range(12))
    return password

def createWeakPassword():
    char_set = string.digits
    # Generate a random password of the specified length
    password = ''.join('a'*8)
    return password

mainURL="https://www.reddit.com/"

def NormalSignUp():
    # Initialize the web driver
    driver = webdriver.Chrome()

    # Create an email and username
    email= createEmail()

    # Create a password
    password = ceatePasword()

    # Navigate to the sign up page
    driver.get("https://www.reddit.com/register/")
    sleep(5)

    # Fill in the email field and submit
    input_field = driver.find_element(By.ID, NamesRef.sigupEmailSpace)
    input_field.send_keys(email)
    input_field.send_keys(Keys.RETURN)
    sleep(5)

    # Fill in the password field
    pass_field = driver.find_element(By.ID, NamesRef.signupPasswordSpace)
    pass_field.send_keys(password)

    #waiting time till I solve the reCAPTCHA
    sleep(15)

    #press enter to proceed to next part
    pass_field.send_keys(Keys.RETURN)

    sleep(15)
    driver.close()


def WeakPassSignUp():
    # Initialize the web driver
    driver = webdriver.Chrome()

    # Create an email and username
    email = createEmail()

    # Create a weak password
    password = createWeakPassword()

    # Navigate to the sign up page
    driver.get("https://www.reddit.com/register/")
    sleep(5)

    # Fill in the email field and submit
    input_field = driver.find_element(By.ID, NamesRef.sigupEmailSpace)
    input_field.send_keys(email)
    input_field.send_keys(Keys.RETURN)
    sleep(5)

    # Fill in the password field
    pass_field = driver.find_element(By.ID, NamesRef.signupPasswordSpace)
    pass_field.send_keys(password)

    # waiting time till I solve the reCAPTCHA
    sleep(15)

    # press enter to proceed to next part
    pass_field.send_keys(Keys.RETURN)

    sleep(15)
    driver.close()

    