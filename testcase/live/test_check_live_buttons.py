import unittest
import allure
from config.setup import get_driver
from data.mobile_params import return_policy_text, shipping_taxes_text, test_report
from utils.mobile.locator_info import schedule_title, share_frame, confirm_button, \
    return_policy, Shipping_taxes, previous_question, next_question, thanks
from utils.mobile.user_actions import Actions


@allure.severity(allure.severity_level.CRITICAL)
@allure.feature("Live")
class TestLiveButtons(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = get_driver(no_rest=True)
        global do
        do = Actions(self.driver)

    def tearDown(self):
        self.driver.quit()

    @allure.story("shop")
    def test1_tap_shop(self) -> None:
        do.tap_shop()
        do.assert_element_by_xpath(return_policy, 'Open shop page success')
        do.assert_element_by_xpath_attr(return_policy, 'label', return_policy_text, 'policy text correct')
        do.assert_element_by_xpath_attr(Shipping_taxes, 'label', shipping_taxes_text, 'Shipping&taxes text correct')
        do.tap_follow_shop_page()
        do.swap_down_shop_page()
        do.tap_shop()
        do.tap_unfollow_shop_page()
        do.tap_report_shop_page()
        do.assert_element(confirm_button, 'Open report page success', 10)
        do.tap_back()
        do.swap_down_shop_page()

    @allure.story("Flag")
    def test2_tap_flag(self) -> None:
        do.tap_flag()
        do.assert_element(confirm_button, 'Open report page success', 10)
        do.assert_element_by_attr(previous_question, 'enabled', 'false', "This is first page")
        do.input_email_answer(test_report['email'])
        do.tap_ok()
        do.input_name_answer(test_report['user'])
        do.tap_ok()
        do.select_an_option()
        do.input_addition(test_report['add'])
        do.tap_ok()
        do.select_screenshot()
        do.assert_element_by_attr(next_question, 'enabled', 'false', "This is last page")
        is_last_page = True
        is_first_page = False
        while is_last_page is True:
            do.tap_pre_question()
            if do.get_attr(previous_question,'enabled') == 'false':
                is_first_page = True
                is_last_page = False
        while is_first_page is True:
            do.tap_next_question()
            if do.get_attr(next_question,'enabled') == 'false':
                break
        do.tap_submit_report()
        do.assert_element(thanks, 'Submit success')
        do.swap_down_report()

    @allure.story("share")
    def test3_tap_share(self) -> None:
        do.tap_share()
        do.assert_element(share_frame, 'Open share success')
        do.tap_close_share()

    @allure.story("schedule")    # listing sold out
    def test4_tap_schedule(self) -> None:
        do.tap_schedule()
        do.assert_element(schedule_title, 'Open schedule success')
        do.swap_down_schedule()
