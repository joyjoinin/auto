from utils.find_element import get_element, get_element_by_xpath
from typing import NoReturn
from mobile.mobile_locators.common import back
from mobile.mobile_locators.setting.setting_page import *


class SettingsActions:

    def __init__(self, driver) -> None:
        self.driver = driver

    def tap_logout(self) -> NoReturn:
        get_element(self.driver, logout).click()

    def confirm_logout(self) -> NoReturn:
        get_element(self.driver, logout_confirm).click()

    def tap_my_wallet(self) -> NoReturn:
        get_element_by_xpath(self.driver, my_wallet).click()

    def tap_my_address(self) -> NoReturn:
        get_element(self.driver, my_address).click()

    def tap_back(self) -> NoReturn:
        get_element(self.driver, back).click()

    def tap_purchases(self) -> NoReturn:
        get_element(self.driver, purchases).click()

    def tap_notifications(self) -> NoReturn:
        get_element(self.driver, notifications).click()

    def tap_become_a_seller(self) -> NoReturn:
        get_element(self.driver, become_a_seller).click()

    def tap_contact_us(self) -> NoReturn:
        get_element(self.driver, contact_us).click()

    def tap_FAQs(self) -> NoReturn:
        get_element(self.driver, FAQs).click()

    def tap_setting_privacy_policy(self) -> NoReturn:
        get_element(self.driver, privacy_policy).click()

    def tap_setting_terms_of_use(self) -> NoReturn:
        get_element(self.driver, terms_of_use_on_setting).click()
