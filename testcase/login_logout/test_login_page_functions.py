import unittest
from time import sleep
import allure
from config.setup import get_driver
from data.params import nonexistent_account, error_password_account, test_account
from utils.find_element import get_element_by_xpath, get_element
from utils.locator_info import failed_login_message, login_next, password, password_after_input, check_your_email, \
    terms_of_use, create_page, create_one_now
from utils.user_actions import Actions
from appium.webdriver.common.touch_action import TouchAction


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
        do.input_password(test_account)
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
        pass
        # ele = get_element(self.driver,terms_of_use)
        # action = TouchAction(self.driver)
        # action.move_to(ele,ele.text.find('Terms of Use'),ele.text.find('Terms of Use') + 12)
        # action.tap(ele,ele.text.find('Terms of Use'),ele.text.find('Terms of Use') + 12).perform()

    @allure.story("check privacy policy")
    def test5_check_privacy_policy(self) -> None:
        pass

    @allure.story("check create one now")
    def test6_check_create_one_now(self) -> None:
        pass
        # do.input_email(error_password_account)
        # do.tap_next()
        # do.input_password(error_password_account)
        # do.tap_fanatics_id()
        # do.tap_create_new_one()
        # get_element(self.driver,create_one_now).click()
        # assert get_element(self.driver,create_page)
        # print('Turn to creat page success')