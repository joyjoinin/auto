import re
from utils.find_element import get_element, get_element_by_xpath
from appium.webdriver.common.touch_action import TouchAction
from mobile.mobile_locators.live.common.common import spots_remain
from mobile.mobile_locators.live.random_set_price.random_set_price_page import *


class RandomSetPriceActions:

    def __init__(self, driver) -> None:
        self.driver = driver

    def decrease_spot(self):
        target = get_element(self.driver,spots_value_button)
        text_location = target.location
        text_size = target.size
        target_y = text_location['y'] + text_size['height'] / 2
        target_x = text_location['x'] + text_size['width'] / 8
        touch_action = TouchAction(self.driver)
        touch_action.tap(x=target_x, y=target_y).perform()

    def increase_spot(self):
        target = get_element(self.driver,spots_value_button)
        text_location = target.location
        text_size = target.size
        target_y = text_location['y'] + text_size['height'] / 2
        target_x = text_location['x'] + text_size['width'] * 7 / 8
        touch_action = TouchAction(self.driver)
        touch_action.tap(x=target_x, y=target_y).perform()

    def get_single_price(self):
        string = get_attr_xpath(spot_price, 'value')
        pattern = r'\d+'
        matches = re.findall(pattern, string)
        if matches:
            number = int(''.join(matches))
            return float('{:.2f}'.format(number))

    def get_buy_spots_num(self):
        string = get_attr_xpath(buy_spots_button,'label')
        pattern = r'\d+'
        matches = re.findall(pattern, string)
        if matches:
            number = int(matches[0])
            return number

    def tap_to_buy(self):
        get_element_by_xpath(self.driver,buy_spots_button).click()

    def get_all_spots_num(self):
        string = self.get_attr_xpath(spots_remain,'label')
        pattern = r'\d+'
        matches = re.findall(pattern, string)
        if len(matches) >= 2:
            all_num = int(matches[0])
            remain_num = int(matches[1])
            return [all_num, remain_num]
