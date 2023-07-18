import unittest
from time import sleep
import pytest
import allure
from appium.webdriver.common.appiumby import AppiumBy

from config.setup import get_driver
from data.params import address_info, card_info, app_name, test_account, new_account
from utils.find_element import get_element, get_element_by_xpath
from utils.locator_info import address_item, password, password_after_input
from utils.save_accounts import save_data
from utils.user_actions import Actions
from appium.webdriver.common.touch_action import TouchAction


def get_input_password(driver, password):
    pass


class Test_debugs(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = get_driver()
        self.driver.activate_app(app_name)
        global do
        do = Actions(self.driver)

    # def tearDown(self):
    #     self.driver.terminate_app(app_name)

    def test1_loginUserExisted(self) -> None:
        save_data(test_account.email,test_account.password)