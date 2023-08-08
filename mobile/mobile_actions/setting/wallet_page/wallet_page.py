from utils.find_element import get_element, get_element_by_xpath
from typing import NoReturn
from appium.webdriver.common.touch_action import TouchAction
from mobile.mobile_locators.setting.address_page.address_page import state_value, state_done
from mobile.mobile_locators.setting.wallet_page.wallet_page import *


class WalletPageActions:

    def __init__(self, driver) -> None:
        self.driver = driver

    def exit_add_payment(self) -> NoReturn:
        get_element(self.driver, exit_add_payment).click()

    def input_card(self, card) -> NoReturn:
        get_element(self.driver, card_number).send_keys(card)

    def input_expiration_date(self, date) -> NoReturn:
        get_element(self.driver, expiration_date).send_keys(date)

    def input_cvc(self, cvc_number) -> NoReturn:
        get_element(self.driver, cvc).send_keys(cvc_number)

    def search_country(self, icon_chevron_down) -> NoReturn:
        get_element_by_xpath(self.driver, icon_chevron_down).click()

    def swipe_up_country(self):
        actions = TouchAction(self.driver)
        actions.press(x=215, y=815).wait(200).move_to(x=215, y=778)
        actions.release().perform()

    def swipe_down_country(self):
        actions = TouchAction(self.driver)
        actions.press(x=215, y=815).wait(200).move_to(x=215, y=845)
        actions.release().perform()

    # United States default, don't need to select others
    def select_country(self, country) -> NoReturn:
        self.search_country(country_list)
        is_sequential_search = True
        while True:
            try:
                value = get_element(self.driver, state_value).get_attribute('value')
                if country in value:
                    get_element(self.driver, state_done).click()
                    break
                if 'Afghanistan' in value:
                    print('Not find Country')
                    break
                if is_sequential_search:
                    self.swipe_up_country()
                    value = get_element(self.driver, state_value).get_attribute('value')
                    if 'Zimbabwe' in value:
                        is_sequential_search = False
                else:
                    self.swipe_down_country()
            except Exception:
                raise

    def input_zip(self, number) -> NoReturn:
        get_element(self.driver, zip_number).send_keys(number)

    def set_up(self) -> NoReturn:
        get_element(self.driver, set_up).click()
