from utils.common_mobile import LocatorInfo

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
