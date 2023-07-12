import unittest
from config.test_setup import get_driver
from utils.user_actions import Actions


class TestExistedAccount(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = get_driver()
        global do
        do = Actions(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test1_loginUserExisted(self) -> None:
        do.tap_login()
        do.input_email()
        do.tap_next()
        do.input_password()
        do.tap_fanatics_id()
        do.tape_track_with_allow()
        do.assert_element('accessibility id', 'Home', 'login success')

    def test2_LogOut(self) -> None:
        do.tap_profile()
        do.tap_setting()
        do.tap_logout()
        do.confirm_logout()
        do.assert_element('accessibility id', 'Log in', 'Log out success')


