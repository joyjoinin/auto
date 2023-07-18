class LocatorInfo:
    def __init__(self, by_type=None, locator=None):
        self.type = by_type
        self.locator = locator


''' App Home '''
login = LocatorInfo('accessibility id', 'Log in')
join = LocatorInfo('accessibility id', 'Join')

''' Log in page'''
email = LocatorInfo('class name', 'XCUIElementTypeTextField')
login_next = LocatorInfo('accessibility id', 'Next')
password = LocatorInfo('class name', 'XCUIElementTypeSecureTextField')
password_after_input = LocatorInfo(locator='//XCUIElementTypeApplication[@name="Fanatics Live Development"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTextField[2]')
failed_login_message = LocatorInfo('accessibility id', 'Invalid email or password')
check_your_email = LocatorInfo('accessibility id', 'Check your email')
fanaticsID = LocatorInfo('accessibility id', 'Log in with Fanatics ID')
not_you = LocatorInfo('accessibility id', 'NOT YOU?')
show_password = LocatorInfo('accessibility id', 'SHOW')
hide_password = LocatorInfo('accessibility id', 'HIDE')
forget_password = LocatorInfo('accessibility id', 'Forgot password?')
terms_of_use = LocatorInfo('accessibility id', 'By tapping log in, you agree to our Terms of Use and acknowledge our Privacy Policy')
create_one_now = LocatorInfo('accessibility id', "Don't have an account? Create one now!")
create_page = LocatorInfo('accessibility id','Create your Fanatics ID')
privacy_page = LocatorInfo('accessibility id','Vertical scroll bar, 31 pages')
terms_of_use_page = LocatorInfo('accessibility id','Vertical scroll bar, 41 pages')
complete = LocatorInfo('accessibility id', 'Complete Fanatics ID registration')
weak_prompt = LocatorInfo('accessibility id', 'Consider some special characters and/or numbers.')
weak = LocatorInfo('accessibility id', 'Weak')
fair = LocatorInfo('accessibility id', 'Fair')
good = LocatorInfo('accessibility id', 'Good')
Strong = LocatorInfo('accessibility id', 'Strong')

'''Input username page'''
join_continue = LocatorInfo('accessibility id', 'Continue')
username = LocatorInfo('class name', 'XCUIElementTypeTextField')
invalid_username = LocatorInfo('accessibility id', 'This username is invalid.')
already_took_username = LocatorInfo('accessibility id', 'Someone already took that one.')

'''Collect page'''
logo_page = LocatorInfo('accessibility id', 'Select what you collect')
logo = LocatorInfo('accessibility id')

'''Track page'''
track = LocatorInfo('accessibility id', 'Want an even more personalized experience?')
track_continue = LocatorInfo('accessibility id', 'Continue')
track_allow = LocatorInfo('accessibility id', 'Allow')

'''Notification page'''
notification = LocatorInfo('accessibility id', 'Stay up to date')
notification_allow = LocatorInfo('accessibility id', 'Allow')
notification_later = LocatorInfo('accessibility id', 'Ehhh, maybe later')
notification_no_allow = LocatorInfo('accessibility id', 'Don’t Allow')

'''Invite page'''
invite = LocatorInfo('accessibility id', 'Invite your friends')
access_code = LocatorInfo('accessibility id', 'Enter access code')
play_button = LocatorInfo('accessibility id', 'waitlistPlayButton')
avatar = LocatorInfo('accessibility id')

'''Access code page'''
access_code_input = LocatorInfo('class name', 'XCUIElementTypeTextField')
submit = LocatorInfo('accessibility id', 'Submit')

'''Follow page'''
follow = LocatorInfo(locator='(//XCUIElementTypeButton[@name="Follow"][1])')
unfollow = LocatorInfo(locator='(//XCUIElementTypeButton[@name="Following"])[1]')

'''Select level page'''
level = LocatorInfo('accessibility id')

'''Home page'''
home = LocatorInfo('accessibility id', 'Home')
profile = LocatorInfo('accessibility id', 'Profile')
complete_profile = LocatorInfo('accessibility id', 'Complete your wallet_addresses')
close_complete_profile = LocatorInfo('accessibility id', 'Close')
view_all = LocatorInfo('accessibility id', 'View all')
complete_and_ready = LocatorInfo()

'''Profile page'''
setting = LocatorInfo('name', 'gear')

'''Setting page'''
logout = LocatorInfo('accessibility id', 'Log out')
logout_confirm = LocatorInfo('accessibility id', 'Yes, log out')
my_address = LocatorInfo('accessibility id', 'My Addresses')
my_wallet = LocatorInfo(locator='//XCUIElementTypeStaticText[@name="My Wallet"]')
back = LocatorInfo('accessibility id', 'Back')

