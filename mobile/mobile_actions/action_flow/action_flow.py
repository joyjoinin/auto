from time import sleep
from data.params import test_account
from typing import NoReturn
from mobile.mobile_actions.home.home_page import HomeActions
from mobile.mobile_actions.login.login_home_page import LoginHomeActions
from mobile.mobile_actions.login.login_page import LoginActions
from mobile.mobile_actions.profile.profile_page import ProfileActions
from mobile.mobile_actions.setting.address_page.address_page import AddressActions
from mobile.mobile_actions.setting.notification_page.notifications_page import NotificationsActions
from mobile.mobile_actions.setting.setting_page import SettingsActions
from mobile.mobile_actions.setting.wallet_page.wallet_page import WalletPageActions
from mobile.mobile_locators.home.home_page import home
from mobile.mobile_locators.login.login_home_page import login
from mobile.mobile_actions.common.assert_actions import AssertEleActions


class FlowActions:

    def __init__(self, driver) -> None:
        self.driver = driver
    def add_card_flow(self, card_info) -> NoReturn:
        actions = WalletPageActions(self.driver)
        actions.input_card(card_info.card)
        actions.input_expiration_date(card_info.date)
        actions.input_cvc(card_info.cvc)
        actions.select_country(card_info.country)
        actions.input_zip(card_info.zip_number)
        actions.set_up()


    def add_address_flow(self, address_info) -> NoReturn:
        actions = AddressActions(self.driver)
        actions.input_firstname(address_info.firstname)
        actions.input_lastname(address_info.lastname)
        actions.input_address(address_info.address)
        actions.input_zip_code(address_info.code)
        actions.input_city(address_info.city)
        actions.input_state(state_text=address_info.state)
        actions.save_address()

    def logout_flow(self) -> NoReturn:
        logout_actions = SettingsActions(self.driver)
        assert_action = AssertEleActions(self.driver)
        tap_profile = HomeActions(self.driver)
        tap_setting = ProfileActions(self.driver)
        sleep(5)
        tap_profile.tap_profile()
        tap_setting.tap_setting()
        logout_actions.tap_logout()
        logout_actions.confirm_logout()
        assert_action.assert_element(login, 'success log out')

    def login_flow(self, account) -> NoReturn:
        login_actions = LoginActions(self.driver)
        tap_login = LoginHomeActions(self.driver)
        assert_action = AssertEleActions(self.driver)
        tap_login.tap_login()
        login_actions.input_email(account)
        login_actions.tap_next()
        login_actions.input_password(account.password)
        login_actions.tap_fanatics_id()
        assert_action.assert_element(home, 'success login')

    def tap_notifications_flow(self, notification_type, buttons, expected, message):
        actions = NotificationsActions(self.driver)
        sleep(5)
        actions.tap_notification_type(notification_type)
        actions.tap_switch_button(
            buttons)
        actions.tap_back_to_notifications()
        actions.tap_notification_type(notification_type)
        assert_action = AssertEleActions(self.driver)
        assert_action.assert_switch_buttons(
            buttons, expected)
        print(message)
        actions.tap_back_to_notifications()

    def get_to_settings(self):
        self.login_flow(test_account)
        tap_profile = HomeActions(self.driver)
        tap_setting = ProfileActions(self.driver)
        tap_profile.tap_profile()
        tap_setting.tap_setting()