from utils.find_element import get_element, get_element_by_xpath,get_elements_by_xpath
from typing import NoReturn
from mobile.mobile_locators.setting.address_page.address_list_page import *


class AddressListActions:

    def __init__(self, driver) -> None:
        self.driver = driver

    def tap_add_shipping(self) -> NoReturn:
        get_element(self.driver, add_address).click()

    def find_address_items(self):
        items = get_elements_by_xpath(self.driver, address_item)
        address_list = []
        for i in items:
            address_label = i.get_attribute('label')
            if address_label is not None:
                address_list.append(address_label)
        return address_list

    def cancel_add_address(self) -> NoReturn:
        get_element_by_xpath(self.driver, cancel_add_address)

    def delete_address(self) -> NoReturn:
        get_element_by_xpath(self.driver, delete_address).click()

    def confirm_delete_address(self) -> NoReturn:
        get_element(self.driver, confirm_delete_address).click()

    def cancel_delete_address(self) -> NoReturn:
        get_element(self.driver, cancel_delete_address).click()

    def back_to_setting(self) -> NoReturn:
        get_element(self.driver, back_to_setting).click()