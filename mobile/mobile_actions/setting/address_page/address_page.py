from time import sleep
from utils.find_element import get_element, get_element_by_xpath
from typing import NoReturn
from appium.webdriver.common.touch_action import TouchAction
from mobile.mobile_locators.setting.address_page.address_page import *


class AddressActions:

    def __init__(self, driver) -> None:
        self.driver = driver

    def input_firstname(self, first_name) -> NoReturn:
        sleep(1)
        get_element_by_xpath(self.driver, firstname).clear().send_keys(first_name)

    def input_lastname(self, last_name) -> NoReturn:
        sleep(1)
        get_element_by_xpath(self.driver, lastname).clear().send_keys(last_name)

    def input_address(self, address_text) -> NoReturn:
        sleep(1)
        get_element_by_xpath(self.driver, address).clear().send_keys(address_text)

    def input_apartment_etc(self, apartment_etc) -> NoReturn:
        sleep(1)
        get_element_by_xpath(self.driver, apartment).clear().send_keys(apartment_etc)

    def input_zip_code(self, code) -> NoReturn:
        sleep(1)
        get_element_by_xpath(self.driver, zip_code).clear().send_keys(code)

    def input_city(self, city_text) -> NoReturn:
        sleep(1)
        get_element_by_xpath(self.driver, city).clear().send_keys(city_text)

    def input_phone(self, phone_number) -> NoReturn:
        sleep(1)
        get_element_by_xpath(self.driver, phone).clear().send_keys(phone_number)

    def input_state(self, state_text) -> NoReturn:
        get_element_by_xpath(self.driver, state).click()
        is_find = False
        while is_find is not True:
            try:
                actions = TouchAction(self.driver)
                actions.press(x=217, y=815).wait(200).move_to(x=216, y=778)
                actions.release().perform()
                value = get_element(self.driver, state_value, 5).get_attribute('value')
                if value == state_text:
                    is_find = True
            except Exception as e:
                raise e
        get_element(self.driver, state_done).click()

    def save_address(self) -> NoReturn:
        get_element(self.driver, save_address).click()
