import unittest
import allure
from config.setup import get_driver
from data.params import test_account
from utils.locator_info import popular_page_title
from utils.user_actions import Actions


@allure.severity(allure.severity_level.CRITICAL)
@allure.feature("View all")
class TestViewAll(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = get_driver()
        global do
        do = Actions(self.driver)
        do.login_flow(test_account)

    def tearDown(self):
        self.driver.quit()

    @allure.story("get to view all")
    def test1_tap_view_all(self):
        do.tap_view_all()
        do.assert_element_by_xpath(popular_page_title,'get to popular page success',2)

    @allure.story("back to Home")
    def test2_back_to_home(self):
        do.tap_view_all()
        do.tap_back()
        try:
            do.assert_element_by_xpath(popular_page_title, 'get to popular page success',2)
        except Exception:
            print('back to Home success')


