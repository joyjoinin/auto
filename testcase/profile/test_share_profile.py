import unittest
import allure
from config.setup import get_driver
from data.mobile_params import test_account
from mobile.mobile_locator_info import share_frame
from mobile.mobile_user_actions import Actions


@allure.severity(allure.severity_level.CRITICAL)
@allure.feature("Share profile")
class TestInviteFriends(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = get_driver()
        global do
        do = Actions(self.driver)
        do.login_flow(test_account)
        do.tap_profile()

    def tearDown(self):
        self.driver.quit()

    @allure.story("share profile")
    def test1_invite_friends(self):
        do.tap_share_profile()
        do.assert_element(share_frame, 'Open share success')
        do.tap_close_share()
