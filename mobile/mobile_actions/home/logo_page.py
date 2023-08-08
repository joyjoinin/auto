from utils.find_element import get_element, get_elements_by_xpath
from typing import NoReturn

from mobile.mobile_locators.home.home_page import recommend_shops_to_follow, \
    recommend_shops_already_following
from mobile.mobile_locators.home.logo_page import logo_item


class LogoActions:

    def __init__(self, driver) -> None:
        self.driver = driver

    def logo_scroll_left(self):
        self.common_swipe_horizontal(self.get_log_scroll_view(), -80)

    def logo_scroll_right(self):
        self.common_swipe_horizontal(self.get_log_scroll_view(), 80)

    def tap_logo(self, logo_name) -> NoReturn:
        logo_item.locator = logo_name
        get_element(self.driver, logo_item).click()

    def get_recommend_follow_buttons(self):
        return get_elements_by_xpath(self.driver, recommend_shops_to_follow)

    def get_recommend_following_buttons(self):
        return get_elements_by_xpath(self.driver, recommend_shops_already_following)
