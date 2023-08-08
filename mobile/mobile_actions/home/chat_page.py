from utils.find_element import get_element, get_element_by_xpath
from typing import NoReturn

from mobile.mobile_locators.home.chat_page import add_chat, cancel_add_message, clear_message_search_bar, \
    message_search_bar


class ChatActions:

    def __init__(self, driver) -> None:
        self.driver = driver

    def tap_add_chat(self) -> NoReturn:
        get_element_by_xpath(self.driver, add_chat).click()

    def cancel_add_message(self) -> NoReturn:
        get_element(self.driver, cancel_add_message).click()

    def clear_message_search_bar(self) -> NoReturn:
        get_element_by_xpath(self.driver, clear_message_search_bar).click()

    def input_on_message_search_bar(self, search_item) -> NoReturn:
        get_element(self.driver, message_search_bar).clear().send_keys(search_item)