from config.setup import get_driver
from utils.find_element import get_element
from typing import NoReturn
from mobile.mobile_locators.login.login_home_page import login, join


class LoginHomeActions:

    def __init__(self) -> None:
        self.driver = get_driver()

    def tap_login(self) -> NoReturn:
        get_element(self.driver, login).click()

    def tap_join(self) -> NoReturn:
        get_element(self.driver, join).click()