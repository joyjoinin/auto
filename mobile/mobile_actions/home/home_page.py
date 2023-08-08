from utils.find_element import get_element, get_element_by_xpath, get_elements_by_xpath
from typing import NoReturn
from appium.webdriver.common.touch_action import TouchAction
from mobile.mobile_locators.home.home_page import home, profile, complete_profile, close_complete_profile, \
    view_all, search_on_homepage, chat_on_homepage
from mobile.mobile_locators.home.logo_page import logo_scroll_view, logo_items
from mobile.mobile_locators.login.login_home_page import home_window


class HomeActions:

    def __init__(self, driver) -> None:
        self.driver = driver

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


    def swipe_up(self, distance=-80) -> NoReturn:
        common_swipe_vertical(get_element(self.driver, home_window), distance)

    def swipe_down(self, distance=80) -> NoReturn:
        common_swipe_vertical(get_element(self.driver, home_window), distance)
