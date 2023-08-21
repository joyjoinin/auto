import unittest
import allure
from config.setup import get_driver
from data.mobile_params import random_spot_name
from utils.mobile.locator_info import spots_randomly
from utils.mobile.user_actions import Actions


@allure.severity(allure.severity_level.CRITICAL)
@allure.feature("Live")
class TestRandomSetPrice(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = get_driver(no_rest=True)
        global do
        do = Actions(self.driver)
        do.assert_element(spots_randomly, 'this is random & set price listing')

    # def tearDown(self):
    #     self.driver.quit()

    @allure.story("Buy a spot")
    def test1_buy_a_spot(self) -> None:
        buy_spot_num = do.get_buy_spots_num()
        single_spot_price = do.get_single_price()
        while buy_spot_num != 1:
            do.decrease_spot()
            buy_spot_num -= 1
        beginning_remained = do.get_all_spots_num()[0]
        do.tap_to_buy()
        do.asser_order_detail(random_spot_name,single_spot_price)
        after_remained = do.get_all_spots_num()[0]
        assert beginning_remained == after_remained + 1

    @allure.story("Buy all spot")
    def test2_buy_all_spot(self) -> None:
        buy_spot_num = do.get_buy_spots_num()
        single_spot_price = do.get_single_price()
        beginning_remained = do.get_all_spots_num()[0]
        while buy_spot_num != beginning_remained:
            do.increase_spot()
            buy_spot_num += 1
        do.tap_to_buy()
