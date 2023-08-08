
from utils.find_element import get_element
from mobile.mobile_locators.live.common.after_payment_page import return_to_stream, view_order_details


class ScoreActions:

    def __init__(self, driver) -> None:
        self.driver = driver

    def tap_return_to_stream(self):
        get_element(self.driver, return_to_stream).click()

    def tap_view_order_details(self):
        get_element(self.driver, view_order_details).click()

