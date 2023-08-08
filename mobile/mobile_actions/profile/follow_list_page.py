from utils.find_element import get_element, get_element_by_xpath
from typing import NoReturn
from mobile.mobile_locators.profile.follow_list_page import following_list_title, followers_list_title
from mobile.mobile_locators.profile.profile_page import *


class FollowActions:

    def __init__(self, driver) -> None:
        self.driver = driver

    def tap_following_in_profile(self) -> NoReturn:
        get_element(self.driver, profile_following).click()

    def tap_followers_in_profile(self) -> NoReturn:
        get_element(self.driver, profile_followers).click()

    def tap_following_list(self) -> NoReturn:
        get_element_by_xpath(self.driver, following_list_title).click()

    def tap_followers_list(self) -> NoReturn:
        get_element_by_xpath(self.driver, followers_list_title).click()