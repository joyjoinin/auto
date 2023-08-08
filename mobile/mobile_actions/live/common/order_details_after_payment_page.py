from utils.find_element import get_element, get_element_by_xpath
from mobile.mobile_locators.live.common.order_details_after_payment_page import back_to_score, \
    contact_fanatics_live


class OrderAfterPaymentActions:

    def __init__(self, driver) -> None:
        self.driver = driver

    def tap_back_to_score(self):
        get_element_by_xpath(self.driver, back_to_score).click()

    def tap_contact_fanatics(self):
        get_element(self.driver, contact_fanatics_live).click()