from time import sleep
from utils.find_element import get_element
from typing import NoReturn
from mobile.mobile_locators.login.input_username_page import *


class UsernameActions:

    def __init__(self, driver) -> None:
        self.driver = driver

    def save_password(self) -> NoReturn:
        get_element(self.driver, save_psd).click()

    def not_now(self) -> NoReturn:
        get_element(self.driver, not_now).click()

    def input_username(self, name) -> NoReturn:
        get_element(self.driver, username).clear().send_keys(name)

    def clear_username(self) -> NoReturn:
        get_element(self.driver, username).clear()

    def tap_continue(self) -> NoReturn:
        sleep(3)
        get_element(self.driver, join_continue).click()