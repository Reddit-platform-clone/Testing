from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
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
    return username, email

def createWeakEmail():
    """
    Function to generate a random email address.

    Returns:
        str: Randomly generated email address.
    """
    # Generate a random string of letters and digits for the username
    username = ''.join(random.choices(string.ascii_letters + string.digits, k=10))

    # Add a domain name
    email = username + '@a.c'
    return username, email

def createPasword():
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
    Function to perform a normal sign-up process on Sarakel.

    This function initializes the Chrome WebDriver, creates a random email and password, navigates to the sign-up
    page, fills in the email and password fields, solves the reCAPTCHA (manually), and submits the sign-up form.

    Returns:
        None
    """
    # Initialize the web driver
    driver = webdriver.Chrome()

    # Create an email and username
    username, email = createEmail()

    # Create a password
    password = createPasword()

    # Navigate to the sign-up page
    driver.get("http://www.sarakel.me/")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, NamesRef.login_button)))

    # Find and click on the login button
    login_button = driver.find_element(By.XPATH, NamesRef.login_button)
    login_button.click()

    #get sign up form
    signup_form = driver.find_element(By.XPATH, NamesRef.signup_form_href)
    signup_form.click()
    sleep(3)
    # Fill in the email field and submit
    input_field = driver.find_element(By.ID, NamesRef.signup_email_space)
    input_field.send_keys(email)
    signup_continue = driver.find_element(By.XPATH, NamesRef.signup_continue_button)
    signup_continue.click()
    sleep(5)

    username_field = driver.find_element(By.ID, NamesRef.signup_username_space)
    username_field.send_keys(username)

    # Fill in the password field
    pass_field = driver.find_element(By.ID, NamesRef.signup_password_space)
    pass_field.send_keys(password)


    # Click on continue  to proceed to the next part
    signup_continue2 = driver.find_element(By.XPATH, NamesRef.signup_continue_button2)
    signup_continue2.click()

    sleep(5)
    # Check if Signup was successful
    try:
       # Look for the error message
       error_message = driver.find_element(By.XPATH, "//div[contains(text(), 'Invalid username or password.')]")
       print("Normal Signup failed:", error_message.text)
       driver.quit()
       return False
    except NoSuchElementException:
       # No error message found, login successful
       print("Normal Signup successful!")
       driver.quit()
       return True

def WeakPassSignUp():
    """
    Function to perform a sign-up process on Sarakel with a weak password (for testing purposes).

    This function initializes the Chrome WebDriver, creates a random email and weak password, navigates to the sign-up
    page, fills in the email and password fields, solves the reCAPTCHA (manually), and submits the sign-up form.

    Returns:
        None
    """
    # Initialize the web driver
    driver = webdriver.Chrome()

    # Create an email and username
    username, email = createEmail()

    # Create a weak password
    password = createWeakPassword()

    # Navigate to the sign-up page
    driver.get("https://www.sarakel.me/")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, NamesRef.login_button)))

    # Find and click on the login button
    login_button = driver.find_element(By.XPATH, NamesRef.login_button)
    login_button.click()

    # get sign up form
    signup_form = driver.find_element(By.XPATH, NamesRef.signup_form_href)
    signup_form.click()
    sleep(3)
    # Fill in the email field and submit
    input_field = driver.find_element(By.ID, NamesRef.signup_email_space)
    input_field.send_keys(email)
    signup_continue = driver.find_element(By.XPATH, NamesRef.signup_continue_button)
    signup_continue.click()
    sleep(5)

    username_field = driver.find_element(By.ID, NamesRef.signup_username_space)
    username_field.send_keys(username)

    # Fill in the password field
    pass_field = driver.find_element(By.ID, NamesRef.signup_password_space)
    pass_field.send_keys(password)

    # Click on continue  to proceed to the next part
    signup_continue2 = driver.find_element(By.XPATH, NamesRef.signup_continue_button2)
    signup_continue2.click()

    sleep(4)
    # Check if Signup was successful
    try:
        # Look for the error message
        error_message = driver.find_element(By.XPATH, "//div[contains(text(), 'An error occurred while signing up')]")
        print("Weak Password Signup Test Pass:", error_message.text)
        driver.quit()
        return True
    except NoSuchElementException:
        # No error message found, signup successful
        print("Weak Password Signup Test Failed!")
        driver.quit()
        return False

def WeakEmailSignUp():
    """
    Function to perform a sign-up process on Sarakel with a weak email (for testing purposes).

    This function initializes the Chrome WebDriver, creates a weak email and strong password, navigates to the sign-up
    page, fills in the email and password fields, solves the reCAPTCHA (manually), and submits the sign-up form.

    Returns:
        None
    """
    # Initialize the web driver
    driver = webdriver.Chrome()

    # Create a weak email and username
    username, email = createWeakEmail()

    # Create a strong password
    password = createPasword()

    # Navigate to the sign-up page
    driver.get("https://www.sarakel.me/")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, NamesRef.login_button)))

    # Find and click on the login button
    login_button = driver.find_element(By.XPATH, NamesRef.login_button)
    login_button.click()

    # get sign up form
    signup_form = driver.find_element(By.XPATH, NamesRef.signup_form_href)
    signup_form.click()
    sleep(3)
    # Fill in the email field and submit
    input_field = driver.find_element(By.ID, NamesRef.signup_email_space)
    input_field.send_keys(email)
    signup_continue = driver.find_element(By.XPATH, NamesRef.signup_continue_button)
    signup_continue.click()
    sleep(5)

    username_field = driver.find_element(By.ID, NamesRef.signup_username_space)
    username_field.send_keys(username)

    # Fill in the password field
    pass_field = driver.find_element(By.ID, NamesRef.signup_password_space)
    pass_field.send_keys(password)

    # Click on continue  to proceed to the next part
    signup_continue2 = driver.find_element(By.XPATH, NamesRef.signup_continue_button2)
    signup_continue2.click()

    sleep(4)
    # Check if Signup was successful
    try:
        # Look for the error message
        error_message = driver.find_element(By.XPATH, "//div[contains(text(), 'An error occurred while signing up')]")
        print("Weak Email Signup Test Pass:", error_message.text)
        driver.quit()
        return True
    except NoSuchElementException:
        # No error message found, signup successful
        print("Weak Email Signup Test Failed!")
        driver.quit()
        return False

def PreviousUsedEmailSignUp():
    """
    Function to perform a sign-up process on Sarakel with a previously used email (for testing purposes).

    This function initializes the Chrome WebDriver, uses a previously used email and strong password, navigates to the sign-up
    page, fills in the email and password fields, solves the reCAPTCHA (manually), and submits the sign-up form.

    Returns:
        None
    """
    # Initialize the web driver
    driver = webdriver.Chrome()

    # Create an email and username
    username, _ = createEmail()

    # Use a previously used email
    email = NamesRef.login_email

    # Create a strong password
    password = createPasword()

    # Navigate to the sign-up page
    driver.get("https://www.sarakel.me/")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, NamesRef.login_button)))

    # Find and click on the login button
    login_button = driver.find_element(By.XPATH, NamesRef.login_button)
    login_button.click()

    # get sign up form
    signup_form = driver.find_element(By.XPATH, NamesRef.signup_form_href)
    signup_form.click()
    sleep(3)
    # Fill in the email field and submit
    input_field = driver.find_element(By.ID, NamesRef.signup_email_space)
    input_field.send_keys(email)
    signup_continue = driver.find_element(By.XPATH, NamesRef.signup_continue_button)
    signup_continue.click()
    sleep(5)

    username_field = driver.find_element(By.ID, NamesRef.signup_username_space)
    username_field.send_keys(username)

    # Fill in the password field
    pass_field = driver.find_element(By.ID, NamesRef.signup_password_space)
    pass_field.send_keys(password)

    # Click on continue  to proceed to the next part
    signup_continue2 = driver.find_element(By.XPATH, NamesRef.signup_continue_button2)
    signup_continue2.click()

    sleep(3)
    # Check if Signup was successful
    try:
        # Look for the error message
        error_message = driver.find_element(By.XPATH,
                                            "//div[contains(text(), 'Email is not available.')]")
        print("Prev used Email Signup test Pass:", error_message.text)
        driver.quit()
        return True
    except NoSuchElementException:
        # No error message found, login successful
        print("Prev used Email Signup test Fail!")
        driver.quit()
        return False

def PreviousUsedUsernameSignUp():
    """
    Function to perform a sign-up process on Sarakel with a previously used username (for testing purposes).

    This function initializes the Chrome WebDriver, creates a random email and strong password, navigates to the sign-up
    page, uses a previously used username, fills in the email and password fields, solves the reCAPTCHA (manually),
    and submits the sign-up form.

    Returns:
        None
    """
    # Initialize the web driver
    driver = webdriver.Chrome()

    # Create a random email and use a previously used username
    username = NamesRef.login_username
    _, email = createEmail()

    # Create a strong password
    password = createPasword()

    # Navigate to the sign-up page
    driver.get("https://www.sarakel.me/")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, NamesRef.login_button)))

    # Find and click on the login button
    login_button = driver.find_element(By.XPATH, NamesRef.login_button)
    login_button.click()

    # get sign up form
    signup_form = driver.find_element(By.XPATH, NamesRef.signup_form_href)
    signup_form.click()
    sleep(3)
    # Fill in the email field and submit
    input_field = driver.find_element(By.ID, NamesRef.signup_email_space)
    input_field.send_keys(email)
    signup_continue = driver.find_element(By.XPATH, NamesRef.signup_continue_button)
    signup_continue.click()
    sleep(5)

    username_field = driver.find_element(By.ID, NamesRef.signup_username_space)
    username_field.send_keys(username)

    # Fill in the password field
    pass_field = driver.find_element(By.ID, NamesRef.signup_password_space)
    pass_field.send_keys(password)

    # Click on continue  to proceed to the next part
    signup_continue2 = driver.find_element(By.XPATH, NamesRef.signup_continue_button2)
    signup_continue2.click()

    sleep(3)
    # Check if Signup was successful
    try:
        # Look for the error message
        error_message = driver.find_element(By.XPATH,
                                            "//div[contains(text(), 'Username is not available.')]")
        print("Prev used username Signup test Pass:", error_message.text)
        driver.quit()
        return True
    except NoSuchElementException:
        # No error message found, login successful
        print("Prev used username Signup test Fail!")
        driver.quit()
        return False

def EmptyUsernameSignUp():
    """
    Function to perform a sign-up process on Sarakel with an empty username (for testing purposes).

    This function initializes the Chrome WebDriver, creates a random email and strong password, navigates to the sign-up
    page, leaves the username field empty, fills in the email and password fields, solves the reCAPTCHA (manually),
    and submits the sign-up form.

    Returns:
        None
    """
    # Initialize the web driver
    driver = webdriver.Chrome()

    # Create a random email and username
    username = ""
    _, email = createEmail()

    # Create a strong password
    password = createPasword()

    # Navigate to the sign-up page
    driver.get("https://www.sarakel.me/")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, NamesRef.login_button)))

    # Find and click on the login button
    login_button = driver.find_element(By.XPATH, NamesRef.login_button)
    login_button.click()

    # get sign up form
    signup_form = driver.find_element(By.XPATH, NamesRef.signup_form_href)
    signup_form.click()
    sleep(3)
    # Fill in the email field and submit
    input_field = driver.find_element(By.ID, NamesRef.signup_email_space)
    input_field.send_keys(email)
    signup_continue = driver.find_element(By.XPATH, NamesRef.signup_continue_button)
    signup_continue.click()
    sleep(5)

    # Leave username field empty
    username_field = driver.find_element(By.ID, NamesRef.signup_username_space)
    username_field.send_keys(username)

    # Fill in the password field
    pass_field = driver.find_element(By.ID, NamesRef.signup_password_space)
    pass_field.send_keys(password)

    # Click on continue  to proceed to the next part
    signup_continue2 = driver.find_element(By.XPATH, NamesRef.signup_continue_button2)
    signup_continue2.click()

    sleep(3)
    # Check if Signup was successful
    try:
        # Look for the error message
        error_message = driver.find_element(By.XPATH,
                                            "//div[contains(text(), 'Username and password cannot be empty.')]")
        print("Empty username Signup test Pass:", error_message.text)
        driver.quit()
        return True
    except NoSuchElementException:
        # No error message found, login successful
        print("Empty username Signup test Fail!")
        driver.quit()
        return False

def EmptyPasswordSignUp():
    """
    Function to perform a sign-up process on Sarakel with an empty password (for testing purposes).

    This function initializes the Chrome WebDriver, creates a random email and username, navigates to the sign-up
    page, fills in the email and username fields, leaves the password field empty, solves the reCAPTCHA (manually),
    and submits the sign-up form.

    Returns:
        None
    """
    # Initialize the web driver
    driver = webdriver.Chrome()

    # Create a random email and username
    username, email = createEmail()

    # Create an empty password
    password = ""

    # Navigate to the sign-up page
    driver.get("https://www.sarakel.me/")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, NamesRef.login_button)))

    # Find and click on the login button
    login_button = driver.find_element(By.XPATH, NamesRef.login_button)
    login_button.click()

    # get sign up form
    signup_form = driver.find_element(By.XPATH, NamesRef.signup_form_href)
    signup_form.click()
    sleep(3)
    # Fill in the email field and submit
    input_field = driver.find_element(By.ID, NamesRef.signup_email_space)
    input_field.send_keys(email)
    signup_continue = driver.find_element(By.XPATH, NamesRef.signup_continue_button)
    signup_continue.click()
    sleep(5)

    username_field = driver.find_element(By.ID, NamesRef.signup_username_space)
    username_field.send_keys(username)

    # Leave password field empty
    pass_field = driver.find_element(By.ID, NamesRef.signup_password_space)
    pass_field.send_keys(password)

    # Click on continue  to proceed to the next part
    signup_continue2 = driver.find_element(By.XPATH, NamesRef.signup_continue_button2)
    signup_continue2.click()

    sleep(3)
    # Check if Signup was successful
    try:
        # Look for the error message
        error_message = driver.find_element(By.XPATH,
                                            "//div[contains(text(), 'Username and password cannot be empty.')]")
        print("Empty Password Signup test Pass:", error_message.text)
        driver.quit()
        return True
    except NoSuchElementException:
        # No error message found, login successful
        print("Empty Password Signup test Fail!")
        driver.quit()
        return False
