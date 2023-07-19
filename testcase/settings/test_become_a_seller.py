import unittest
import allure
from config.setup import get_driver
from utils.user_actions import Actions


@allure.feature("Become a seller")
class TestPurchases(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = get_driver()
        global do
        do = Actions(self.driver)

    def tearDown(self):
        do.back_to_setting()
        self.driver.quit()

    @allure.story("become a seller")
    def test1_become_a_seller(self):
        do.tap_setting()
        do.tap_become_a_seller()
