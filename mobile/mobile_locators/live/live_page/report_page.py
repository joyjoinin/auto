from utils.common_mobile import LocatorInfo

Report_page = LocatorInfo('accessibility id', 'Report a Problem')
email_answer = LocatorInfo(locator='//XCUIElementTypeTextField[@name="What is your email address?"]')
name_answer = LocatorInfo(locator='//XCUIElementTypeOther[@name="main"]/XCUIElementTypeOther[3]/XCUIElementTypeOther[1]/XCUIElementTypeTextView[1]')
report_option_list = LocatorInfo(locator='//XCUIElementTypeOther[@name="Question 3 This question is required."]/XCUIElementTypeOther[4]/XCUIElementTypeOther//XCUIElementTypeOther')
addition_answer = LocatorInfo(locator='//XCUIElementTypeOther[@name="main"]/XCUIElementTypeOther[3]/XCUIElementTypeOther[1]/XCUIElementTypeTextView[1]')
screenshot_select = LocatorInfo('accessibility id', 'choice 1')
confirm_button = LocatorInfo('accessibility id', 'OK')
submit_report = LocatorInfo('accessibility id', 'Submit')
next_question = LocatorInfo('accessibility id', 'Navigate to next question')
previous_question = LocatorInfo('accessibility id', 'Navigate to previous question')
thanks = LocatorInfo('accessibility id','Thank you for your submission. ')
report_title = LocatorInfo('accessibility id','Fanatics Gradient')