'''wallet '''
exit_add_payment = LocatorInfo('accessibility id', 'UIButton.Close')
card_number = LocatorInfo('accessibility id', 'Card number')
expiration_date = LocatorInfo('accessibility id', 'expiration date')
cvc = LocatorInfo('accessibility id', 'CVC')
country_list = LocatorInfo(locator='//XCUIElementTypeImage[@name="icon_chevron_down"]')
country_done = LocatorInfo('accessibility id', 'Done')
zip_number = LocatorInfo('accessibility id', 'ZIP')
set_up = LocatorInfo('accessibility id', 'Set up')

'''address page'''
firstname = LocatorInfo(locator='//XCUIElementTypeApplication[@name="Fanatics Live '
                                'Development"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther['
                                '2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                                '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                                '/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther'
                                '/XCUIElementTypeTextField[1]')
lastname = LocatorInfo(locator='//XCUIElementTypeApplication[@name="Fanatics Live '
                               'Development"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther['
                               '2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                               '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                               '/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther'
                               '/XCUIElementTypeTextField[2]')
address = LocatorInfo(locator='//XCUIElementTypeApplication[@name="Fanatics Live '
                              'Development"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther['
                              '2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                              '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                              '/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther'
                              '/XCUIElementTypeTextField[3]')
apartment = LocatorInfo(locator='//XCUIElementTypeApplication[@name="Fanatics Live '
                                'Development"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther['
                                '2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                                '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                                '/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther'
                                '/XCUIElementTypeTextField[4]')
zip_code = LocatorInfo(locator='//XCUIElementTypeApplication[@name="Fanatics Live '
                               'Development"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther['
                               '2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                               '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                               '/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther'
                               '/XCUIElementTypeTextField[5]')
city = LocatorInfo(locator='//XCUIElementTypeApplication[@name="Fanatics Live '
                           'Development"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther['
                           '2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                           '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                           '/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther'
                           '/XCUIElementTypeTextField[6]')
state = LocatorInfo(locator='//XCUIElementTypeApplication[@name="Fanatics Live '
                            'Development"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther['
                            '2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                            '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                            '/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther'
                            '/XCUIElementTypeTextField[7]')
phone = LocatorInfo(locator='//XCUIElementTypeApplication[@name="Fanatics Live '
                            'Development"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther['
                            '2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                            '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                            '/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther'
                            '/XCUIElementTypeTextField[9]')
state_value = LocatorInfo('class name', 'XCUIElementTypePickerWheel')
state_done = LocatorInfo('accessibility id', 'Done')
save_address = LocatorInfo('name', 'Save address')

'''address list'''
add_address = LocatorInfo('accessibility id', 'Add shipping address')
cancel_add_address = LocatorInfo(locator='//XCUIElementTypeButton[@name="Cancel"]')
address_item = LocatorInfo(locator='//XCUIElementTypeSwitch')
delete_address = LocatorInfo(locator='(//XCUIElementTypeButton[@name="Delete"])[2]')  # delete 2rd as default
confirm_delete_address = LocatorInfo('accessibility id', 'Delete address')
cancel_delete_address = LocatorInfo('accessibility id', 'No cancel')
back_to_setting = LocatorInfo('accessibility id', 'Settings')

'''wallet list'''
add_wallet = LocatorInfo(locator='//XCUIElementTypeButton[@name="+ Add"]')
wallet_list = LocatorInfo(locator='//XCUIElementTypeApplication[@name="Fanatics Live '
                                  'Development"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther['
                                  '2]/XCUIElementTypeOther[2]/XCUIElementTypeScrollView/XCUIElementTypeOther['
                                  '1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther['
                                  '1]/XCUIElementTypeOther/XCUIElementTypeCollectionView/XCUIElementTypeCell')
edit_card = LocatorInfo('accessibility id', 'Edit')
delete_card = LocatorInfo(locator='(//XCUIElementTypeImage[@name="icon_x"])[2]')  # delete 2rd as default
confirm_delete_card = LocatorInfo(locator='(//XCUIElementTypeButton[@name="Remove"])[3]')
cancel_delete_card = LocatorInfo(locator='//XCUIElementTypeButton[@name="Cancel"]')
done_edit_card = LocatorInfo('accessibility id', 'Done')
card_set_up = LocatorInfo('accessibility id', 'Set up')
