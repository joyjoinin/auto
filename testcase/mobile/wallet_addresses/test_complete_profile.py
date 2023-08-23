import unittest
import allure
from time import sleep
from config.setup import get_driver
from data.mobile_params import card_info, address_info
from utils.find_element import get_element
from utils.mobile.locator_info import notification, home
from utils.mobile.common import get_new_account
from utils.mobile.user_actions import Actions


@allure.severity(allure.severity_level.CRITICAL)
@allure.feature("Complete wallet addresses")
class TestCard(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = get_driver()
        global do
        do = Actions(self.driver)
    def tearDown(self):
        self.driver.quit()

    @allure.story("Complete wallet addresses")
    def test1_complete_profile(self) -> None:
        new_account = get_new_account()
        do.tap_join()
        sleep(3)
        do.input_email(new_account)
        do.input_password(new_account.password)
        do.tap_complete()
        do.not_now()
        do.input_username(new_account.username)
        sleep(10)
        do.tap_continue()
        sleep(3)
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
        do.tap_complete_profile()
        do.add_card_flow(card_info)
        sleep(3)
        do.add_address_flow(address_info)
        '''miss assert tooltip for complete'''
        do.assert_element(home, 'Complete success')
