import unittest
import allure
from time import sleep
from config.setup import get_driver
from data.params import card_info, address_info
from utils.find_element import get_element
from utils.locator_info import notification, home, login
from utils.help_function import save_data, get_new_account
from utils.user_actions import Actions


@allure.severity(allure.severity_level.CRITICAL)
@allure.feature("Complete wallet addresses")
class TestCard(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = get_driver()
        global do
        do = Actions(self.driver)
        do.open_app()

    def tearDown(self):
        self.driver.quit()

    @allure.story("Complete wallet addresses")
    def test1_complete_profile(self) -> None:
        retry = False
        new_account = get_new_account()
        try:
            do.assert_element(login, 'start from login page')
        except Exception:
            do.retry_for_failed_in_creation(new_account)
            retry = True
        if retry is False:
            do.tap_join()
            sleep(3)
            do.input_email(new_account)
            do.input_password(new_account.password)
            # save_data(new_account.email, new_account.password)
            do.tap_complete()
            # do.input_username(new_account.username)
            sleep(10)
            do.tap_continue()
            try:
                get_element(self.driver, notification)
                do.set_notification_later()
            except Exception:
                print('already set notification')
            sleep(3)
            do.tap_enter_access_code()
            sleep(3)
            do.input_code(new_account.access_code)
            do.tap_submit()
            do.tap_logos(new_account.logo_select)
            do.tap_continue()
            do.tap_follow(new_account.follow_count)
            do.tap_continue()
            do.select_level(new_account.level_index)
            do.tap_continue()
        do.tap_complete_profile()
        do.add_card_flow(card_info)
        sleep(3)
        do.add_address_flow(address_info)
        '''miss assert tooltip for complete'''
        do.assert_element(home, 'Complete success')