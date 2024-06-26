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

# Sarakel locators:
value_Xpath_signup = "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.EditText[1]"
pass_Xpath_signup = "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.EditText[2]"
createC_Xpath = "//android.widget.EditText"
post_Xpath_title = "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText[1]"
post_Xpath_body = "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText[2]"
menu_Xpath_home = "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.Button[1]"
pass_Xpath_login = "//android.widget.ScrollView/android.widget.EditText[2]"
username_Xpath_signup = "//android.widget.EditText"
home_Xpath = "(//android.widget.Button[@content-desc='Home']"
pop_Xpath = "//android.widget.Button[@content-desc='Popular']"
hot_Xpath = "//android.widget.Button[@content-desc='Hot']"
random_Xpath = "//android.widget.Button[@content-desc='Random']"
chat_Xpath = "//android.widget.ImageView[@content-desc='bahey']"
message_Xpath = "//android.widget.EditText"
send_Xpath = "//android.widget.EditText/android.widget.Button"
join_Xpath = "//android.widget.Button[@content-desc='Join']"
sideBar_Xpath = "//android.widget.ImageView"
my_profile_Xpath = "//android.view.View[@content-desc='Profile']"
edit_profile_Xpath = "//android.widget.Button[@content-desc='Edit']"
join_post_Xpath = "(//android.widget.Button[@content-desc='Join'])[1]"
add_comment_Xpath = "//android.widget.EditText"
post_comment_Xpath = "//android.widget.EditText/android.widget.Button"
reply_Xpath = "//android.widget.TextView[@resource-id='com.reddit.frontpage:id/reply_to_comment']"
upvote_post_Xpath = """//android.view.View[@content-desc=" c/Liverpool
• 33m
spoiler alert
test flair
0
0
0"]/android.widget.Button[3]"""
downvote_post_Xpath = """//android.view.View[@content-desc=" c/Liverpool
• 33m
spoiler alert
test flair
0
0
0"]/android.widget.Button[4]"""
compose_mess_Xpath = "//android.widget.Button[@content-desc='New Message']"
send_to_Xpath = "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText[1]"
title_Xpath = "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText[2]"
body_Xpath = "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText[3]"
sendmess_Xpath = "//android.widget.Button[@content-desc='Send']"
set_post = """//android.view.View[@content-desc=" c/Liverpool
• 33m
spoiler alert
test flair
0
0
0"]/android.widget.Button[2]"""
share_Xpath = """//android.view.View[@content-desc=" c/Liverpool
• 33m
spoiler alert
test flair
0
0
0"]/android.widget.Button[6]"""
sideBar_Xpath = "//android.widget.ImageView"
savedComment_ID = """Comments
Tab 2 of 2"""
my_profile_Xpath = "//android.view.View[@content-desc='Profile']"
social_Xpath = "//android.widget.Button[@content-desc='Add social link']"
upvote_comment_Xpath = "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View[8]/android.view.View/android.view.View/android.widget.EditText/android.widget.Button[4]"
downvote_comment_Xpath = "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View[8]/android.view.View/android.view.View/android.widget.EditText/android.widget.Button[5]"
settings_comment_Xpath = "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View[8]/android.view.View/android.view.View/android.widget.EditText/android.widget.Button[2]"
oldpass_Xpath = "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText[1]"
newpass_Xpath = "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText[2]"
confpass_Xpath = "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText[3]"
changepass_Xpath = "//android.widget.Button[@content-desc='Change Password']"
anyy_Xpath = "(//android.view.View[@content-desc='Anyone on Sarakel'])[1]/android.widget.CheckBox"
older_Xpath = "//android.view.View[@content-desc='Acount older than 30 days']/android.widget.CheckBox"
nobody_Xpath = "(//android.view.View[@content-desc='Nobody'])[1]/android.widget.CheckBox"
noomess_Xpath = "(//android.view.View[@content-desc='Nobody'])[2]/android.widget.CheckBox"
back_Xpath = "//android.widget.Button[@content-desc='Back']"
profilee_Xpath = "//android.view.View[@content-desc='u/hafez']"
logout_Xpath = "//android.view.View[@content-desc='u/hafez']/android.widget.Button"
