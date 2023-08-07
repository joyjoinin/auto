import unittest
import allure
from config.setup import get_driver
from data.params import won_message
from utils.mobile_utils.mobile_locator_info import sold_out, first_won, first_won_price, \
    first_won_name, first_item_button
from utils.mobile_utils.mobile_user_actions import Actions


@allure.severity(allure.severity_level.CRITICAL)
@allure.feature("Live")
class TestPickSetPrice(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = get_driver(no_rest=True)
        global do
        do = Actions(self.driver)

    def tearDown(self):
        self.driver.quit()

    @allure.story("Buy a spot")  # always first spot
    def test1_buy_a_spot(self) -> None:
        do.pick_your_spot()
        do.swipe_down(30)
        spot_price = do.get_price(first_item_button)
        spot_name = do.get_first_spot_name()
        do.tap_first_spot()
        do.asser_order_detail(spot_name,spot_price)
        do.tap_return_to_stream()
        do.assert_element_by_xpath(first_won, 'Buy spot success')
        won_price = do.get_price(first_won_price)
        won_spot_name = do.get_attr_xpath(first_won_name, 'label')
        message = do.get_latest_message()
        assert won_message in message
        assert won_price == spot_price
        assert won_spot_name == spot_name

    @allure.story("Buy spots")
    def test1_buy_spots(self) -> None:
        listing_sold_out = False
        first_page_sold_out = False
        do.pick_your_spot()
        while listing_sold_out is False:
            while first_page_sold_out is False:
                try:
                    do.swipe_down(30)
                    do.tap_spot_automated()
                    do.pay_now()
                    do.tap_return_to_stream()
                except:
                    print('first page sold out')
                    first_page_sold_out = True
            while first_page_sold_out is True:
                try:
                    do.swipe_up(-60)
                    do.tap_spot_automated()
                    do.pay_now()
                    do.tap_return_to_stream()
                except Exception as e:
                    listing_sold_out = True
                    break
        do.swap_down_spots_listing()
        do.assert_element(sold_out, 'Sold out success')
