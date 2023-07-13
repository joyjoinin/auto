class LocatorInfo:
    def __init__(self, by_type=None, locator=None):
        self.type = by_type
        self.locator = locator


login = LocatorInfo('accessibility id', 'Log in')
email = LocatorInfo('class name', 'XCUIElementTypeTextField')
login_next = LocatorInfo('accessibility id', 'Next')
password = LocatorInfo('class name', 'XCUIElementTypeSecureTextField')
fanaticsID = LocatorInfo('accessibility id', 'Log in with Fanatics ID')
track = LocatorInfo('accessibility id', 'Want an even more personalized experience?')
track_continue = LocatorInfo('accessibility id', 'Continue')
track_allow = LocatorInfo('accessibility id', 'Allow')
home = LocatorInfo('accessibility id', 'Home')
profile = LocatorInfo('accessibility id', 'Profile')
setting = LocatorInfo('name', 'gear')
logout = LocatorInfo('accessibility id', 'Log out')
logout_confirm = LocatorInfo('accessibility id', 'Yes, log out')
join = LocatorInfo('accessibility id', 'Join')
complete = LocatorInfo('accessibility id', 'Complete Fanatics ID registration')
username = LocatorInfo('class name', 'XCUIElementTypeTextField')
join_continue = LocatorInfo('accessibility id', 'Continue')
notification = LocatorInfo('accessibility id', 'Stay up to date')
notification_allow = LocatorInfo('accessibility id', 'Allow')
notification_later = LocatorInfo('accessibility id', 'Ehhh, maybe later')
notification_no_allow = LocatorInfo('accessibility id', 'Don’t Allow')
invite = LocatorInfo('accessibility id', 'Invite your friends')
access_code = LocatorInfo('accessibility id', 'Enter access code')
play_button = LocatorInfo('accessibility id', 'waitlistPlayButton')
avatar = LocatorInfo('accessibility id')
access_code_input = LocatorInfo('class name', 'XCUIElementTypeTextField')
submit = LocatorInfo('accessibility id', 'Submit')
logo = LocatorInfo('accessibility id')
follow = LocatorInfo(locator='(//XCUIElementTypeButton[@name="Follow"])[%s]')
unfollow = LocatorInfo(locator='(//XCUIElementTypeButton[@name="Following"])[%s]')
level = LocatorInfo(locator='(//XCUIElementTypeImage[@name="radioUnselected"])[%s]')
complete_profile = LocatorInfo('accessibility id', 'Complete your profile')
close_complete_profile = LocatorInfo('accessibility id', 'Close')
view_all = LocatorInfo('accessibility id', 'View all')
exit_add_payment = LocatorInfo('accessibility id', 'UIButton.Close')
card_number = LocatorInfo('accessibility id', 'Card number')
expiration_date = LocatorInfo('accessibility id', 'expiration date')
cvc = LocatorInfo('accessibility id', 'CVC')
country_list = LocatorInfo(locator='//XCUIElementTypeImage[@name="icon_chevron_down"]')
country_done = LocatorInfo('accessibility id', 'Done')
zip_number = LocatorInfo('accessibility id', 'ZIP')
set_up = LocatorInfo('accessibility id', 'Set up')
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
my_address = LocatorInfo('accessibility id', 'My Addresses')
my_wallet = LocatorInfo(locator='//XCUIElementTypeStaticText[@name="My Wallet"]')
add_address = LocatorInfo('accessibility id', 'Add shipping address')
cancel_add_address = LocatorInfo(locator='//XCUIElementTypeButton[@name="Cancel"]')
address_item = LocatorInfo(locator='//XCUIElementTypeSwitch')
delete_address = LocatorInfo(locator='(//XCUIElementTypeButton[@name="Delete"])[2]')  # delete 2rd as default
confirm_delete_address = LocatorInfo('accessibility id', 'Delete address')
cancel_delete_address = LocatorInfo('accessibility id', 'No cancel')
back_to_setting = LocatorInfo('accessibility id', 'Settings')
back = LocatorInfo('accessibility id', 'Back')
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