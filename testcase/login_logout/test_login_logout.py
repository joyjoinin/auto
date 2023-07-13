import unittest
from config.test_setup import get_driver
from data.test_params import test_account, app_name
from utils.locator_info import home, login
from utils.user_actions import Actions


class TestExistedAccount(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = get_driver()
        self.driver.activate_app(app_name)
        global do
        do = Actions(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test1_loginUserExisted(self) -> None:
        do.tap_login()
        do.input_email(test_account)
        do.tap_next()
        do.input_password(test_account)
        do.tap_fanatics_id()
        do.assert_element(home, 'login success')

    def test2_LogOutUserExisted(self) -> None:
        do.tap_profile()
        do.tap_setting()
        do.tap_logout()
        do.confirm_logout()
        do.assert_element(login, 'Log out success')
