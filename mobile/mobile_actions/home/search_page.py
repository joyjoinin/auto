
from utils.find_element import get_element_by_xpath
from typing import NoReturn
from mobile.mobile_locators.home.search_page import close_search_page


class SearchActions:

    def __init__(self, driver) -> None:
        self.driver = driver

    def close_search_page(self) -> NoReturn:
        get_element_by_xpath(self.driver, close_search_page).click()
