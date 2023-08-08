from utils.find_element import get_element
from typing import NoReturn
from mobile.mobile_locators.profile.share_page import close_share_frame


class ShareActions:

    def __init__(self, driver) -> None:
        self.driver = driver

    def tap_close_share(self) -> NoReturn:
        get_element(self.driver, close_share_frame).click()