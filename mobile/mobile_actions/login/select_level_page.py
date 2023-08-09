from data.mobile_params import level_params
from utils.find_element import get_element
from mobile.mobile_locators.login.select_level_page import level


class LevelActions:

    def __init__(self, driver) -> None:
        self.driver = driver

    def select_level(self, index):
        level.locator = level_params[index - 1]
        get_element(self.driver, level).click()