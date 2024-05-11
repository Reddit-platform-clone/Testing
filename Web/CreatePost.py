from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from time import sleep
import NamesRef
import NormalLogin

def CreatePost():
    """
    Function to create a new post on Sarakel.

    This function logs in using predefined credentials, navigates to the page for creating a new post, fills in the
    title and body fields, selects a community, and submits the post.

    Returns:
        None
    """
    driver = NormalLogin.login(NamesRef.login_username, NamesRef.login_password)

    # Wait until the create button appears and click on it
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, NamesRef.Create_Button)))
    create_button = driver.find_element(By.XPATH, NamesRef.Create_Button)
    create_button.click()

    # Fill in the title field
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, NamesRef.Title_field)))
    title_field = driver.find_element(By.XPATH, NamesRef.Title_field)
    title_field.send_keys("Testing Title")

    # Fill in the post body field
    post_body = driver.find_element(By.XPATH, NamesRef.Post_Body_field)
    post_body.send_keys("Testing the body field ")

    # Select a community from the dropdown list
    dropdown_list = driver.find_element(By.XPATH, NamesRef.community_DDL)
    select = Select(dropdown_list)
    select.select_by_index(1)

    # Click on the submit button
    Submit_Button = driver.find_element(By.XPATH, NamesRef.Post_Submit_Button)
    Submit_Button.click()

    sleep(8)
    driver.quit()

def CreatePostImage():
    """
    Function to create a new image post on Sarakel.

    This function logs in using predefined credentials, navigates to the page for creating a new post, fills in the
    title, selects an image, selects a community, and submits the post.

    Returns:
        None
    """
    driver = NormalLogin.login(NamesRef.login_username, NamesRef.login_password)

    # Wait until the create button appears and click on it
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, NamesRef.Create_Button)))
    create_button = driver.find_element(By.XPATH, NamesRef.Create_Button)
    create_button.click()

    # Click on the image section
    image_section = driver.find_element(By.XPATH, NamesRef.image_section)
    image_section.click()

    # Fill in the title field
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, NamesRef.Title_field)))
    title_field = driver.find_element(By.XPATH, NamesRef.Title_field)
    title_field.send_keys("Testing Title in Image Section")

    # Provide the file path to the image file
    image_path = "Put_your_Path"
    file_input = driver.find_element(By.XPATH, NamesRef.image_btn)
    file_input.send_keys(image_path)

    # Select a community from the dropdown list
    dropdown_list = driver.find_element(By.XPATH, NamesRef.community_DDL)
    select = Select(dropdown_list)
    select.select_by_index(1)

    # Click on the submit button
    Submit_Button = driver.find_element(By.XPATH, NamesRef.Post_Submit_Button)
    Submit_Button.click()

    sleep(8)
    driver.quit()

def CreatePostLink():
    """
    Function to create a new link post on Sarakel.

    This function logs in using predefined credentials, navigates to the page for creating a new post, fills in the
    title, enters a link, selects a community, and submits the post.

    Returns:
        None
    """
    driver = NormalLogin.login(NamesRef.login_username, NamesRef.login_password)

    # Wait until the create button appears and click on it
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, NamesRef.Create_Button)))
    create_button = driver.find_element(By.XPATH, NamesRef.Create_Button)
    create_button.click()

    # Click on the link section
    link_section = driver.find_element(By.XPATH, NamesRef.link_section)
    link_section.click()

    # Fill in the title field
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, NamesRef.Title_field)))
    title_field = driver.find_element(By.XPATH, NamesRef.Title_field)
    title_field.send_keys("Testing Title in Link Section")

    # Enter the link URL
    link_area = driver.find_element(By.XPATH, NamesRef.link_post_area)
    link_area.send_keys("https://www.sarakel.me/")

    # Select a community from the dropdown list
    dropdown_list = driver.find_element(By.XPATH, NamesRef.community_DDL)
    select = Select(dropdown_list)
    select.select_by_index(1)

    # Click on the submit button
    Submit_Button = driver.find_element(By.XPATH, NamesRef.Post_Submit_Button)
    Submit_Button.click()

    sleep(2)
    driver.quit()

def CreatePostPoll():
    """
    Function to create a new poll post on Sarakel.

    This function logs in using predefined credentials, navigates to the page for creating a new post, fills in the
    title, adds poll options, selects a community, and submits the post.

    Returns:
        None
    """
    driver = NormalLogin.login(NamesRef.login_username, NamesRef.login_password)

    # Wait until the create button appears and click on it
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, NamesRef.Create_Button)))
    create_button = driver.find_element(By.XPATH, NamesRef.Create_Button)
    create_button.click()

    # Click on the poll section
    link_section = driver.find_element(By.XPATH, NamesRef.poll_section)
    link_section.click()

    # Fill in the title field
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, NamesRef.Title_field)))
    title_field = driver.find_element(By.XPATH, NamesRef.Title_field)
    title_field.send_keys("Testing Title in Poll Section")

    # Fill in the poll body
    poll_body = driver.find_element(By.XPATH, NamesRef.poll_body)
    poll_body.send_keys("Testing poll body")

    # Fill in poll options
    option_1 = driver.find_element(By.XPATH, NamesRef.poll_op1)
    option_1.send_keys("Option1 test")

    option_2 = driver.find_element(By.XPATH, NamesRef.poll_op2)
    option_2.send_keys("Option2 test")

    # Select a community from the dropdown list
    dropdown_list = driver.find_element(By.XPATH, NamesRef.community_DDL)
    select = Select(dropdown_list)
    select.select_by_index(1)

    # Select the vote length
    vote_len_list = driver.find_element(By.XPATH, NamesRef.poll_vote_len)
    select_2 = Select(vote_len_list)
    select_2.select_by_index(1)

    # Click on the submit button
    Submit_Button = driver.find_element(By.XPATH, NamesRef.Post_Submit_Button)
    Submit_Button.click()

    sleep(2)
    driver.quit()

CreatePostPoll()
