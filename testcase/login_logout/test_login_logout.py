import unittest
from config.setup import get_driver
from data.params import test_account, app_name
from utils.locator_info import home, login
from utils.user_actions import Actions


class TestLoginLogout(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = get_driver()
        self.driver.activate_app(app_name)
        global do
        do = Actions(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test1_loginUserExisted(self) -> None:
        do.login_flow()
        do.assert_element(home, 'login success')

    def test2_LogOutUserExisted(self) -> None:
        do.logout_flow()
        do.assert_element(login, 'Log out success')
