from time import sleep
from utils.find_element import get_element, get_element_by_xpath
from typing import NoReturn

from mobile.mobile_locators.profile.edit_intro_page import *


class IntroActions:

    def __init__(self, driver) -> None:
        self.driver = driver

    def input_new_intro(self, new_intro) -> NoReturn:
        sleep(1)
        get_element(self.driver, intro_text_field).clear().send_keys(new_intro)

    def tap_save_intro(self) -> NoReturn:
        get_element_by_xpath(self.driver, save_intro).click()