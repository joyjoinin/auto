import unittest
import allure
from config.setup import get_driver
from utils.find_element import get_element
from utils.locator_info import invite_frame, invite_pop, share_frame
from utils.user_actions import Actions


@allure.severity(allure.severity_level.CRITICAL)
@allure.feature("Share profile")
class TestInviteFriends(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = get_driver()
        global do
        do = Actions(self.driver)
    def tearDown(self):
        self.driver.quit()

    @allure.story("share profile")
    def test1_invite_friends(self):
        do.tap_share_profile()
        do.assert_element(share_frame, 'Open share success')
        do.tap_close_share()
