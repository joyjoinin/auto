from time import sleep
from utils.find_element import get_element, get_element_by_xpath
from mobile.mobile_locators.live.common.order_details import cancel_order, nav_arrow_down, nav_arrow_up, \
    change_card, change_address, pay_now


class OrderActions:

    def __init__(self, driver) -> None:
        self.driver = driver

    def cancel_pay(self):
        get_element_by_xpath(self.driver, cancel_order).click()

    def open_summary(self):
        sleep(2)
        get_element(self.driver, nav_arrow_down).click()

    def close_summary(self):
        get_element(self.driver, nav_arrow_up).click()

    def change_method(self):
        get_element_by_xpath(self.driver, change_card).click()

    def change_address(self):
        get_element_by_xpath(self.driver, change_address).click()

    def pay_now(self):
        get_element_by_xpath(self.driver, pay_now).click()
