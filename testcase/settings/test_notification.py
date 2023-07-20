import unittest
import allure
from config.setup import get_driver
from utils.locator_info import livestreams, marketing_rewards, community
from utils.user_actions import Actions


@allure.severity(allure.severity_level.CRITICAL)
@allure.feature("Notifications")
class TestPurchases(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = get_driver()
        global do
        do = Actions(self.driver)


    def tearDown(self):
        do.back_to_setting()
        self.driver.quit()

    @allure.story("notifications")
    def test1_notifications(self):
        do.tap_notifications()
        do.assert_element(livestreams,'find livestreams')
        do.assert_element(marketing_rewards,'find marketing rewards')
        do.assert_element(community,'find community')
