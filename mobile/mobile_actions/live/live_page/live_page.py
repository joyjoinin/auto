from utils.find_element import get_element, get_element_by_xpath,get_element_attr_by_xpath
from typing import NoReturn

from mobile.mobile_locators.live.common.listing_sold_out_page import view_schedule
from mobile.mobile_locators.live.live_page.live_page import *
from mobile.mobile_locators.live.pick_set_price.pick_set_price_page import pick_your_spot_button


class LiveActions:

    def __init__(self, driver) -> None:
        self.driver = driver

    def tap_live(self) -> NoReturn:
        get_element_by_xpath(self.driver, first_card_location).click()

    def try_find_live(self, live_name) -> NoReturn:
        live_elem = LocatorInfo('accessibility id', locator=live_name)
        i = 0
        while i < 12:
            target_x = get_element(self.driver, live_elem, 3).location['x']
            if target_x != 50:
                self.swipe_left_card()
                i += 1
            else:
                break

    def pick_your_spot(self):
        get_element(self.driver, pick_your_spot_button).click()

    def get_latest_message(self):
        return get_element_attr_by_xpath(self.driver, latest_message, 'value')

    def input_message_on_live(self,message):
        get_element(self.driver,input_message).send_keys(message)

    def send_message_on_live(self):
        get_element_by_xpath(self.driver,send_message).click()

    def get_error_message_on_live(self):
        return get_element_attr_by_xpath(self.driver,error_message_for_too_long,'value')

    def tap_view_schedule(self):
        get_element(self.driver, view_schedule).click()

    def close_live(self):
        get_element(self.driver, close_live).click()

    def tap_shop(self):
        get_element_by_xpath(self.driver, shop_avatar).click()

    def tap_flag(self):
        get_element(self.driver, flag).click()

    def tap_share(self):
        get_element(self.driver, share).click()

    def tap_schedule(self):
        get_element(self.driver, schedule).click()
