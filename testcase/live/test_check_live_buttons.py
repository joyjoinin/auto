import unittest
import allure
from config.setup import get_driver
from utils.locator_info import schedule_title, share_frame, contact_us_page, confirm_button, report_title, return_policy
from utils.user_actions import Actions


@allure.severity(allure.severity_level.CRITICAL)
@allure.feature("Live")
class TestLiveButtons(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = get_driver(no_rest=True)
        global do
        do = Actions(self.driver)

    def tearDown(self):
        self.driver.quit()

    @allure.story("shop")
    def test1_tap_shop(self) -> None:
        do.tap_shop()
        do.assert_element_by_xpath(return_policy,'Open shop page success')
        do.swap_down_shop_page()

    @allure.story("Flag")
    def test2_tap_flag(self) -> None:
        do.tap_flag()
        do.assert_element(confirm_button,'Open report page success',10)
        do.swap_down_report()
    @allure.story("share")
    def test3_tap_share(self) -> None:
        do.tap_share()
        do.assert_element(share_frame, 'Open share success')
        do.tap_close_share()

    @allure.story("schedule")
    def test4_tap_schedule(self) -> None:
        do.tap_schedule()
        do.assert_element(schedule_title,'Open schedule success')
        do.swap_down_schedule()
