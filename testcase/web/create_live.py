from selenium import webdriver
from time import sleep
from utils.common import  get_random_username
from utils.find_element import *
from web.web_locator_info import *

import unittest
import allure
from time import sleep
from config.setup import get_driver
from data.params import card_info
from web.web_user_actions import Actions


@allure.severity(allure.severity_level.CRITICAL)
@allure.feature("Bank Card")
class TestCard(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        global do
        do = Actions(self.driver)
    def tearDown(self):
        self.driver.quit()

    @allure.story("Add live with 4 listing different")
    def test1_add_live(self) -> None:
        do.login()
        do.sign_in()
        do.schedule_a_show()
        do.create_random_set_price_listing()
        do.create_random_auction()
        do.create_pick_spot_auction()
        do.create_pick_spot_set_price()
        do.publish()



