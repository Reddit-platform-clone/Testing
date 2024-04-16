from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from faker import Faker
import random
import string
import NamesRef


def createEmail():
    """
    Function to generate a random email address.

    Returns:
        str: Randomly generated email address.
    """
    # Generate a random string of letters and digits for the username
    username = ''.join(random.choices(string.ascii_letters + string.digits, k=10))

    # Add a domain name
    email = username + '@yopmail.com'
    return email


def ceatePasword():
    """
    Function to generate a random strong password.

    Returns:
        str: Randomly generated strong password.
    """
    char_set = string.ascii_letters + string.digits + string.punctuation
    # Generate a random password of the specified length
    password = ''.join(random.choice(char_set) for i in range(12))
    return password


def createWeakPassword():
    """
    Function to generate a weak password (for testing purposes).

    Returns:
        str: Weak password.
    """
    char_set = string.digits
    # Generate a weak password (all digits)
    password = ''.join('a'*8)
    return password


def NormalSignUp():
    """
    Function to perform a normal sign-up process on Reddit.

    This function initializes the Chrome WebDriver, creates a random email and password, navigates to the sign-up
    page, fills in the email and password fields, solves the reCAPTCHA (manually), and submits the sign-up form.

    Returns:
        None
    """
    # Initialize the web driver
    driver = webdriver.Chrome()

    # Create an email and username
    email = createEmail()

    # Create a password
    password = ceatePasword()

    # Navigate to the sign-up page
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

    # Waiting time till the reCAPTCHA is solved
    sleep(15)

    # Press enter to proceed to the next part
    pass_field.send_keys(Keys.RETURN)

    sleep(15)
    driver.close()


def WeakPassSignUp():
    """
    Function to perform a sign-up process on Reddit with a weak password (for testing purposes).

    This function initializes the Chrome WebDriver, creates a random email and weak password, navigates to the sign-up
    page, fills in the email and password fields, solves the reCAPTCHA (manually), and submits the sign-up form.

    Returns:
        None
    """
    # Initialize the web driver
    driver = webdriver.Chrome()

    # Create an email and username
    email = createEmail()

    # Create a weak password
    password = createWeakPassword()

    # Navigate to the sign-up page
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

    # Waiting time till the reCAPTCHA is solved
    sleep(15)

    # Press enter to proceed to the next part
    pass_field.send_keys(Keys.RETURN)

    sleep(15)
    driver.close()

WeakPassSignUp()
