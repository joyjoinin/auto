from utils.find_element import get_element
from typing import NoReturn
from mobile.mobile_locators.login.notification_page import *


class NotificationActions:

    def __init__(self, driver) -> None:
        self.driver = driver

    def set_notification(self) -> NoReturn:
        get_element(self.driver, notification).click()

    def set_notification_later(self) -> NoReturn:
        get_element(self.driver, notification_later).click()

    def allow_notification(self) -> NoReturn:
        get_element(self.driver, notification_allow).click()

    def not_allow_notification(self) -> NoReturn:
        get_element(self.driver, notification_no_allow).click()