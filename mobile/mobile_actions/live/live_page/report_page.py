import random
from utils.find_element import get_element, get_element_by_xpath, get_elements_by_xpath
from mobile.mobile_locators.common import submit
from mobile.mobile_locators.live.live_page.report_page import *


class ReportActions:

    def __init__(self, driver) -> None:
        self.driver = driver

    def input_email_answer(self,answer):
        get_element_by_xpath(self.driver, email_answer).clear().send_keys(answer)

    def tap_ok(self):
        get_element(self.driver, confirm_button).click()

    def tap_next_question(self):
        get_element(self.driver, next_question).click()

    def tap_pre_question(self):
        get_element(self.driver, previous_question).click()

    def input_name_answer(self,answer):
        get_element_by_xpath(self.driver, name_answer).clear().send_keys(answer)

    def select_an_option(self):
        get_elements_by_xpath(self.driver, report_option_list)[random.randint(0,6)].click()

    def input_addition(self,answer):
        get_element_by_xpath(self.driver, addition_answer).clear().send_keys(answer)

    def select_screenshot(self):
        get_element(self.driver,screenshot_select).click()

    def tap_submit_report(self):
        get_element(self.driver, submit).click()

    def swap_down_report(self):
        self.swap_down_list(report_title, 800)

