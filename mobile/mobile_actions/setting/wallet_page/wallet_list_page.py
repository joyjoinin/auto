from utils.find_element import get_element, get_element_by_xpath,get_elements_by_xpath
from typing import NoReturn
from mobile.mobile_locators.setting.wallet_page.wallet_list_page import *


class WalletListActions:

    def __init__(self, driver) -> None:
        self.driver = driver

    def tap_add_card(self) -> NoReturn:
        get_element_by_xpath(self.driver, add_wallet).click()

    def get_wallet_list(self):
        items = get_elements_by_xpath(self.driver, wallet_list)
        wallet_items = []
        for i in items:
            item = i.get_attribute('UID')
            if item is not None:
                wallet_items.append(item)
        return wallet_items

    def edit_card_list(self) -> NoReturn:
        get_element(self.driver, edit_card).click()

    def delete_card(self) -> NoReturn:
        get_element_by_xpath(self.driver, delete_card).click()

    def confirm_delete_card(self) -> NoReturn:
        get_element_by_xpath(self.driver, confirm_delete_card).click()

    def cancel_delete_card(self) -> NoReturn:
        get_element(self.driver, cancel_delete_card).click()

    def tap_done_edit_card(self) -> NoReturn:
        get_element(self.driver, done_edit_card).click()

    def tap_card_set_up(self) -> NoReturn:
        get_element(self.driver, card_set_up).click()
