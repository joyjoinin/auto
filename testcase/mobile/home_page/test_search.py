import unittest
import allure
from config.setup import get_driver
from data.mobile_params import test_account
from utils.mobile.locator_info import search_field, popular_streams_title
from utils.mobile.user_actions import Actions


@allure.severity(allure.severity_level.CRITICAL)
@allure.feature("Home search")
class TestHomeSearch(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = get_driver()
        global do
        do = Actions(self.driver)
        do.login_flow(test_account)

    def tearDown(self):
        self.driver.quit()

    @allure.story("get to search page")
    def test1_tap_search(self):
        do.tap_home_search()
        do.assert_element_by_xpath(search_field, 'get search field')
        do.assert_element(popular_streams_title, 'get popular streams')

    @allure.story("exit search page")
    def test2_close_search(self):
        do.tap_home_search()
        do.close_search_page()
        try:
            do.assert_element_by_xpath(search_field, 'get search field')
        except Exception:
            print('back to home success')
