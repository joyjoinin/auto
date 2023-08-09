import unittest
import allure
from time import sleep
from config.setup import get_driver
from data.mobile_params import test_account
from utils.find_element import get_element
from mobile.mobile_locator_info import join_continue, invalid_username, already_took_username, logo_page, notification, \
    track, home
from utils.common_mobile import get_new_account
from mobile.mobile_user_actions import Actions


@allure.severity(allure.severity_level.MINOR)
@allure.feature("Username Creation")
class TestAccountCreation(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = get_driver()
        global do
        do = Actions(self.driver)
        new_account = get_new_account()
        do.tap_join()
        sleep(3)
        do.input_email(new_account)
        do.input_password(new_account.password)
        do.tap_complete()
        sleep(10)
        do.not_now()

    def tearDown(self):
        self.driver.quit()

    @allure.story("Create without username")
    def test01_create_without_username(self) -> None:
        do.clear_username()
        do.tap_continue()
        do.assert_element_by_attr(join_continue, 'enabled', 'false', "Can't continue without username")

    @allure.story("Create with username invalid")
    def test02_create_with_username_invalid(self) -> None:
        new_account = get_new_account()
        do.clear_username()
        do.input_username(new_account.invalid_name)
        do.assert_element_by_attr(join_continue, 'enabled', 'false', "Can't continue with username invalid")
        do.assert_element(invalid_username, 'This username is invalid')

    @allure.story("Create with username already took")
    def test03_create_with_username_already_took(self) -> None:
        do.clear_username()
        do.input_username(test_account.already_took_username)
        do.assert_element_by_attr(join_continue, 'enabled', 'true', "Can't continue with username already took")
        do.assert_element(already_took_username, 'This username is already took')
        do.tap_continue()
        try:
            get_element(self.driver, logo_page)
        except:
            print('Continue failed with username already took')

    @allure.story("Create with correct username ")
    def test04_create_with_username_valid(self) -> None:
        new_account = get_new_account()
        do.clear_username()
        do.input_username(new_account.username)
        sleep(3)
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
            get_element(self.driver, notification,3)
            do.set_notification_later()
        except Exception:
            print('already set notification')
        sleep(3)
        do.select_level(new_account.level_index)
        do.tap_continue()
        try:
            get_element(self.driver, track, 3)
            do.tap_continue()
            do.tape_track_with_allow()
        except Exception:
            print("No track notice")
        do.assert_element(home, 'Create success')
