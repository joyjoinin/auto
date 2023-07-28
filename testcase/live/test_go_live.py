import unittest
import allure
from config.setup import get_driver
from data.params import test_account, test_live_name
from utils.locator_info import close_live
from utils.user_actions import Actions


@allure.severity(allure.severity_level.CRITICAL)
@allure.feature("Live")
class TestGOLive(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = get_driver()
        global do
        do = Actions(self.driver)
        do.login_flow(test_account)

    def tearDown(self):
        self.driver.quit()

    @allure.story("Go live")
    def test1_go_live(self) -> None:
        do.try_find_live(test_live_name)
        do.tap_live()
        do.assert_element(close_live,'get in live success')
