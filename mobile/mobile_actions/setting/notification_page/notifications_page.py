from utils.find_element import get_element, get_element_by_xpath
from mobile.mobile_locators.setting.notification_page.live_streams_page import back_to_notifications


class NotificationsActions:

    def __init__(self, driver) -> None:
        self.driver = driver

    def tap_notification_type(self, notification_type):
        get_element(self.driver, notification_type).click()

    def tap_switch_button(self, buttons):
        for i in buttons:
            try:
                get_element_by_xpath(self.driver, i).click()
            except Exception as e:
                raise e

    def tap_back_to_notifications(self):
        get_element(self.driver, back_to_notifications).click()