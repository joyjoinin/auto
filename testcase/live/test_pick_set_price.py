import unittest
import allure
from config.setup import get_driver
from utils.find_element import get_element_by_xpath
from utils.locator_info import spot_item
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

    @allure.story("Buy a spot")
    def test1_buy_first_spot(self) -> None:
        do.pick_your_spot()
        do.swipe_up()
        do.pick_a_spot(1)
        do.pay_now()
        do.tap_return_to_stream()
