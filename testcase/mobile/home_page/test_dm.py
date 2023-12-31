import unittest
from time import sleep

import allure
from config.setup import get_driver
from data.mobile_params import test_account
from utils.mobile.locator_info import empty_chat_page, new_message_title, message_title
from utils.mobile.user_actions import Actions


@allure.severity(allure.severity_level.CRITICAL)
@allure.feature("Direct message")
class TestDMs(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = get_driver()
        global do
        do = Actions(self.driver)
        do.login_flow(test_account)
        sleep(5)
        do.tap_chart_on_homepage()

    def tearDown(self):
        self.driver.quit()

    @allure.story("Go direct message")
    def test1_go_direct_message(self):
        do.assert_element(message_title, 'get to messages page success')
        try:
            do.assert_element_by_xpath_attr(empty_chat_page, 'value', 'Nothing yet', 'This is empty')
        except Exception:
            print('List is not empty')

    @allure.story("add message")
    def test2_add_message(self):
        do.tap_add_chat()
        do.assert_element(new_message_title, 'get to new message page success')
        do.cancel_add_message()
        do.assert_element(message_title, 'cancel success')
        do.tap_back()
