import unittest
import allure
from config.setup import get_driver
from data.params import test_account
from utils.user_actions import Actions


@allure.severity(allure.severity_level.CRITICAL)
@allure.feature("Home logos")
class TestHomeLogos(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = get_driver()
        global do
        do = Actions(self.driver)
        do.open_app()

    def tearDown(self):
        self.driver.quit()

    @allure.story("Swipe logo")
    def test1_swipe_logo(self):
        # do.login_flow(test_account)
        pass

    @allure.story("tap first logo")
    def test2_tap_first_logo(self):
        # do.login_flow(test_account)
        pass

    @allure.story("tap first logo")
    def test3_tap_last_logo(self):
        # do.login_flow(test_account)
        pass