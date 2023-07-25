class LocatorInfo:
    def __init__(self, by_type=None, locator=None):
        self.type = by_type
        self.locator = locator


''' App Home '''
login = LocatorInfo('accessibility id', 'Log in')
join = LocatorInfo('accessibility id', 'Join')
home_window = LocatorInfo('class name', 'XCUIElementTypeWindow')

''' Log in page'''
email = LocatorInfo('class name', 'XCUIElementTypeTextField')
login_next = LocatorInfo('accessibility id', 'Next')
password = LocatorInfo('class name', 'XCUIElementTypeSecureTextField')
password_after_input = LocatorInfo(
    locator='//XCUIElementTypeApplication[@name="Fanatics Live Development"]/XCUIElementTypeWindow['
            '1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
            '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
            '/XCUIElementTypeOther/XCUIElementTypeTextField[2]')
failed_login_message = LocatorInfo('accessibility id', 'Invalid email or password')
check_your_email = LocatorInfo('accessibility id', 'Check your email')
fanaticsID = LocatorInfo('accessibility id', 'Log in with Fanatics ID')
not_you = LocatorInfo('accessibility id', 'NOT YOU?')
show_password = LocatorInfo('accessibility id', 'SHOW')
hide_password = LocatorInfo('accessibility id', 'HIDE')
forget_password = LocatorInfo('accessibility id', 'Forgot password?')
terms_of_use = LocatorInfo('accessibility id',
                           'By tapping log in, you agree to our Terms of Use and acknowledge our Privacy policy')
