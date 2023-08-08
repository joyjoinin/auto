import random
from time import sleep
from data.params import Logos
from utils.find_element import get_element
from mobile.mobile_locators.login.collect_page import logo


class CollectActions:

    def __init__(self, driver) -> None:
        self.driver = driver

    def tap_logos(self, logo_selected):
        sleep(3)
        i = 0
        logo_list = Logos
        tap_list = []
        while i < logo_selected:
            logo.locator = logo_list[random.randint(0, 11)]
            get_element(self.driver, logo).click()
            tap_list.append(logo.locator)
            i += 1
        return tap_list
