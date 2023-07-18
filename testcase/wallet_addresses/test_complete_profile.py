import unittest
import allure
from time import sleep
from config.setup import get_driver
from data.params import card_info, new_account, address_info
from utils.find_element import get_element
from utils.locator_info import notification, home
from utils.save_accounts import save_data
from utils.user_actions import Actions


@allure.feature("Complete wallet_addresses")
class TestCard(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = get_driver()
        global do
        do = Actions(self.driver)

    def tearDown(self):
        self.driver.quit()

    @allure.story("Complete wallet_addresses")
    def test1_comlete_profile(self) -> None:
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
        do.tap_complete_profile()
        do.add_card_flow(card_info)
        sleep(3)
        do.add_address_flow(address_info)
        '''miss assert tooltip for complete'''
        do.assert_element(home, 'Complete success')
