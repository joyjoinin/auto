import random
import unittest
from time import sleep
from config.setup import get_driver
from data.params import new_account
from utils.find_element import get_element
from utils.locator_info import join_continue, invalid_username, already_took_username, logo_page, notification
from utils.save_accounts import save_data
from utils.user_actions import Actions
import allure


@allure.feature("Username Creation")
class TestAccountCreation(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = get_driver()
        global do
        do = Actions(self.driver)
        do.open_app()

    def tearDown(self):
        do.close_app()
        self.driver.quit()

    @allure.story("Create without username")
    def test01_create_without_username(self) -> None:
        do.tap_join()
        sleep(3)
        do.input_email(new_account)
        do.input_password(new_account.password)
        do.tap_complete()
        save_data(new_account.email, new_account.password)
        do.assert_element_by_attr(join_continue, 'enabled', 'false', "Can't continue without username")

    @allure.story("Create with username invalid")
    def test02_create_with_username_invalid(self) -> None:
        do.input_username(new_account.invalid_name)
        do.assert_element_by_attr(join_continue, 'enabled', 'false', "Can't continue with username invalid")
        do.assert_element(invalid_username,'This username is invalid')

    @allure.story("Create with username already took")
    def test03_create_with_username_already_took(self) -> None:
        do.input_username(new_account.already_took_username)
        do.assert_element_by_attr(join_continue, 'enabled', 'true', "Can't continue with username already took")
        do.assert_element(already_took_username,'This username is already took')
        do.tap_continue()
        try:
            get_element(self.driver,logo_page)
        except:
            print('Continue failed with username already took')

    @allure.story("Create with correct username ")
    def test04_create_with_username_valid(self) -> None:
        do.input_username('test' + str(random.randint(0, 10000)))
        do.tap_continue()
        # do.tap_enter_access_code()
        # sleep(3)
        # do.input_code(new_account.access_code)
        # do.tap_submit()
        do.tap_logos(new_account.logo_select)
        do.tap_continue()
        do.tap_follow(new_account.follow_count)
        do.tap_continue()
        try:
            get_element(self.driver,notification)
            do.set_notification_later()
        except Exception:
            print('already set notification')
        finally:
            do.select_level(new_account.level_index)
            do.tap_continue()


