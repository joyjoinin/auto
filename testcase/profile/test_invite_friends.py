import unittest
import allure
from time import sleep
from config.setup import get_driver
from utils.find_element import get_element
from utils.locator_info import invite_frame, invite_pop
from utils.user_actions import Actions


@allure.severity(allure.severity_level.CRITICAL)
@allure.feature("Invite friends")
class TestInviteFriends(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = get_driver()
        global do
        do = Actions(self.driver)
        do.tap_invite_friends_on_profile()

    def tearDown(self):
        self.driver.quit()

    @allure.story("invite friends")
    def test1_invite_friends(self):
        do.assert_element(invite_frame, 'open invite frame success')
        do.tap_send_invite()
        do.assert_element(invite_pop, 'open invite pop success')
        do.tap_close_invite()
        try:
            get_element(self.driver, invite_pop, 2)
        except Exception:
            print('close success')

    @allure.story("cancel invite")
    def test2_cancel_invite(self):
        sleep(2)
        do.tap_cancel_invite()
        try:
            get_element(self.driver, invite_frame, 2)
        except Exception:
            print('cancel success')
