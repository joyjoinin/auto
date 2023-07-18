import unittest
from time import sleep
from config.setup import get_driver
from data.params import new_account
from utils.find_element import get_element
from utils.locator_info import weak, weak_prompt, complete, fair, good, notification
from utils.save_accounts import save_data
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
        do.close_app()
        self.driver.quit()

    @allure.story("Basic create flow")
    def test01_basic_flow_create_account(self) -> None:
        do.tap_join()
        sleep(3)
        do.input_email(new_account)
        do.input_password(new_account.password)
        do.tap_complete()
        sleep(5)
        save_data(new_account.email,new_account.password)
        do.input_username(new_account.username)
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

    @allure.story("Weak_password creation")
    def test02_create_with_weak_password(self) -> None:
        do.tap_join()
        do.input_email(new_account)
        do.input_password(new_account.weak_password)
        do.assert_element(weak, 'This is weak password')
        do.assert_element(weak_prompt, 'Show prompt success')
        do.assert_element_by_attr(complete, 'enabled', 'false', "Can't complete with weak password")

    @allure.story("Fair_password creation")
    def test03_create_with_fair_password(self) -> None:
        do.tap_join()
        do.input_email(new_account)
        do.input_password(new_account.fair_password)
        do.assert_element(fair, 'This is weak password')
        do.assert_element(weak_prompt, 'Show prompt success')
        do.assert_element_by_attr(complete, 'enabled', 'false', "Can't complete with fair password")

    @allure.story("Good_password creation")
    def test04_create_with_good_password(self) -> None:
        do.tap_join()
        sleep(3)
        do.input_email(new_account)
        do.input_password(new_account.good_password)
        do.assert_element(good, 'This is good password')
        try:
            get_element(self.driver, weak_prompt)
        except Exception:
            print('Not show prompt for good password success')
        do.assert_element_by_attr(complete, 'enabled', 'true', "Can complete with good password")
        do.tap_complete()
        sleep(5)
        save_data(new_account.email, new_account.good_password)
        do.input_username(new_account.username)
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
