from utils.find_element import get_element, get_element_by_xpath, get_elements, get_elements_by_xpath
from typing import NoReturn

from mobile.mobile_actions.common.common import CommonActions
from mobile.mobile_actions.live.common.order_details import OrderActions
from mobile.mobile_locators.live.common.order_details import order_total_price, subtotal, shipping, tax, \
    total, gift_name, gift_subtotal


class AssertEleActions:

    def __init__(self, driver) -> None:
        self.driver = driver

    def assert_element(self, locator, message, wait_time=5) -> NoReturn:
        try:
            assert get_element(self.driver, locator, wait_time)
            print('\n{}'.format(message))
        except Exception as e:
            raise e


    def assert_element_by_xpath(self, locator, message, wait_time=5) -> NoReturn:
        try:
            assert get_element_by_xpath(self.driver, locator, wait_time)
            print('\n{}'.format(message))
        except Exception as e:
            raise e


    def assert_elements(self, locator, message, wait_time=5) -> NoReturn:
        try:
            assert get_elements(self.driver, locator, wait_time)
            print('\n{}'.format(message))
        except Exception as e:
            raise e


    def assert_elements_by_xpath(self, locator, message, wait_time=5) -> NoReturn:
        try:
            assert get_elements_by_xpath(self.driver, locator, wait_time)
            print('\n{}'.format(message))
        except Exception as e:
            raise e


    def assert_element_by_attr(self, locator, attr, expected, message, wait_time=5) -> NoReturn:
        try:
            assert get_element(self.driver, locator, wait_time).get_attribute(attr) == expected
            print('\n{}'.format(message))
        except Exception as e:
            raise e


    def assert_element_by_xpath_attr(self, locator, attr, expected, message, wait_time=5) -> NoReturn:
        try:
            assert get_element_by_xpath(self.driver, locator, wait_time).get_attribute(attr) == expected
            print('\n{}'.format(message))
        except Exception as e:
            raise e


    def assert_switch_buttons(self, buttons, expected) -> NoReturn:
        for i in buttons:
            try:
                assert get_element_by_xpath(self.driver, i, 2).get_attribute('value') == expected
                print('\nswitch button success')
            except Exception as e:
                raise e

    def asser_order_detail(self, spot_name, spot_price) -> NoReturn:
        price_action = CommonActions(self.driver)
        page_action = OrderActions(self.driver)
        page_action.open_summary()
        order_price = price_action.get_price(order_total_price)
        subtotal_price = price_action.get_price(subtotal)
        shipping_price = price_action.get_price(shipping)
        tax_price = price_action.get_price(tax)
        total_price = price_action.get_price(total)
        order_spot_name = price_action.get_attr_xpath(gift_name, 'label')
        spot_subtotal = price_action.get_price(gift_subtotal)
        assert spot_name == order_spot_name
        assert order_price == total_price
        assert spot_subtotal == subtotal_price == spot_price
        assert total_price == shipping_price + subtotal_price + tax_price
        page_action.pay_now()