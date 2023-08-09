import unittest
import allure
from config.setup import get_driver
from data.mobile_params import test_account
from utils.find_element import get_element_by_xpath
from mobile.mobile_locator_info import recommend_location
from mobile.mobile_user_actions import Actions


@allure.severity(allure.severity_level.CRITICAL)
@allure.feature("You might also like")
class TestYouMightAlsoLike(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = get_driver()
        global do
        do = Actions(self.driver)
        do.login_flow(test_account)

    def tearDown(self):
        self.driver.quit()

    @allure.story("follow a channel")
    def test1_find_channels(self):
        is_end = False
        channels_location = ''
        while is_end is False:
            do.swipe_up()
            location = get_element_by_xpath(self.driver, recommend_location).location['y']
            if location != -1 and location == channels_location:
                is_end = True
            else:
                channels_location = location
        print('\nfind You Might Also Like')

    @allure.story("follow all channels , unfollow all channels")
    def test2_follow_channels_actions(self):
        is_end = False
        channels_location = ''
        while is_end is False:
            do.swipe_up()
            location = get_element_by_xpath(self.driver, recommend_location).location['y']
            if location != -1 and location == channels_location:
                is_end = True
            else:
                channels_location = location
        print('\nfind You Might Also Like')
        follow_buttons = do.get_recommend_follow_buttons()
        for button in follow_buttons:
            button.click()
        following_buttons = do.get_recommend_following_buttons()
        assert following_buttons == follow_buttons
        print('\nfollow all success')
        follow_buttons = do.get_recommend_following_buttons()
        for button in follow_buttons:
            button.click()
        following_buttons = do.get_recommend_follow_buttons()
        assert following_buttons == follow_buttons
        print('\nunfollow all success')


