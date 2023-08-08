import random
import unittest
import allure
from time import sleep
from config.setup import get_driver
from data.params import test_account
from utils.find_element import get_element_by_xpath
from utils.common import get_random_username, get_random_text, get_expected_interests
from mobile.mobile_locator_info import save_username, profile_username, profile_self_intro
from mobile.mobile_user_actions import Actions


@allure.severity(allure.severity_level.CRITICAL)
@allure.feature("Edit Profile")
class TestEditProfile(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = get_driver()
        global do
        do = Actions(self.driver)
        do.login_flow(test_account)
        do.tap_profile()
        do.tap_edit_profile()
    def tearDown(self):
        self.driver.quit()

    @allure.story("change avatar")
    def test1_change_avatar(self):
        do.tap_edit_avatar()
        do.tap_avatar_colorful()
        do.tap_save_avatar()
        '''need assert color'''

    @allure.story("change username")
    def test2_change_username(self):
        do.tap_edit_username()
        new_username = get_random_username()
        do.input_new_username(new_username)
        wait_to_save = True
        while wait_to_save is True:
            if get_element_by_xpath(self.driver, save_username).get_attribute('enabled') == 'true':
                wait_to_save = False
        do.tap_save_username()
        do.assert_element_by_xpath_attr(profile_username, 'value', new_username, 'Edit username success')

    @allure.story("edit self intro")
    def test3_change_self_intro(self):
        do.tap_edit_self_intro()
        intro_text = get_random_text()
        do.input_new_intro(intro_text)
        do.tap_save_intro()
        do.assert_element_by_xpath_attr(profile_self_intro, 'value', intro_text, 'Edit intro success')

    @allure.story("change interests")
    def test4_change_interests(self):
        origin_interests = do.get_all_interests()
        do.tap_add_interests()
        change_interests = do.tap_logos(random.randint(1, 12))
        expected_interest_list = get_expected_interests(origin_interests, change_interests)
        do.tap_back_to_edit_page()
        sleep(3)
        current_interests = do.get_all_interests()
        assert set(expected_interest_list) == set(current_interests)
        print('Change interests success')