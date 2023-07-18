import random
from data.params import level_params, test_account, app_name, Logos
from utils.find_element import get_element, get_element_by_xpath, get_elements, get_elements_by_xpath
from typing import NoReturn
from appium.webdriver.common.touch_action import TouchAction
from utils.locator_info import *


class Actions:

    def __init__(self, driver) -> None:
        self.driver = driver

    '''App activity'''

    def open_app(self) -> NoReturn:
        self.driver.activate_app(app_name)

    def close_app(self) -> NoReturn:
        self.driver.terminate_app(app_name)

    '''App Home'''

    def tap_login(self) -> NoReturn:
        get_element(self.driver, login).click()

    def tap_join(self) -> NoReturn:
        get_element(self.driver, join).click()

    '''Login page'''

    def input_email(self, account) -> NoReturn:
        get_element(self.driver, email).clear().send_keys(account.email)

    def clear_email(self) -> NoReturn:
        get_element(self.driver, email).clear()

    def tap_next(self) -> NoReturn:
        get_element(self.driver, login_next).click()

    def input_password(self, password_type) -> NoReturn:
        get_element(self.driver, password).clear().send_keys(password_type)

    def tap_fanatics_id(self) -> NoReturn:
        get_element(self.driver, fanaticsID).click()

    def tap_not_you(self) -> NoReturn:
        get_element(self.driver, not_you).click()

    def tap_show_password(self) -> NoReturn:
        get_element(self.driver, show_password).click()

    def tap_hide_password(self) -> NoReturn:
        get_element(self.driver, hide_password).click()

    def tap_forget_password(self) -> NoReturn:
        get_element(self.driver, forget_password).click()

    def tap_privacy_policy(self) -> NoReturn:
        get_element(self.driver, terms_of_use).click()

    def tap_create_new_one(self) -> NoReturn:
        get_element(self.driver, create_one_now).click()

    def tap_complete(self) -> NoReturn:
        get_element(self.driver, complete).click()

    '''Access code page'''

    def input_code(self, code) -> NoReturn:
        get_element(self.driver, access_code_input).send_keys(code)

    def tap_submit(self) -> NoReturn:
        get_element(self.driver, submit).click()

    '''Username page'''

    def input_username(self, name) -> NoReturn:
        get_element(self.driver, username).clear()
        get_element(self.driver, username).send_keys(name)

    def tap_continue(self) -> NoReturn:
        get_element(self.driver, join_continue).click()

    '''Track page'''

    def tape_track_with_allow(self) -> NoReturn:
        try:
            get_element(self.driver, track).click()
            get_element(self.driver, track_continue).click()
            get_element(self.driver, track_allow).click()
        except Exception as e:
            raise e
        finally:
            self.tap_home()

    '''Notification page'''

    def set_notification(self) -> NoReturn:
        get_element(self.driver, notification).click()

    def set_notification_later(self) -> NoReturn:
        get_element(self.driver, notification_later).click()

    def allow_notification(self) -> NoReturn:
        get_element(self.driver, notification_allow).click()

    def not_allow_notification(self) -> NoReturn:
        get_element(self.driver, notification_no_allow).click()

    '''Invite page'''

    def tap_invite_your_friends(self) -> NoReturn:
        get_element(self.driver, invite).click()

    def tap_enter_access_code(self) -> NoReturn:
        get_element(self.driver, access_code).click()

    def tap_wait_list_play_button(self) -> NoReturn:
        get_element(self.driver, play_button).click()

    def tap_user_avatar(self, initial) -> NoReturn:
        avatar.locator = initial
        get_element(self.driver, avatar).click()

    '''Collect page'''

    def tap_logos(self, logo_selected) -> NoReturn:
        i = 0
        logo_list = Logos
        while i < logo_selected:
            logo.locator = logo_list[random.randint(0, len(logo_list) - 1)]
            get_element(self.driver, logo).click()
            logo_list.remove(logo.locator)
            i = i + 1

    '''Follow page'''

    def tap_follow(self, index) -> NoReturn:
        for i in range(1, index + 1):
            get_element_by_xpath(self.driver, follow).click()

    def tap_unfollow(self, index) -> NoReturn:
        for i in range(1, index + 1):
            get_element_by_xpath(self, unfollow).click()

    '''Select level page '''

    def select_level(self, index) -> NoReturn:
        level.locator = level_params[index - 1]
        get_element(self.driver, level).click()

    '''Home page'''

    def tap_home(self) -> NoReturn:
        get_element(self.driver, home).click()

    def tap_profile(self) -> NoReturn:
        get_element(self.driver, profile).click()

    def tap_complete_profile(self) -> NoReturn:
        get_element(self.driver, complete_profile).click()

    def tap_close_complete_profile(self) -> NoReturn:
        get_element(self.driver, close_complete_profile).click()

    def tap_view_all(self) -> NoReturn:
        get_element(self.driver, view_all).click()

    '''Profile page'''

    def tap_setting(self) -> NoReturn:
        get_element(self.driver, setting).click()

    '''Setting page'''

    def tap_logout(self) -> NoReturn:
        get_element(self.driver, logout).click()

    def confirm_logout(self) -> NoReturn:
        get_element(self.driver, logout_confirm).click()

    def tap_my_wallet(self) -> NoReturn:
        get_element_by_xpath(self.driver, my_wallet).click()

    def tap_my_address(self) -> NoReturn:
        get_element(self.driver, my_address).click()

    def tap_back(self) -> NoReturn:
        get_element(self.driver, back).click()

    '''Wallet page'''

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

    def add_card_flow(self, card_info) -> NoReturn:
        self.input_card(card_info.card)
        self.input_expiration_date(card_info.date)
        self.input_cvc(card_info.cvc)
        self.select_country(card_info.country)
        self.input_zip(card_info.zip_number)
        self.set_up()

    '''Wallet list'''

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

    '''Addresses page'''

    def input_firstname(self, first_name) -> NoReturn:
        get_element_by_xpath(self.driver, firstname).clear().send_keys(first_name)

    def input_lastname(self, last_name) -> NoReturn:
        get_element_by_xpath(self.driver, lastname).clear().send_keys(last_name)

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
                actions.press(x=217, y=815).wait(200).move_to(x=216, y=778)
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
        self.input_firstname(address_info.firstname)
        self.input_lastname(address_info.lastname)
        self.input_address(address_info.address)
        self.input_zip_code(address_info.code)
        self.input_city(address_info.city)
        self.input_state(state_text=address_info.state)
        self.save_address()

    '''address list page'''

    def tap_add_shipping(self) -> NoReturn:
        get_element(self.driver, add_address).click()

    def find_address_items(self):
        items = get_elements_by_xpath(self.driver, address_item)
        address_list = []
        for i in items:
            address_label = i.get_attribute('label')
            if address_label is not None:
                address_list.append(address_label)
        return address_list

    def cancel_add_address(self) -> NoReturn:
        get_element_by_xpath(self.driver, cancel_add_address)

    def delete_address(self) -> NoReturn:
        get_element_by_xpath(self.driver, delete_address).click()

    def confirm_delete_address(self) -> NoReturn:
        get_element(self.driver, confirm_delete_address).click()

    def cancel_delete_address(self) -> NoReturn:
        get_element(self.driver, cancel_delete_address).click()

    def back_to_setting(self) -> NoReturn:
        get_element(self.driver, back_to_setting).click()

    '''Flows'''

    def logout_flow(self) -> NoReturn:
        self.tap_profile()
        self.tap_setting()
        self.tap_logout()
        self.confirm_logout()

    def login_flow(self) -> NoReturn:
        self.tap_login()
        self.input_email(test_account)
        self.tap_next()
        self.input_password(test_account.password)
        self.tap_fanatics_id()

    '''assert action'''

    def assert_element(self, locator, message) -> NoReturn:
        try:
            assert get_element(self.driver, locator)
            print(message)
        except Exception as e:
            raise e

    def assert_elements(self, locator, message) -> NoReturn:
        try:
            assert get_elements(self.driver, locator)
            print(message)
        except Exception as e:
            raise e

    def assert_element_by_attr(self, locator, attr, expected, message) -> NoReturn:
        try:
            assert get_element(self.driver, locator).get_attribute(attr) == expected
            print(message)
        except Exception as e:
            raise e
