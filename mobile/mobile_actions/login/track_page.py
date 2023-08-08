from utils.find_element import get_element
from typing import NoReturn
from mobile.mobile_locators.login.track_page import *
from mobile.mobile_actions.home.home_page import HomeActions


class TrackAction:

    def __init__(self, driver) -> None:
        self.driver = driver

    def tape_track_with_allow(self) -> NoReturn:
        try:
            get_element(self.driver, track).click()
            get_element(self.driver, track_continue).click()
            get_element(self.driver, track_allow).click()
        except Exception as e:
            raise e
        finally:
            HomeActions(self.driver).tap_home()
