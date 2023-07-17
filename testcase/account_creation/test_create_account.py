import unittest
from time import sleep
from config.setup import get_driver
from data.params import new_account
from utils.user_actions import Actions
import allure


@allure.feature("Account Creation")
class TestAccountCreation(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = get_driver()
        global do
        do = Actions(self.driver)
        do.open_app()

    def tearDown(self):
        do.logout_flow()
        self.driver.quit()

    @allure.story("Create new account")
    def test_create_new_account(self) -> None:
        do.tap_join()
        sleep(3)
        do.input_email(new_account)
        do.input_password(new_account)
        do.tap_complete()
        sleep(5)
        do.input_username(new_account.username)
        do.tap_continue()
        sleep(3)
        try:
            do.set_notification()
            sleep(3)
        except Exception:
            raise
        finally:
            do.tap_enter_access_code()
            sleep(3)
            do.input_code(new_account.access_code)
            do.tap_submit()
            do.tap_logos(new_account.logo_name)
            do.tap_continue()
            do.tap_follow(new_account.follow_count)
            do.tap_continue()
            do.select_level(new_account.level_index)
            do.tap_continue()
