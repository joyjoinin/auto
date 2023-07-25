import random
from time import sleep
from config.setup import get_app_name
from data.params import level_params, app_name, Logos, device_type, test_account
from utils.find_element import get_element, get_element_by_xpath, get_elements, get_elements_by_xpath
from typing import NoReturn
from appium.webdriver.common.touch_action import TouchAction
from utils.locator_info import *


class Actions:

    def __init__(self, driver) -> None:
        self.driver = driver

    '''App activity'''

    def open_app(self) -> NoReturn:
        if device_type == 'Real':
            self.driver.activate_app(get_app_name('Dev'))
        else:
            self.driver.activate_app(app_name)

    def close_app(self) -> NoReturn:
        if device_type == 'Real':
            self.driver.terminate_app(get_app_name('Dev'))
        else:
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
        sleep(3)
        get_element(self.driver, access_code_input).send_keys(code)

    def tap_submit(self) -> NoReturn:
        sleep(3)
        get_element(self.driver, submit).click()

    '''Username page'''

    def input_username(self, name) -> NoReturn:
        get_element(self.driver, username).clear().send_keys(name)

    def clear_username(self) -> NoReturn:
        get_element(self.driver, username).clear()

    def tap_continue(self) -> NoReturn:
        sleep(3)
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

    def tap_logos(self, logo_selected):
        sleep(3)
        i = 0
        logo_list = Logos
        tap_list = []
        while i < logo_selected:
            print((len(logo_list)))
            logo.locator = logo_list[random.randint(0, len(logo_list) - 1)]
            get_element(self.driver, logo).click()
            tap_list.append(logo.locator)
            logo_list.remove(logo.locator)
            i = i + 1
        return tap_list

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

    def get_log_scroll_view(self):
        return get_element_by_xpath(self.driver, logo_scroll_view)

    def get_all_logo(self):
        items = get_elements_by_xpath(self.driver, logo_items)
        logo_list = []
        for item in items:
            logo_list.append(item.get_attribute('value'))
        return logo_list

    def swipe_left_card(self) -> NoReturn:
        actions = TouchAction(self.driver)
        actions.press(x=216, y=416).wait(200).move_to(x=60, y=416)
        actions.release().perform()

    def swipe_right_card(self) -> NoReturn:
        actions = TouchAction(self.driver)
        actions.press(x=216, y=416).wait(200).move_to(x=363, y=416)
        actions.release().perform()

    def tap_home_search(self) -> NoReturn:
        get_element_by_xpath(self.driver, search_on_homepage).click()

    def tap_chart_on_homepage(self) -> NoReturn:
        get_element_by_xpath(self.driver, chat_on_homepage).click()

    def common_swipe_vertical(self, element, direction):
        text_location = element.location
        text_size = element.size
        target_y = text_location['y'] + text_size['height'] / 2
        target_x = text_location['x'] + text_size['width'] / 2
        touch_action = TouchAction(self.driver)
        touch_action.press(x=target_x, y=target_y).wait(200).move_to(x=target_x, y=target_y + direction)
        touch_action.release().perform()

    def swipe_up(self) -> NoReturn:
        self.common_swipe_vertical(get_element(self.driver,home_window), -80)

    def swipe_down(self) -> NoReturn:
        self.common_swipe_vertical(get_element(self.driver,home_window), 80)

    '''Log scroll'''

    def common_swipe_horizontal(self, element, direction):
        text_location = element.location
        text_size = element.size
        target_y = text_location['y'] + text_size['height'] / 2
        target_x = text_location['x'] + text_size['width'] / 2
        touch_action = TouchAction(self.driver)
        touch_action.press(x=target_x, y=target_y).wait(200).move_to(x=target_x + direction, y=target_y)
        touch_action.release().perform()

    def log_scroll_left(self):
        self.common_swipe_horizontal(self.get_log_scroll_view(), -80)

    def log_scroll_right(self):
        self.common_swipe_horizontal(self.get_log_scroll_view(), 80)

    def tap_logo(self, logo_name) -> NoReturn:
        logo_item.locator = logo_name
        get_element(self.driver,logo_item).click()

    def get_recommend_follow_buttons(self):
        return get_elements_by_xpath(self.driver, recommend_shops_to_follow)

    def get_recommend_following_buttons(self):
        return get_elements_by_xpath(self.driver, recommend_shops_already_following)
    '''Search page'''

    def close_search_page(self) -> NoReturn:
        get_element_by_xpath(self.driver, close_search_page).click()

    '''DMs page'''

    def tap_add_chat(self) -> NoReturn:
        get_element_by_xpath(self.driver, add_chat).click()

    def cancel_add_message(self) -> NoReturn:
        get_element(self.driver, cancel_add_message).click()

    def clear_message_search_bar(self) -> NoReturn:
        get_element_by_xpath(self.driver, clear_message_search_bar).click()

    def input_on_message_search_bar(self, search_item) -> NoReturn:
        get_element(self.driver, message_search_bar).clear().send_keys(search_item)

    '''Profile page'''

    def tap_setting(self) -> NoReturn:
        get_element(self.driver, setting).click()

    def tap_edit_profile(self) -> NoReturn:
        get_element(self.driver, edit_profile).click()

    def tap_invite_friends(self) -> NoReturn:
        get_element(self.driver, invite_friends).click()

    def tap_share_profile(self) -> NoReturn:
        get_element(self.driver, share_profile).click()

    def tap_profile_followers(self) -> NoReturn:
        get_element(self.driver, profile_followers).click()

    def tap_profile_following(self) -> NoReturn:
        get_element(self.driver, profile_following).click()

    def tap_favorite_shop(self) -> NoReturn:
        get_elements(self.driver, favorite_shops).click()

    '''Edit profile page'''

    def tap_edit_avatar(self) -> NoReturn:
        get_element_by_xpath(self.driver, edit_avatar).click()

    def tap_edit_username(self) -> NoReturn:
        get_element_by_xpath(self.driver, edit_username).click()

    def tap_edit_self_intro(self) -> NoReturn:
        get_element_by_xpath(self.driver, edit_self_intro).click()

    def tap_add_interests(self) -> NoReturn:
        get_element(self.driver, add_interests).click()

    def get_profile_username(self):
        return get_element_by_xpath(self.driver, profile_username).text

    def get_profile_intro(self):
        return get_element_by_xpath(self.driver, profile_self_intro).text

    def get_all_interests(self):
        names = []
        for i in get_elements_by_xpath(self.driver, all_interests):
            names.append(i.text)
        return names

    '''Avatar page'''

    def tap_camera_add(self) -> NoReturn:
        get_element(self.driver, camera_add).click()

    def tap_add_media_image(self) -> NoReturn:
        get_element(self.driver, add_media_image).click()

    def tap_avatar_colorful(self) -> NoReturn:
        all_avatar = get_elements_by_xpath(self.driver, avatar_colorful)
        select_index = random.randint(0, len(all_avatar) - 1)
        all_avatar[select_index].click()

    def tap_save_avatar(self) -> NoReturn:
        get_element_by_xpath(self.driver, save_avatar).click()

    '''Edit username page'''

    def input_new_username(self, new_username) -> NoReturn:
        sleep(1)
        get_element(self.driver, username_input_box).clear().send_keys(new_username)

    def tap_save_username(self) -> NoReturn:
        get_element_by_xpath(self.driver, save_username).click()

    '''Edit intro page'''

    def input_new_intro(self, new_intro) -> NoReturn:
        sleep(1)
        get_element(self.driver, intro_text_field).clear().send_keys(new_intro)

    def tap_save_intro(self) -> NoReturn:
        get_element_by_xpath(self.driver, save_intro).click()

    '''Add interests page'''

    def tap_back_to_edit_page(self) -> NoReturn:
        get_element(self.driver, back_to_edit_page).click()

    '''Invite friends function'''

    def tap_invite_friends_on_profile(self) -> NoReturn:
        get_element(self.driver, invite_friends).click()

    def tap_send_invite(self) -> NoReturn:
        get_element(self.driver, send_invite).click()

    def tap_cancel_invite(self) -> NoReturn:
        get_element(self.driver, cancel_invite).click()

    def tap_close_invite(self) -> NoReturn:
        get_element(self.driver, close_invite_pop).click()

    '''Share page'''

    def tap_close_share(self) -> NoReturn:
        get_element(self.driver, close_share_frame).click()

    '''Follow page'''

    def tap_following_in_profile(self) -> NoReturn:
        get_element(self.driver, profile_following).click()

    def tap_followers_in_profile(self) -> NoReturn:
        get_element(self.driver, profile_followers).click()

    def tap_following_list(self) -> NoReturn:
        get_element_by_xpath(self.driver, following_list_title).click()

    def tap_followers_list(self) -> NoReturn:
        get_element_by_xpath(self.driver, followers_list_title).click()

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

    def tap_purchases(self) -> NoReturn:
        get_element(self.driver, purchases).click()

    def tap_notifications(self) -> NoReturn:
        get_element(self.driver, notifications).click()

    def tap_become_a_seller(self) -> NoReturn:
        get_element(self.driver, become_a_seller).click()

    def tap_contact_us(self) -> NoReturn:
        get_element(self.driver, contact_us).click()

    def tap_FAQs(self) -> NoReturn:
        get_element(self.driver, FAQs).click()

    def tap_setting_privacy_policy(self) -> NoReturn:
        get_element(self.driver, privacy_policy).click()

    def tap_setting_terms_of_use(self) -> NoReturn:
        get_element(self.driver, terms_of_use_on_setting).click()

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
        sleep(1)
        get_element_by_xpath(self.driver, firstname).clear().send_keys(first_name)

    def input_lastname(self, last_name) -> NoReturn:
        sleep(1)
        get_element_by_xpath(self.driver, lastname).clear().send_keys(last_name)

    def input_address(self, address_text) -> NoReturn:
        sleep(1)
        get_element_by_xpath(self.driver, address).clear().send_keys(address_text)

    def input_apartment_etc(self, apartment_etc) -> NoReturn:
        sleep(1)
        get_element_by_xpath(self.driver, apartment).clear().send_keys(apartment_etc)

    def input_zip_code(self, code) -> NoReturn:
        sleep(1)
        get_element_by_xpath(self.driver, zip_code).clear().send_keys(code)

    def input_city(self, city_text) -> NoReturn:
        sleep(1)
        get_element_by_xpath(self.driver, city).clear().send_keys(city_text)

    def input_phone(self, phone_number) -> NoReturn:
        sleep(1)
        get_element_by_xpath(self.driver, phone).clear().send_keys(phone_number)

    def input_state(self, state_text) -> NoReturn:
        get_element_by_xpath(self.driver, state).click()
        is_find = False
        while is_find is not True:
            try:
                actions = TouchAction(self.driver)
                actions.press(x=217, y=815).wait(200).move_to(x=216, y=778)
                actions.release().perform()
                value = get_element(self.driver, state_value, 5).get_attribute('value')
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

    '''Purchase page'''

    '''Notifications page'''

    def tap_notification_type(self, type):
        get_element(self.driver, type).click()

    def tap_switch_button(self, buttons):
        for i in buttons:
            try:
                get_element_by_xpath(self.driver, i).click()
            except Exception as e:
                raise e

    def tap_back_to_notifications(self):
        get_element(self.driver, back_to_notifications).click()

    '''Privacy Policy'''

    '''Flows'''

    def logout_flow(self) -> NoReturn:
        sleep(5)
        self.tap_profile()
        self.tap_setting()
        self.tap_logout()
        self.confirm_logout()

    def login_flow(self, account) -> NoReturn:
        self.tap_login()
        self.input_email(account)
        self.tap_next()
        self.input_password(account.password)
        self.tap_fanatics_id()

    def retry_for_failed_in_creation(self, new_account):
        self.input_username(new_account.username)
        sleep(10)
        self.tap_continue()
        try:
            get_element(self.driver, notification)
            self.set_notification_later()
        except Exception:
            print('already set notification')
        sleep(3)
        self.tap_enter_access_code()
        sleep(3)
        self.input_code(new_account.access_code)
        self.tap_submit()
        self.tap_logos(new_account.logo_select)
        self.tap_continue()
        self.tap_follow(new_account.follow_count)
        self.tap_continue()
        self.select_level(new_account.level_index)
        self.tap_continue()
        self.logout_flow()
        self.assert_element(login, 'success logout')

    def tap_notifications_flow(self, notification_type, buttons, expected, message):
        self.tap_notification_type(notification_type)
        self.tap_switch_button(
            buttons)
        self.tap_back_to_notifications()
        self.tap_notification_type(notification_type)
        self.assert_switch_buttons(
            buttons, expected)
        print(message)
        self.tap_back_to_notifications()

    def get_to_settings(self):
        self.login_flow(test_account)
        self.tap_profile()
        self.tap_setting()

    '''assert action'''

    def assert_element(self, locator, message, wait_time=5) -> NoReturn:
        try:
            assert get_element(self.driver, locator, wait_time)
            print('\n{}'.format(message))
        except Exception as e:
            raise e

    def assert_element_by_xpath(self, locator, message, wait_time=5) -> NoReturn:
        try:
            assert get_element_by_xpath(self.driver, locator, wait_time)
            print('\n{}'.format(message))
        except Exception as e:
            raise e

    def assert_elements(self, locator, message, wait_time=5) -> NoReturn:
        try:
            assert get_elements(self.driver, locator, wait_time)
            print('\n{}'.format(message))
        except Exception as e:
            raise e

    def assert_elements_by_xpath(self, locator, message, wait_time=5) -> NoReturn:
        try:
            assert get_elements_by_xpath(self.driver, locator, wait_time)
            print('\n{}'.format(message))
        except Exception as e:
            raise e

    def assert_element_by_attr(self, locator, attr, expected, message, wait_time=5) -> NoReturn:
        try:
            assert get_element(self.driver, locator, wait_time).get_attribute(attr) == expected
            print('\n{}'.format(message))
        except Exception as e:
            raise e

    def assert_element_by_xpath_attr(self, locator, attr, expected, message, wait_time=5) -> NoReturn:
        try:
            assert get_element_by_xpath(self.driver, locator, wait_time).get_attribute(attr) == expected
            print('\n{}'.format(message))
        except Exception as e:
            raise e

    def assert_switch_buttons(self, buttons, expected) -> NoReturn:
        for i in buttons:
            try:
                assert get_element_by_xpath(self.driver, i, 2).get_attribute('value') == expected
                print('\nswitch button success')
            except Exception as e:
                raise e
