from utils.find_element import get_element
from typing import NoReturn
from mobile.mobile_locators.login.login_page import *


class LoginActions:

    def __init__(self, driver) -> None:
        self.driver = driver
    def input_email(self, account) -> NoReturn:
        get_element(self.driver, email).clear().send_keys(account.email)

    def clear_email(self) -> NoReturn:
        get_element(self.driver, email).clear()

    def tap_next(self) -> NoReturn:
        get_element(self.driver, login_next).click()

    def input_password(self, password_type) -> NoReturn:
        get_element(self.driver, password).clear().send_keys(password_type)

    def tap_fanatics_id(self) -> NoReturn:
        get_element(self.driver, fanaticsID).click()

    def tap_not_you(self) -> NoReturn:
        get_element(self.driver, not_you).click()

    def tap_show_password(self) -> NoReturn:
        get_element(self.driver, show_password).click()

    def tap_hide_password(self) -> NoReturn:
        get_element(self.driver, hide_password).click()

    def tap_forget_password(self) -> NoReturn:
        get_element(self.driver, forget_password).click()

    def tap_privacy_policy(self) -> NoReturn:
        get_element(self.driver, terms_of_use).click()

    def tap_create_new_one(self) -> NoReturn:
        get_element(self.driver, create_one_now).click()

    def tap_complete(self) -> NoReturn:
        get_element(self.driver, complete).click()
