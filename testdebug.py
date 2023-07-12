import unittest
from config.test_setup import get_driver
from data.test_params import address_info, card_info, app_name
from utils.find_element import get_element
from utils.user_actions import Actions
from appium.webdriver.common.touch_action import TouchAction


class Test_debugs(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = get_driver()
        self.driver.activate_app(app_name)
        global do
        do = Actions(self.driver)

    def tearDown(self):
        # self.driver.terminate_app(app_name)
            pass

    def test1_loginUserExisted(self) -> None:
        # do.add_card_flow(card_info)
        pass