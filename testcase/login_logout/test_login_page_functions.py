import unittest
import allure
from time import sleep
from config.setup import get_driver
from data.params import error_password_account, test_account
from utils.find_element import get_element_by_xpath, get_element
from utils.locator_info import login_next, password, password_after_input, check_your_email, \
    terms_of_use, create_page, create_one_now, privacy_page, terms_of_use_page
from utils.user_actions import Actions
from appium.webdriver.common.touch_action import TouchAction


@allure.severity(allure.severity_level.CRITICAL)
@allure.feature("Login page's functions")
class TestCheckFunctions(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = get_driver()
        global do
        do = Actions(self.driver)
        do.open_app()
        do.tap_login()

    def tearDown(self):
        do.close_app()
        self.driver.quit()

    @allure.story("Check Not You")
    def test1_check_not_you(self) -> None:
        do.input_email(test_account)
        do.tap_next()
        do.tap_not_you()
        do.assert_element(login_next, 'Tap Not You success')

    @allure.story("check show/hide password")
    def test2_check_show_password(self) -> None:
        do.input_email(test_account)
        do.tap_next()
        do.input_password(test_account.password)
        do.tap_show_password()
        assert get_element_by_xpath(self.driver, password_after_input).get_attribute('value') == test_account.password
        print('Show password success')
        do.tap_hide_password()
        assert get_element(self.driver, password).get_attribute('value') == '•' * len(test_account.password)
        print('Hide password success')

    @allure.story("check forget password")
    def test3_check_forget_password(self) -> None:
        do.input_email(test_account)
        do.tap_next()
        do.tap_forget_password()
        assert get_element(self.driver, check_your_email)
        print('Send email success')

    @allure.story("check terms of use")
    def test4_check_terms_of_use(self) -> None:
        sleep(3)
        target_element = get_element(self.driver, terms_of_use)
        target_text_start = target_element.text.index('Terms of Use')
        line_len = len('By tapping log in, you agree to our Terms of Use and acknowledge')
        text_location = target_element.location
        text_size = target_element.size
        target_y = text_location['y'] + text_size['height'] / 4
        target_x = text_location['x'] + text_size['width'] * (target_text_start + len('Terms of Use') / 2) / line_len
        touch_action = TouchAction(self.driver)
        touch_action.tap(x=target_x, y=target_y).perform()
        do.assert_element_by_xpath(terms_of_use_page, 'get terms of use success')

    @allure.story("check privacy policy")
    def test5_check_privacy_policy(self) -> None:
        sleep(3)
        target_element = get_element(self.driver, terms_of_use)
        text_location = target_element.location
        text_size = target_element.size
        target_y = text_location['y'] + text_size['height'] * 3 / 4
        target_x = text_location['x'] + text_size['width'] / 2
        touch_action = TouchAction(self.driver)
        touch_action.tap(x=target_x, y=target_y).perform()
        do.assert_element_by_xpath(privacy_page, 'get privacy success')

    @allure.story("check create one now")
    def test6_check_create_one_now(self) -> None:
        do.input_email(error_password_account)
        do.tap_next()
        do.input_password(error_password_account.password)
        do.tap_fanatics_id()
        sleep(2)
        target_element = get_element(self.driver, create_one_now)
        target_text_start = target_element.text.index('Create one now')
        line_len = len("Don't have an account? Create one now!")
        text_location = target_element.location
        text_size = target_element.size
        target_y = text_location['y'] + text_size['height'] / 2
        target_x = text_location['x'] + text_size['width'] * (target_text_start + len('Create one now') / 2) / line_len
        touch_action = TouchAction(self.driver)
        touch_action.tap(x=target_x, y=target_y).perform()
        do.assert_element(create_page, 'Turn to create page success')
