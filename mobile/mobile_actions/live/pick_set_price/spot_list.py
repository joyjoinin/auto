from utils.find_element import get_element, get_element_by_xpath, get_elements_by_xpath
from mobile.mobile_locators.live.live_page.live_page import live
from mobile.mobile_locators.live.live_page.schedule_page import schedule_title
from mobile.mobile_locators.live.pick_set_price.pick_set_price_page import spot_item
from mobile.mobile_locators.live.pick_set_price.spot_list import *


class SpotListActions:

    def __init__(self, driver) -> None:
        self.driver = driver

    def pick_a_spot(self, number):
        item = spot_item
        item.locator = item.locator + f'[{number}]//XCUIElementTypeButton[last()]'
        get_element_by_xpath(self.driver, item).click()

    def get_spot_name(self, number):
        item = spot_item
        item.locator = item.locator + f'[{number}]//XCUIElementTypeStaticText[last()]'
        return get_element_by_xpath(self.driver, item).get_attribute('value')

    def get_first_spot_name(self):
        first_item_name = LocatorInfo()
        first_item_name.locator = spot_item.locator + '[1]//XCUIElementTypeStaticText[last()]'
        return get_element_by_xpath(self.driver, first_item_name).get_attribute('label')

    def tap_available(self):
        get_element(self.driver, available).click()

    def tap_breaking(self):
        get_element(self.driver, breaking).click()

    def tap_first_spot(self):
        get_element_by_xpath(self.driver, first_item_button).click()

    def tap_spot_automated(self):
        get_elements_by_xpath(self.driver, spot_listing)[0].click()

    def swap_down_list(self,locator,position):
        self.common_swipe_vertical(get_element(self.driver, locator), position)

    def swap_down_spots_listing(self):
        self.swap_down_list(live, 200)

    def swap_down_schedule(self):
        self.swap_down_list(schedule_title, 800)
