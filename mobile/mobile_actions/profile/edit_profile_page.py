from utils.find_element import get_element, get_element_by_xpath, get_elements_by_xpath
from typing import NoReturn
from mobile.mobile_locators.profile.edit_profile_page import *


class EditProfileActions:

    def __init__(self, driver) -> None:
        self.driver = driver

    def tap_edit_avatar(self) -> NoReturn:
        get_element_by_xpath(self.driver, edit_avatar).click()

    def tap_edit_username(self) -> NoReturn:
        get_element_by_xpath(self.driver, edit_username).click()

    def tap_edit_self_intro(self) -> NoReturn:
        get_element_by_xpath(self.driver, edit_self_intro).click()

    def tap_add_interests(self) -> NoReturn:
        get_element(self.driver, add_interests).click()

    def get_profile_username(self):
        return get_element_by_xpath(self.driver, profile_username).text

    def get_profile_intro(self):
        return get_element_by_xpath(self.driver, profile_self_intro).text

    def get_all_interests(self):
        names = []
        for i in get_elements_by_xpath(self.driver, all_interests):
            names.append(i.text)
        return names

