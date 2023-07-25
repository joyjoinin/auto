import unittest
import allure
from config.setup import get_driver
from data.params import test_account
from utils.locator_info import home, login
from utils.user_actions import Actions


@allure.severity(allure.severity_level.CRITICAL)
@allure.feature("Login && Log out")
class TestLoginLogout(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = get_driver()
        global do
        do = Actions(self.driver)
    def tearDown(self):
        self.driver.quit()

    @allure.story("Login")
    def test1_loginUserExisted(self):
        do.login_flow(test_account)
        do.assert_element(home, 'Login success')

    @allure.story("Log out")
    def test2_LogOutUserExisted(self) -> None:
        do.logout_flow()
        do.assert_element(login, 'Log out success')
