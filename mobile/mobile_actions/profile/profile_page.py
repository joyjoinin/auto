from utils.find_element import get_element, get_elements
from typing import NoReturn
from mobile.mobile_locators.profile.profile_page import *


class ProfileActions:

    def __init__(self, driver) -> None:
        self.driver = driver

    def tap_setting(self) -> NoReturn:
        get_element(self.driver, setting).click()

    def tap_edit_profile(self) -> NoReturn:
        get_element(self.driver, edit_profile).click()

    def tap_invite_friends(self) -> NoReturn:
        get_element(self.driver, invite_friends).click()

    def tap_share_profile(self) -> NoReturn:
        get_element(self.driver, share_profile).click()

    def tap_profile_followers(self) -> NoReturn:
        get_element(self.driver, profile_followers).click()

    def tap_profile_following(self) -> NoReturn:
        get_element(self.driver, profile_following).click()

    def tap_favorite_shop(self) -> NoReturn:
        get_elements(self.driver, favorite_shops).click()