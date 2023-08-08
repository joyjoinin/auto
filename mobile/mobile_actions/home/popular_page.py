from utils.find_element import get_element
from typing import NoReturn
from mobile.mobile_locators.live.live_page.live_page import live_name_location


class PopularActions:

    def __init__(self, driver) -> None:
        self.driver = driver
    def tap_live_at_view_all(self, live_name) -> NoReturn:
        target_live = live_name_location
        target_live.locator = live_name
        try:
            get_element(self.driver, target_live).click()
        except:
            print("Can't find live")