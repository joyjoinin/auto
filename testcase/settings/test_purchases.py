import unittest
import allure
import pytest

from config.setup import get_driver
from utils.mobile.locator_info import purchases_navigation_bar, empty_purchases_list, items_in_purchases_list
from utils.mobile.user_actions import Actions


@allure.severity(allure.severity_level.CRITICAL)
@allure.feature("Purchases")
class TestPurchases(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = get_driver()
        global do
        do = Actions(self.driver)
        do.get_to_settings()

    def tearDown(self):
        self.driver.quit()

    @allure.story("empty purchase")
    @pytest.mark.skip('use account with data')
    def test1_empty_purchase(self):
        do.tap_purchases()
        do.assert_element(purchases_navigation_bar, 'get to purchases page success')
        do.assert_element(empty_purchases_list, 'empty purchases list')

    @allure.story("purchase list")
    def test2_purchase_list(self):
        do.tap_purchases()
        do.assert_elements_by_xpath(items_in_purchases_list, 'have purchases list')

