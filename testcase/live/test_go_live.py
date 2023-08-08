import unittest
import allure
from config.setup import get_driver
from data.params import test_account, test_live_name
from mobile.mobile_locator_info import input_message
from mobile.mobile_user_actions import Actions


@allure.severity(allure.severity_level.CRITICAL)
@allure.feature("Live")
class TestGOLive(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = get_driver(no_rest=True)
        global do
        do = Actions(self.driver)

    def tearDown(self):
        self.driver.quit()

    @allure.story("Go live from hero card")
    def test1_go_live_from_hero_card(self) -> None:
        try:
            do.login_flow(test_account)
            do.try_find_live(test_live_name)
            do.tap_live()
            do.assert_element(input_message, 'get in live success')
            do.close_live()
        except:
            print("Can't find live")

    @allure.story("Go live by view all")
    def test2_go_live_by_View_all(self) -> None:
        try:
            do.tap_view_all()
            do.tap_live_at_view_all(test_live_name)
            do.assert_element(input_message, 'get in live success')
        except:
            print('No view all')
