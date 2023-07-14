import unittest
from time import sleep
import pytest
import allure
from appium.webdriver.common.appiumby import AppiumBy

from config.setup import get_driver
from data.params import address_info, card_info, app_name, test_creat_account
from utils.find_element import get_element
from utils.locator_info import address_item
from utils.user_actions import Actions
from appium.webdriver.common.touch_action import TouchAction


class Test_debugs(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = get_driver()
        self.driver.activate_app(app_name)
        global do
        do = Actions(self.driver)

    # def tearDown(self):
    #     self.driver.terminate_app(app_name)

    def test1_loginUserExisted(self) -> None:
        do.tap_continue()