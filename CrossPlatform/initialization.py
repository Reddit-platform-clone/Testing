from typing import Any, Dict

# Appium driver initialization 

desired_caps: Dict[str, Any] = {
    "platformName": "Android",
    "appium:platformVersion": "13",
    "appium:deviceName": "emulator-5554",
    "appium:automationName": "UIAutomator2",
    "appium:app": "C:\\Users\\Emad\\Desktop\\Cross-Platform-main\\sarakel\\build\\app\\outputs\\apk\\debug\\app-debug.apk"
}

url = 'http://localhost:4723'

# Locators:

# 1- Sarakel locators:
value_Xpath_signup = "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.EditText[1]"
pass_Xpath_signup = "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.EditText[2]"
createC_Xpath = "//android.widget.EditText"
post_Xpath_title = "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText[1]"
post_Xpath_body = "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText[2]"
menu_Xpath_home = "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.Button[1]"
pass_Xpath_login = "//android.widget.ScrollView/android.widget.EditText[2]"
username_Xpath_signup = "//android.widget.EditText"

# 2- Reddit locators:
home_Xpath = "//android.widget.TextView[@content-desc='Home feed' and @resource-id='toolbar_feed_type_label']"
pop_Xpath = "(//android.view.View[@resource-id='toolbar_feed_type_item'])[2]"
watch_Xpath = "(//android.view.View[@resource-id='toolbar_feed_type_item'])[3]"
latest_Xpath = "(//android.view.View[@resource-id='toolbar_feed_type_item'])[4]"
join_Xpath = "//android.view.View[@resource-id='post_join_button']"
upvote_Xpath = "(//android.view.View[@resource-id='post_footer'])[2]/android.view.View[1]"
comment_Xpath = "(//android.view.View[@resource-id='post_comment_button'])[2]"
add_comment_Xpath = "//android.widget.Button[@resource-id='com.reddit.frontpage:id/reply_text_view']"
post_comment_Xpath = "//android.widget.Button[@resource-id='com.reddit.frontpage:id/menu_item_text']"
reply_Xpath = "//android.widget.TextView[@resource-id='com.reddit.frontpage:id/reply_to_comment']"
upvote_comment_Xpath = "(//android.widget.ImageView[@content-desc='Upvote'])[1]"
downvote_comment_Xpath = "(//android.widget.ImageView[@content-desc='Downvote'])[2]"
share_Xpath = "(//android.view.View[@resource-id='post_share_button'])[1]"
share_profile_Xpath = "(//android.view.View[@resource-id='share_action_button'])[3]"
share_post_Xpath = "//android.widget.ImageView[@resource-id='com.reddit.frontpage:id/inner_peeking_snoovatar']"
profile_Xpath = "//android.widget.ImageView[@resource-id='com.reddit.frontpage:id/inner_peeking_snoovatar']"
my_profile_Xpath = "//android.widget.TextView[@resource-id='com.reddit.frontpage:id/drawer_nav_item_title' and @text='My profile']"
edit_profile_Xpath = "//android.view.ViewGroup[@resource-id='com.reddit.frontpage:id/profile_pager_header']/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.widget.Button"
