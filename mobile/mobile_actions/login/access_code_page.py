from time import sleep
from utils.find_element import get_element
from typing import NoReturn
from mobile.mobile_locators.common import submit
from mobile.mobile_locators.login.access_code_page import access_code_input


class CodeActions:

    def __init__(self, driver) -> None:
        self.driver = driver

    def input_code(self, code) -> NoReturn:
        sleep(3)
        get_element(self.driver, access_code_input).send_keys(code)

    def tap_submit(self) -> NoReturn:
        sleep(3)
        get_element(self.driver, submit).click()