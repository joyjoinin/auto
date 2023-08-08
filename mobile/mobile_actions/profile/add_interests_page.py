from utils.find_element import get_element
from typing import NoReturn
from mobile.mobile_locators.profile.add_interests_page import back_to_edit_page


class InterestsActions:

    def __init__(self, driver) -> None:
        self.driver = driver

    def tap_back_to_edit_page(self) -> NoReturn:
        get_element(self.driver, back_to_edit_page).click()