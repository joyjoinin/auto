from time import sleep
from utils.find_element import get_element, get_element_by_xpath
from typing import NoReturn
from mobile.mobile_locators.profile.edit_username_page import *


class EditUsernameActions:

    def __init__(self, driver) -> None:
        self.driver = driver

    def input_new_username(self, new_username) -> NoReturn:
        sleep(1)
        get_element(self.driver, username_input_box).clear().send_keys(new_username)

    def tap_save_username(self) -> NoReturn:
        get_element_by_xpath(self.driver, save_username).click()