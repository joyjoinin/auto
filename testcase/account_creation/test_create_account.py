import allure
import unittest
from time import sleep
from config.setup import get_driver
from data.mobile_params import test_account
from mobile.mobile_user_actions import Actions
from utils.find_element import get_element
from mobile.mobile_locator_info import weak, weak_prompt, complete, fair, good, notification, login, already_in_use, track, home
from utils.common_mobile import get_new_account

@allure.severity(allure.severity_level.CRITICAL)
@allure.feature("Account Creation")
class TestAccountCreation(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = get_driver()
        global do
        do = Actions(self.driver)

    def tearDown(self):
        self.driver.quit()

    @allure.story("Basic create flow")
    def test01_basic_flow_create_account(self) -> None:
        new_account = get_new_account()
        do.assert_element(login, 'start from login page')
        do.tap_join()
        sleep(3)
        do.input_email(new_account)
        do.input_password(new_account.password)
        do.tap_complete()
        do.not_now()
        do.input_username(new_account.username)
        sleep(5)
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
            get_element(self.driver, notification, 3)
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

    @allure.story("Weak_password creation")
    def test02_create_with_weak_password(self) -> None:
        new_account = get_new_account()
        do.tap_join()
        do.input_email(new_account)
        do.input_password(new_account.weak_password)
        do.assert_element(weak, 'This is weak password')
        do.assert_element(weak_prompt, 'Show prompt success')
        do.assert_element_by_attr(complete, 'enabled', 'false', "Can't complete with weak password")

    @allure.story("Fair_password creation")
    def test03_create_with_fair_password(self) -> None:
        new_account = get_new_account()
        do.tap_join()
        do.input_email(new_account)
        do.input_password(new_account.fair_password)
        do.assert_element(fair, 'This is fair password')
        do.assert_element(weak_prompt, 'Show prompt success')
        do.assert_element_by_attr(complete, 'enabled', 'false', "Can't complete with fair password")

    @allure.story("Good_password creation")
    def test04_create_with_good_password(self) -> None:
        new_account = get_new_account()
        do.tap_join()
        sleep(3)
        do.input_email(new_account)
        do.input_password(new_account.good_password)
        do.assert_element(good, 'This is good password')
        try:
            get_element(self.driver, weak_prompt, 3)
        except Exception:
            print('Not show prompt for good password success')
        do.assert_element_by_attr(complete, 'enabled', 'true', "Can complete with good password")
        do.tap_complete()
        sleep(10)
        do.not_now()
        do.tap_continue()
        # sleep(3)
        # do.tap_enter_access_code()
        # sleep(3)
        # do.input_code(new_account.access_code)
        # do.tap_submit()
        do.tap_logos(new_account.logo_select)
        do.tap_continue()
        do.tap_follow(new_account.follow_count)
        do.tap_continue()
        try:
            get_element(self.driver, notification)
            do.set_notification_later()
        except Exception:
            print('already set notification')
        do.select_level(new_account.level_index)
        do.tap_continue()
        try:
            get_element(self.driver, track, 3)
            do.tap_continue()
            do.tape_track_with_allow()
        except Exception:
            print("No track notice")
        do.assert_element(home, 'Create success')

    @allure.story("Email already took")
    def test05_create_with_email_already_took(self) -> None:
        new_account = get_new_account()
        do.tap_join()
        sleep(3)
        do.input_email(test_account)
        do.input_password(new_account.good_password)
        do.tap_complete()
        do.assert_element(already_in_use, 'create failed by email already took')

