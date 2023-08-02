import unittest
import allure
from config.setup import get_driver
from utils.find_element import get_elements_by_xpath, get_element
from utils.locator_info import spot_listing, last_spot, live, sold_out
from utils.user_actions import Actions


@allure.severity(allure.severity_level.CRITICAL)
@allure.feature("Live")
class TestPickSetPrice(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = get_driver()
        global do
        do = Actions(self.driver)

    #
    def tearDown(self):
        self.driver.quit()

    @allure.story("Buy spots")
    def test1_buy_spots(self) -> None:
        listing_sold_out = False
        first_page_sold_out = False
        all_buttons = spot_listing
        all_buttons.locator = spot_listing.locator + '//XCUIElementTypeButton'
        do.pick_your_spot()
        while listing_sold_out is False:
            while first_page_sold_out is False:
                try:
                    do.swipe_down(30)
                    get_elements_by_xpath(self.driver, spot_listing)[0].click()
                    do.pay_now()
                    do.tap_return_to_stream()
                except:
                    print('first page sold out')
                    first_page_sold_out = True
            while first_page_sold_out is True:
                try:
                    do.swipe_up(-60)
                    get_elements_by_xpath(self.driver, spot_listing)[0].click()
                    do.pay_now()
                    do.tap_return_to_stream()
                except Exception as e:
                    listing_sold_out = True
                    break
        do.common_swipe_vertical(get_element(self.driver, live), 200)
        do.assert_element(sold_out, 'Sold out success')
