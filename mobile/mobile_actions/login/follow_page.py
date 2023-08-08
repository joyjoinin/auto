from utils.find_element import get_element_by_xpath
from typing import NoReturn
from mobile.mobile_locators.login.follow_page import follow, unfollow


class FollowActions:

    def __init__(self, driver) -> None:
        self.driver = driver

    def tap_follow(self, index) -> NoReturn:
        for i in range(1, index + 1):
            get_element_by_xpath(self.driver, follow).click()

    def tap_unfollow(self, index) -> NoReturn:
        for i in range(1, index + 1):
            get_element_by_xpath(self, unfollow).click()