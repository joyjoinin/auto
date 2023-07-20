import unittest
import allure
from config.setup import get_driver
from data.params import nonexistent_account, error_password_account
from utils.locator_info import failed_login_message
from utils.user_actions import Actions


@allure.severity(allure.severity_level.MINOR)
@allure.feature("Login error")
class TestErrorLogin(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = get_driver()
        global do
        do = Actions(self.driver)
        do.open_app()
        do.tap_login()

    def tearDown(self):
        do.close_app()
        self.driver.quit()

    @allure.story("login with nonexistent account")
    def test1_login_with_nonexistent_account(self) -> None:
        do.input_email(nonexistent_account)
        do.tap_next()
        do.input_password(nonexistent_account.password)
        do.tap_fanatics_id()
        do.assert_element(failed_login_message, 'Failed log in')

    @allure.story("login with error password")
    def test2_login_with_error_password(self) -> None:
        do.input_email(error_password_account)
        do.tap_next()
        do.input_password(error_password_account.password)
        do.tap_fanatics_id()
        do.assert_element(failed_login_message, 'Failed log in')
