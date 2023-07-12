from utils.find_element import get_element, get_element_by_xpath
from typing import NoReturn
from appium.webdriver.common.touch_action import TouchAction
from utils.locator_info import *


class Actions:

    def __init__(self, driver) -> None:
        self.driver = driver

    def tap_login(self) -> NoReturn:
        get_element(self.driver, login).click()

    def input_email(self) -> NoReturn:
        get_element(self.driver, email).send_keys('joy009@fanatics.live')

    def clear_email(self) -> NoReturn:
        get_element(self.driver, email).clear()

    def tap_next(self) -> NoReturn:
        get_element(self.driver, login_next).click()

    def input_password(self) -> NoReturn:
        get_element(self.driver, password).send_keys('Joytest159753?')

    def tap_fanatics_id(self) -> NoReturn:
        get_element(self.driver, fanaticsID).click()

    def tape_track_with_allow(self) -> NoReturn:
        try:
            get_element(self.driver, track)
            get_element(self.driver, track_continue).click()
            get_element(self.driver, track_allow).click()
        except Exception as e:
            raise e

    def tap_profile(self) -> NoReturn:
        get_element(self.driver, profile).click()

    def tap_setting(self) -> NoReturn:
        get_element(self.driver, setting).click()

    def tap_logout(self) -> NoReturn:
        get_element(self.driver, logout).click()

    def confirm_logout(self) -> NoReturn:
        get_element(self.driver, logout_confirm).click()

    def assert_element(self, locator, message) -> NoReturn:
        try:
            assert get_element(self.driver, locator)
            print(message)
        except Exception as e:
            raise e

    def tap_join(self) -> NoReturn:
        get_element(self.driver,join).click()

    def tap_complete(self) -> NoReturn:
        get_element(self.driver, complete).click()

    def input_username(self) -> NoReturn:
        get_element(self.driver, username).send_keys('joy100')

    def tap_continue(self) -> NoReturn:
        get_element(self.driver, join_continue).click()

    def set_notification(self) -> NoReturn:
        get_element(self.driver, notification).click()

    def set_notification_later(self) -> NoReturn:
        get_element(self.driver, notification_later).click()

    def allow_notification(self) -> NoReturn:
        get_element(self.driver, notification_allow).click()

    def not_allow_notification(self) -> NoReturn:
        get_element(self.driver, notification_no_allow).click()

    def tap_invite_your_friends(self) -> NoReturn:
        get_element(self.driver, invite).click()

    def tap_enter_access_code(self) -> NoReturn:
        get_element(self.driver, access_code).click()

    def tap_wait_list_play_button(self) -> NoReturn:
        get_element(self.driver, play_button).click()

    def tap_user_avatar(self, initial) -> NoReturn:
        avatar.locator = initial
        get_element(self.driver, avatar).click()

    def input_code(self, code) -> NoReturn:
        get_element(self.driver, access_code_input).send_keys(code)

    def tap_submit(self) -> NoReturn:
        get_element(self.driver, submit).click()

    def tap_logos(self, logo_selected) -> NoReturn:
        logo.locator = logo_selected
        get_element(self.driver, logo).click()

    def tap_follow(self, index) -> NoReturn:
        if index:
            for i in index:
                get_element_by_xpath(self, follow % i).click()

    def tap_unfollow(self, index) -> NoReturn:
        if index:
            for i in index:
                get_element_by_xpath(self, unfollow % i).click()

    def select_level(self, index) -> NoReturn:
        get_element_by_xpath(self, level % index).click()

    def tap_complete_profile(self) -> NoReturn:
        get_element(self.driver, complete_profile).click()

    def tap_close_complete_profile(self) -> NoReturn:
        get_element(self.driver,close_complete_profile).click()

    def tap_view_all(self) -> NoReturn:
        get_element(self.driver, view_all).click()

    def exit_add_payment(self) -> NoReturn:
        get_element(self.driver, exit_add_payment).click()

    def input_card(self, card) -> NoReturn:
        get_element(self.driver, card_number).send_keys(card)

    def input_expiration_date(self, date) -> NoReturn:
        get_element(self.driver, expiration_date).send_keys(date)

    def input_cvc(self, cvc_number) -> NoReturn:
        get_element(self.driver, cvc).send_keys(cvc_number)

    # United States default, don't need to select others
    def select_country(self) -> NoReturn:
        get_element(self.driver, country_done).click()

    def input_zip(self, number) -> NoReturn:
        get_element(self.driver, zip_number).send_keys(number)

    def set_up(self) -> NoReturn:
        get_element(self.driver, set_up).click()

    def add_card_flow(self, card_info) -> NoReturn:
        self.input_card(card_info['card'])
        self.input_expiration_date(card_info['date'])
        self.input_cvc(card_info['cvc'])
        self.select_country()
        self.input_zip(card_info['zip_number'])
        self.set_up()

    def input_firstname(self, first_name) -> NoReturn:
        get_element_by_xpath(self.driver, firstname).clear().send_keys(first_name)

    def input_lastname(self, last_name) -> NoReturn:
        get_element_by_xpath(self.driver, last_name).clear().send_keys(last_name)

    def input_address(self, address_text) -> NoReturn:
        get_element_by_xpath(self.driver, address).clear().send_keys(address_text)

    def input_apartment_etc(self, apartment_etc) -> NoReturn:
        get_element_by_xpath(self.driver, apartment).clear().send_keys(apartment_etc)

    def input_zip_code(self, code) -> NoReturn:
        get_element_by_xpath(self.driver, zip_code).clear().send_keys(code)

    def input_city(self, city_text) -> NoReturn:
        get_element_by_xpath(self.driver, city).clear().send_keys(city_text)

    def input_phone(self, phone_number) -> NoReturn:
        get_element_by_xpath(self.driver, phone).clear().send_keys(phone_number)

    def input_state(self, state_text) -> NoReturn:
        get_element_by_xpath(self.driver, state).click()
        is_find = False
        while is_find is not True:
            try:
                actions = TouchAction(self.driver)
                actions.press(x=217, y=815).wait(1000).move_to(x=216, y=778)
                actions.release().perform()
                value = get_element(self.driver, state_value).get_attribute('value')
                if value == state_text:
                    is_find = True
            except Exception as e:
                raise e
        get_element(self.driver, state_done).click()

    def save_address(self) -> NoReturn:
        get_element(self.driver, save_address).click()

    def add_address_flow(self, address_info) -> NoReturn:
        self.input_firstname(address_info['firstname'])
        self.input_lastname(address_info['lastname'])
        self.input_address(address_info['address'])
        self.input_zip_code(address_info['code'])
        self.input_city(address_info['city'])
        self.input_state(state_text=address_info['state'])
        self.save_address()
