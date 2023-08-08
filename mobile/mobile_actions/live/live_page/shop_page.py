from utils.find_element import get_element, get_element_by_xpath
from mobile.mobile_locators.live.live_page.shop_page import *


class ShopActions:

    def __init__(self, driver) -> None:
        self.driver = driver

    def swap_down_shop_page(self):
        self.common_swipe_vertical(get_element_by_xpath(self.driver,avatar_in_shop), 800)

    def tap_follow_shop_page(self):
        get_element(self.driver,follow_shop).click()

    def tap_unfollow_shop_page(self):
        get_element(self.driver,unfollow_shop).click()

    def tap_report_shop_page(self):
        get_element_by_xpath(self.driver,report_in_shop).click()