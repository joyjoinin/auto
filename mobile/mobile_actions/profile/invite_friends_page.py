from utils.find_element import get_element
from typing import NoReturn
from mobile.mobile_locators.profile.invite_friends_page import *
from mobile.mobile_locators.profile.profile_page import *


class InviteActions:

    def __init__(self, driver) -> None:
        self.driver = driver

    def tap_invite_friends_on_profile(self) -> NoReturn:
        get_element(self.driver, invite_friends).click()

    def tap_send_invite(self) -> NoReturn:
        get_element(self.driver, send_invite).click()

    def tap_cancel_invite(self) -> NoReturn:
        get_element(self.driver, cancel_invite).click()

    def tap_close_invite(self) -> NoReturn:
        get_element(self.driver, close_invite_pop).click()
