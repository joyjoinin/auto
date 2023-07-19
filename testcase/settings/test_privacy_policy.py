import unittest
import allure
from config.setup import get_driver
from utils.locator_info import text_container
from utils.user_actions import Actions


@allure.feature("Privacy policy")
class TestPurchases(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = get_driver()
        global do
        do = Actions(self.driver)

    def tearDown(self):
        do.back_to_setting()
        self.driver.quit()

    @allure.story("privacy policy")
    def test1_privacy_policy(self):
        do.tap_setting_privacy_policy()
        do.assert_element_by_xpath(text_container,'go privacy policy success')
