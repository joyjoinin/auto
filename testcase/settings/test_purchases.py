import unittest
import allure
from config.setup import get_driver
from utils.locator_info import purchases_navigation_bar, empty_purchases_list
from utils.user_actions import Actions


@allure.severity(allure.severity_level.CRITICAL)
@allure.feature("Purchases")
class TestPurchases(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = get_driver()
        global do
        do = Actions(self.driver)

    def tearDown(self):
        do.back_to_setting()
        do.logout_flow()
        self.driver.quit()

    @allure.story("empty purchase")
    def test1_empty_purchase(self):
        do.tap_purchases()
        do.assert_element(purchases_navigation_bar, 'get to purchases page success')
        do.assert_element(empty_purchases_list, 'empty purchases list')
