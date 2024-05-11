from selenium.webdriver.common.by import By
from time import sleep
import NamesRef
import NormalLogin


def NavigateCommunity():
    """
    Function to navigate through a community page.

    This function logs in using predefined credentials, navigates to a community, joins it, filters posts,
    changes view type, selects a post, and opens it.

    Args:
        None

    Returns:
        None
    """
    # Login using predefined credentials
    driver = NormalLogin.login(NamesRef.login_username, NamesRef.login_password)
    sleep(5)

    # Click on the first community to navigate
    nav_comm = driver.find_element(By.XPATH, NamesRef.community_select_1st)
    nav_comm.click()
    sleep(5)

    # Join the community
    join_comm = driver.find_element(By.XPATH, NamesRef.join_btn_on_community)
    join_comm.click()
    sleep(3)

    # Filter posts
    posts_filter = driver.find_element(By.XPATH, NamesRef.posts_filter)
    posts_filter.click()
    sleep(2)

    # Click on the dropdown to select filter options
    dropdown_list = driver.find_element(By.XPATH, NamesRef.posts_filter_DDL_on_community)
    dropdown_list.click()
    sleep(5)

    # Click on the dropdown to change view type
    dropdown_list2 = driver.find_element(By.XPATH, NamesRef.posts_view_type_on_community)
    dropdown_list2.click()
    sleep(2)

    # Select the desired view type
    select_view = driver.find_element(By.XPATH, NamesRef.select_post_view_btn)
    select_view.click()
    sleep(5)

    # Re-open dropdown to switch view type
    dropdown_list2.click()
    sleep(2)

    # Select another view type
    select_view1 = driver.find_element(By.XPATH, NamesRef.select_post_view1_btn)
    select_view1.click()
    sleep(5)

    # Open the first post in the community
    open_post = driver.find_element(By.XPATH, NamesRef.open_1st_post_on_community)
    open_post.click()
    sleep(5)

    driver.quit()
