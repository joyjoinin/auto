import unittest
import allure
from config.setup import get_driver
from data.params import test_account
from utils.locator_info import following_list_title, followers_list_title, \
    empty_followers_list, empty_following_list
from utils.user_actions import Actions


@allure.severity(allure.severity_level.CRITICAL)
@allure.feature("Follow")
class TestFollow(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = get_driver()
        global do
        do = Actions(self.driver)
        do.login_flow(test_account)
        do.tap_profile()

    def tearDown(self):
        self.driver.quit()

    @allure.story("followers")
    def test1_followers(self):
        do.tap_profile_followers()
        do.assert_element_by_xpath(followers_list_title, 'get in list success')

    @allure.story("following")
    def test2_following(self):
        do.tap_profile_following()
        do.assert_element_by_xpath(following_list_title, 'get in list success')

    @allure.story("Empty list")
    def test3_follow_list(self):
        do.tap_profile_following()
        do.assert_element_by_xpath(following_list_title, 'get in list success')
        do.tap_followers_list()
        do.assert_element(empty_followers_list, 'empty followers list')
        do.tap_following_list()
        do.assert_element(empty_following_list, 'empty following list')
