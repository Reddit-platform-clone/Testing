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
home_Xpath = "//android.widget.Button[@content-desc='Home']"
pop_Xpath = "//android.view.View[@content-desc='Popular']"
join_Xpath = "//android.widget.Button[@content-desc='Join']"
profile_Xpath = "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.Button[4]"
my_profile_Xpath = "//android.view.View[@content-desc='My Profile']"
edit_profile_Xpath = "//android.widget.Button[@content-desc='Edit']"
chat_Xpath = "//android.view.View[@content-desc='habiba']"
message_Xpath = "//android.widget.EditText"
send_Xpath = "//android.widget.EditText/android.widget.Button"
join_post_Xpath = "(//android.widget.Button[@content-desc='Join'])[1]"
upvote_post_Xpath = """"//android.widget.ImageView[@content-desc="2 
1890
1
56
56"]/android.widget.Button[3]"""
join_post_Xpath = "(//android.widget.Button[@content-desc='Join'])[1]"
dwonvote_post_Xpath = """//android.widget.ImageView[@content-desc="2 
1890
1
56
56"]/android.widget.Button[4]"""
compose_mess_Xpath = "//android.widget.Button[@content-desc='Compose Message']"
send_to_Xpath = "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText[1]"
title_Xpath = "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText[2]"
body_Xpath = "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText[3]"
sendmess_Xpath = "//android.widget.Button[@content-desc='Send']"


# 2- Reddit locators:
watch_Xpath = "(//android.view.View[@resource-id='toolbar_feed_type_item'])[3]"
latest_Xpath = "(//android.view.View[@resource-id='toolbar_feed_type_item'])[4]"
comment_Xpath = "(//android.view.View[@resource-id='post_comment_button'])[2]"
add_comment_Xpath = "//android.widget.Button[@resource-id='com.reddit.frontpage:id/reply_text_view']"
post_comment_Xpath = "//android.widget.Button[@resource-id='com.reddit.frontpage:id/menu_item_text']"
reply_Xpath = "//android.widget.TextView[@resource-id='com.reddit.frontpage:id/reply_to_comment']"
upvote_comment_Xpath = "(//android.widget.ImageView[@content-desc='Upvote'])[1]"
downvote_comment_Xpath = "(//android.widget.ImageView[@content-desc='Downvote'])[2]"
share_Xpath = "(//android.view.View[@resource-id='post_share_button'])[1]"
share_profile_Xpath = "(//android.view.View[@resource-id='share_action_button'])[3]"
share_post_Xpath = "//android.widget.ImageView[@resource-id='com.reddit.frontpage:id/inner_peeking_snoovatar']"
name_Xpath = "//android.widget.TextView[@text='Display name – optional']"
about_Xpath = "//android.widget.EditText[@resource-id='about_field']"
social_link_Xpath = "//android.widget.Button[@content-desc='Add social link']"
choose_link_Xpath = "//android.widget.TextView[@text='Reddit']"  # choose which name you want to add the link for
com_or_usnm_Xpath = "//android.widget.FrameLayout[@resource-id='com.reddit.frontpage:id/screen_modal_container']/android.view.ViewGroup/android.view.View/android.widget.EditText/android.view.View"
visibility_Xpath = "//android.view.View[@resource-id='content_visibility']/android.view.View"
active_comm_Xpath = "//android.view.View[@resource-id='show_active_communities']/android.view.View"