create_one_now = LocatorInfo('accessibility id', "Don't have an account? Create one now!")
create_page = LocatorInfo('accessibility id', 'Create your Fanatics ID')
# privacy_page = LocatorInfo('accessibility id', 'Vertical scroll bar, 31 pages')
# terms_of_use_page = LocatorInfo('accessibility id', 'Vertical scroll bar, 41 pages')
terms_of_use_page = LocatorInfo(locator='//XCUIElementTypeApplication[@name="Fanatics Live '
                                        'Development"]/XCUIElementTypeWindow['
                                        '1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                                        '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                                        '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                                        '/XCUIElementTypeWebView/XCUIElementTypeWebView/XCUIElementTypeWebView')
privacy_page = LocatorInfo(locator='//XCUIElementTypeApplication[@name="Fanatics Live '
                                   'Development"]/XCUIElementTypeWindow['
                                   '1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                                   '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                                   '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                                   '/XCUIElementTypeWebView/XCUIElementTypeWebView/XCUIElementTypeWebView')
complete = LocatorInfo('accessibility id', 'Complete Fanatics ID registration')
weak_prompt = LocatorInfo('accessibility id', 'Consider some special characters and/or numbers.')
weak = LocatorInfo('accessibility id', 'Weak')
fair = LocatorInfo('accessibility id', 'Fair')
good = LocatorInfo('accessibility id', 'Good')
Strong = LocatorInfo('accessibility id', 'Strong')
already_in_use = LocatorInfo('accessibility id', 'That email is already in use')

'''Input username page'''
username_page = LocatorInfo('accessibility id', "It's name time")
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
home_navigation_bar = LocatorInfo(locator='//XCUIElementTypeNavigationBar[@name="_TtGC7SwiftUI32NavigationStackHosting"]')
home = LocatorInfo('accessibility id', 'Home')
profile = LocatorInfo('accessibility id', 'Profile')
complete_profile = LocatorInfo('accessibility id', 'Complete your profile')
close_complete_profile = LocatorInfo('accessibility id', 'Close')
view_all = LocatorInfo('accessibility id', 'View all')
complete_and_ready = LocatorInfo()
search_on_homepage = LocatorInfo(locator='//XCUIElementTypeButton[@name="magnifyingGlass"]')
chat_on_homepage = LocatorInfo(locator='//XCUIElementTypeOther[@name="chatBubbleEmpty"]')
hero_card_position = LocatorInfo(locator='')
you_might_also_like = LocatorInfo('accessibility id', 'sectionheaderYouMightAlsoLike')
recommend_location = LocatorInfo(locator='//XCUIElementTypeStaticText[@name="sectionheaderYouMightAlsoLike"]/following'
                                         '-sibling::XCUIElementTypeOther')
recommend_shops_to_follow = LocatorInfo(locator='(//XCUIElementTypeButton[@name="Follow"])')
recommend_shops_already_following = LocatorInfo(locator='(//XCUIElementTypeButton[@name="Following"])')
'''Search page'''
search_field = LocatorInfo(locator='//XCUIElementTypeApplication[@name="Fanatics Live '
                                   'Development"]/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther'
                                   '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                                   '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                                   '/XCUIElementTypeOther/XCUIElementTypeOther['
                                   '3]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                                   '/XCUIElementTypeOther/XCUIElementTypeTextField')
popular_streams_title = LocatorInfo('accessibility id', 'sectionheaderPopularStreams')
close_search_page = LocatorInfo(locator='//XCUIElementTypeButton[@name="Close"]')

'''Chat page'''
message_title = LocatorInfo('accessibility id', 'Messages')
add_chat = LocatorInfo(locator='//XCUIElementTypeButton[@name="chatAdd"]')
empty_chat_page = LocatorInfo(locator='(//XCUIElementTypeStaticText[@name="ChatChannelListView"])[1]')

# new message
cancel_add_message = LocatorInfo('accessibility id', 'Cancel')
new_message_title = LocatorInfo('accessibility id', 'New Message')
message_search_bar = LocatorInfo('class name', 'XCUIElementTypeTextField')
clear_message_search_bar = LocatorInfo(locator='//XCUIElementTypeButton[@name="SearchBar"]')
message_welcome = LocatorInfo('accessibility id', 'Helloooooo?')

'''Logo scroll view'''
logo_scroll_view = LocatorInfo(locator='//XCUIElementTypeAny[@name="Fanatics Live '
                                       'Development"]/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther'
                                       '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                                       '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                                       '/XCUIElementTypeOther/XCUIElementTypeOther['
                                       '2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                                       '/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther'
                                       '/XCUIElementTypeScrollView')

logo_items = LocatorInfo(locator='//XCUIElementTypeAny[@name="Fanatics Live '
                                 'Development"]/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther'
                                 '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                                 '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                                 '/XCUIElementTypeOther/XCUIElementTypeOther['
                                 '2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                                 '/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther'
                                 '/XCUIElementTypeScrollView/XCUIElementTypeOther/XCUIElementTypeStaticText')

logo_item = LocatorInfo('accessibility id')
logo_title = LocatorInfo('class name', 'XCUIElementTypeNavigationBar')

'''Popular live breaks page'''
popular_page_title = LocatorInfo(locator='//XCUIElementTypeStaticText[@name="Popular Live Breaks"]')

'''Profile page'''
setting = LocatorInfo('name', 'gear')
edit_profile = LocatorInfo('accessibility id', 'Edit Profile')
invite_friends = LocatorInfo('accessibility id', 'Invite friends')
share_profile = LocatorInfo('accessibility id', 'Share Profile')
profile_followers = LocatorInfo('accessibility id', 'Followers')
profile_following = LocatorInfo('accessibility id', 'Following')
favorite_shops = LocatorInfo('accessibility id', 'sectionheaderFavoriteShops')

'''Edit profile page'''
edit_avatar = LocatorInfo(locator='//XCUIElementTypeImage[@name="pencil"]')
edit_username = LocatorInfo(locator='(//XCUIElementTypeButton[@name="pencil"])[1]')
profile_username = LocatorInfo(locator='//XCUIElementTypeStaticText['
                                       '@name="Username"]/following-sibling::XCUIElementTypeStaticText')
edit_self_intro = LocatorInfo(locator='(//XCUIElementTypeButton[@name="pencil"])[2]')
profile_self_intro = LocatorInfo(locator='//XCUIElementTypeStaticText['
                                         '@name="Biography"]/following-sibling::XCUIElementTypeStaticText')
add_interests = LocatorInfo('accessibility id', 'plus')
all_interests = LocatorInfo(
    locator='//XCUIElementTypeStaticText[@name="My '
            'Interests"]/following-sibling::XCUIElementTypeOther/XCUIElementTypeStaticText')

'''Avatar page'''
camera_add = LocatorInfo('accessibility id', 'cameraAdd')
add_media_image = LocatorInfo('accessibility id', 'addMediaImage')
avatar_colorful = LocatorInfo(
    locator='//XCUIElementTypeButton[@name="addMediaImage"]/following-sibling::XCUIElementTypeOther'
            '/XCUIElementTypeButton')
save_avatar = LocatorInfo(locator='//XCUIElementTypeButton[@name="Save"]')

'''Add interests page'''
back_to_edit_page = LocatorInfo('accessibility id', 'Edit Profile')

'''Edit username page'''
username_input_box = LocatorInfo('class name', 'XCUIElementTypeTextField')
save_username = LocatorInfo(locator='//XCUIElementTypeButton[@name="Save"]')

'''Edit intro page'''
intro_text_field = LocatorInfo('class name', 'XCUIElementTypeTextView')
save_intro = LocatorInfo(locator='//XCUIElementTypeButton[@name="Save"]')

'''Invite friends'''
invite_frame = LocatorInfo('accessibility id', 'Gift your friends VIP access')
send_invite = LocatorInfo('accessibility id', 'Send invite')
cancel_invite = LocatorInfo('accessibility id', 'No, cancel')
invite_pop = LocatorInfo('accessibility id', 'ActivityListView')
close_invite_pop = LocatorInfo('accessibility id', 'Close')

'''Share profile'''
share_frame = LocatorInfo('accessibility id', 'ActivityListView')
close_share_frame = LocatorInfo('accessibility id', 'Close')

'''follow list page'''
search_glass = LocatorInfo('accessibility id', 'magnifyingGlass')
following_list_title = LocatorInfo(locator='//XCUIElementTypeStaticText[@name="Following"]')
followers_list_title = LocatorInfo(locator='//XCUIElementTypeStaticText[@name="Followers"]')
empty_following_list = LocatorInfo('accessibility id', 'Hello darkness...')
empty_followers_list = LocatorInfo('accessibility id', 'Who needs followers?')

'''Setting page'''
logout_confirm = LocatorInfo('accessibility id', 'Yes, log out')
my_address = LocatorInfo('accessibility id', 'My Addresses')
my_wallet = LocatorInfo(locator='//XCUIElementTypeStaticText[@name="My Wallet"]')
back = LocatorInfo('accessibility id', 'Back')
purchases = LocatorInfo('accessibility id', 'Purchases')
notifications = LocatorInfo('accessibility id', 'Notifications')
become_a_seller = LocatorInfo('accessibility id', 'Become a seller')
contact_us = LocatorInfo('accessibility id', 'Contact us')
FAQs = LocatorInfo('accessibility id', 'FAQs')
privacy_policy = LocatorInfo('accessibility id', 'Privacy policy')
terms_of_use_on_setting = LocatorInfo('accessibility id', 'Terms of use')
logout = LocatorInfo('accessibility id', 'Log out')

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

'''Purchases page'''
purchases_navigation_bar = LocatorInfo('class name', 'XCUIElementTypeNavigationBar')
empty_purchases_list = LocatorInfo('accessibility id', 'Ready to rip?')

'''Privacy policy page'''
text_container = LocatorInfo(locator='//XCUIElementTypeApplication[@name="Fanatics Live '
                                     'Development"]/XCUIElementTypeWindow['
                                     '1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                                     '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                                     '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                                     '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                                     '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeWebView'
                                     '/XCUIElementTypeWebView/XCUIElementTypeWebView')

'''Become a seller'''
become_a_seller_page = LocatorInfo(locator='//XCUIElementTypeStaticText[@name="Get in first. Want to sell with '
                                           'Fanatics Live, let us know!"]')
apply = LocatorInfo('accessibility id', 'Apply')

'''FQAs'''
FAQs_page = LocatorInfo(locator='//XCUIElementTypeOther[@name="How can we help you?"]')

'''Contact us'''
contact_us_page = LocatorInfo('accessibility id', "Thank you for using Fanatics Live. What's your email address?")

'''Notifications'''
livestreams = LocatorInfo('accessibility id', 'Livestreams')
marketing_rewards = LocatorInfo('accessibility id', 'Marketing & rewards')
community = LocatorInfo('accessibility id', 'Community')
turn_on_notification = LocatorInfo('accessibility id', 'Turn on notifications')
alert_notifications = LocatorInfo(locator='//XCUIElementTypeAlert[@name="“Fanatics Live Development” Would Like to '
                                          'Send You Notifications"]')
allow_notifications = LocatorInfo('accessibility id', 'Allow')
do_not_allow_notification = LocatorInfo('accessibility id', 'Don’t Allow')

# Livestreams
button_new_stream_added = LocatorInfo(locator='//XCUIElementTypeSwitch[@name="New stream added, Your favorite channel '
                                              'scheduled something new"]/XCUIElementTypeSwitch')
button_stream_going_live = LocatorInfo(
    locator='//XCUIElementTypeSwitch[@name="Stream going live, A stream is starting now"]/XCUIElementTypeSwitch')
button_giveaways = LocatorInfo(
    locator='//XCUIElementTypeSwitch[@name="Giveaways, Your chance at something great — for free!"]/XCUIElementTypeSwitch')
button_suggested_streams = LocatorInfo(
    locator='//XCUIElementTypeSwitch[@name="Suggested streams, We found something we think you’ll like"]/XCUIElementTypeSwitch')
button_push_notifications = LocatorInfo(
    locator='//XCUIElementTypeSwitch[@name="Push Notifications"]/XCUIElementTypeSwitch')
button_email = LocatorInfo(locator='//XCUIElementTypeSwitch[@name="Email"]/XCUIElementTypeSwitch')
back_to_notifications = LocatorInfo('accessibility id', 'Notifications')

# Marketing & rewards
button_breaking_news = LocatorInfo(
    locator='//XCUIElementTypeSwitch[@name="Breaking news, You\'re gonna want to hear this"]/XCUIElementTypeSwitch')
button_offers_rewards = LocatorInfo(
    locator='//XCUIElementTypeSwitch[@name="Offers & rewards, A chance to win FanCash and more"]/XCUIElementTypeSwitch')
button_events = LocatorInfo(
    locator='//XCUIElementTypeSwitch[@name="Events, Your ticket to a special event"]/XCUIElementTypeSwitch')

# Community
button_direct_messages = LocatorInfo(
    locator='//XCUIElementTypeSwitch[@name="Direct Messages, Someone has sent you a message"]/XCUIElementTypeSwitch')
button_new_followers = LocatorInfo(
    locator='//XCUIElementTypeSwitch[@name="New followers, Someone new is following you"]/XCUIElementTypeSwitch')
