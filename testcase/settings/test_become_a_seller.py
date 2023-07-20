import unittest
import allure
from time import sleep
from config.setup import get_driver
from utils.locator_info import become_a_seller_page
from utils.user_actions import Actions


@allure.severity(allure.severity_level.CRITICAL)
@allure.feature("Become a seller")
class TestPurchases(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = get_driver()
        global do
        do = Actions(self.driver)
        do.open_app()
        do.tap_profile()
        do.tap_setting()

    def tearDown(self):
        do.back_to_setting()
        self.driver.quit()

    @allure.story("become a seller")
    def test1_become_a_seller(self):
        do.tap_become_a_seller()
        do.assert_element_by_xpath(become_a_seller_page,'show apply page success')
