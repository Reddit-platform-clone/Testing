from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from time import sleep
import NormalLogin
import NamesRef

def NavigateHome():
    """
    Navigate through the home page.

    This function logs in, scrolls through the page, applies filters, and navigates through posts.

    Args:
        None

    Returns:
        None
    """
    # Login using predefined credentials
    driver = NormalLogin.login(NamesRef.login_username, NamesRef.login_password)
    sleep(5)

    # Scroll down, click notification button, and go back
    Scroll(driver)
    filters(driver)
    NavigatePost(driver)

    notification_btn = driver.find_element(By.XPATH, NamesRef.notification_btn)
    notification_btn.click()
    sleep(5)

    driver.back()
    sleep(3)

    driver.quit()

def Scroll(driver):
    """
    Scroll through the page.

    This function scrolls down the page, clicks on elements, and waits for a few seconds.

    Args:
        driver: Selenium WebDriver instance.

    Returns:
        None
    """
    # Get the current height of the page
    current_height = driver.execute_script("return document.body.scrollHeight;")
    # Scroll down using JavaScript
    driver.execute_script(f"window.scrollTo(0, {current_height * 2});")
    sleep(5)

    # Click on 'back to top' button
    back_to_top = driver.find_element(By.XPATH, NamesRef.back_to_top)
    back_to_top.click()
    sleep(2)

    # Scroll down again
    driver.execute_script(f"window.scrollTo(0, {current_height * 2});")
    sleep(2)

    # Click on 'more posts' button
    more_posts = driver.find_element(By.XPATH, NamesRef.more_posts)
    more_posts.click()
    sleep(10)
    # Scroll down one more time
    driver.execute_script(f"window.scrollTo(0, {current_height * 2});")
    sleep(10)
    return

def NavigatePost(driver):
    """
    Navigate through posts.

    This function interacts with various elements within a post, clicks on them, and prints success/failure messages.

    Args:
        driver: Selenium WebDriver instance.

    Returns:
        None
    """
    # Click on 'upvote' button
    upvote = driver.find_element(By.XPATH, NamesRef.upvote_out)
    upvote.click()
    sleep(2)

    # Click on 'downvote' button
    downvote = driver.find_element(By.XPATH, NamesRef.downvote_out)
    downvote.click()
    sleep(2)

    # Click on 'share' button
    share = driver.find_element(By.XPATH, NamesRef.downvote_out)
    share.click()
    sleep(3)

    # Check if sharing was successful
    try:
        error_message = driver.find_element(By.XPATH, "//div[contains(text(), 'Link copied')]")
        print("share post Success", error_message.text)
    except NoSuchElementException:
        print("share post Failed!")

    # Hover over 'options' button
    options_btn = driver.find_element(By.XPATH, NamesRef.options_of_post)
    actions = ActionChains(driver)
    actions.move_to_element(options_btn).perform()

    # Click on 'show few' option
    show_few = driver.find_element(By.XPATH, NamesRef.show_few_out_ddl)
    show_few.click()
    sleep(3)

    # Go back to previous page
    driver.back()
    sleep(3)

    # Hover over 'options' button again
    actions.move_to_element(options_btn).perform()

    # Click on 'save' option
    save = driver.find_element(By.XPATH, NamesRef.save_post_out_ddl)
    save.click()
    sleep(3)
    try:
        error_message = driver.find_element(By.XPATH, "//div[contains(text(), 'Post Saved')]")
        print("Save post Success", error_message.text)
    except NoSuchElementException:
        print("Save post Failed!")

    # Hover over 'options' button again
    actions.move_to_element(options_btn).perform()

    # Click on 'hide post' option
    hide_post = driver.find_element(By.XPATH, NamesRef.hide_post_out_ddl)
    hide_post.click()
    sleep(3)

    # Click on 'undo hide' option
    undo_hide = driver.find_element(By.XPATH, NamesRef.undo_hide_out)
    undo_hide.click()
    sleep(5)

    # Click on 'comment' section
    comment_section = driver.find_element(By.XPATH, NamesRef.comment_out)
    comment_section.click()
    sleep(5)

    # Input a comment
    comment_field_input = driver.find_element(By.XPATH, NamesRef.comment_in_post_field)
    comment_field_input.send_keys("Testing comment on post")

    # Click on 'submit' button
    comment_submit = driver.find_element(By.XPATH, NamesRef.send_comment_btn_in)
    comment_submit.click()

    sleep(5)

    # Go back to previous page
    driver.back()
    sleep(2)

def filters(driver):
    """
    Apply filters on the page.

    This function applies filters such as post filters and view type filters.

    Args:
        driver: Selenium WebDriver instance.

    Returns:
        None
    """
    # Click on 'posts filter'
    posts_filter = driver.find_element(By.XPATH, NamesRef.posts_filter_home)
    posts_filter.click()
    sleep(2)

    # Click on 'dropdown list' for filters
    dropdown_list = driver.find_element(By.XPATH, NamesRef.posts_filter_DDL_on_home)
    dropdown_list.click()
    sleep(5)

    # Click on 'dropdown list' for view type
    dropdown_list2 = driver.find_element(By.XPATH, NamesRef.posts_view_type_on_home)
    dropdown_list2.click()
    sleep(2)

    # Select a view type
    select_view = driver.find_element(By.XPATH, NamesRef.select_post_view_btn_home)
    select_view.click()
    sleep(5)

    # Click on 'dropdown list' for view type again
    dropdown_list2.click()
    sleep(2)

    # Select another view type
    select_view1 = driver.find_element(By.XPATH, NamesRef.select_post_view1_btn_home)
    select_view1.click()
    sleep(5)
    return
