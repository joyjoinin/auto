import unittest
import allure
from config.setup import get_driver
from data.params import test_account
from utils.user_actions import Actions


@allure.severity(allure.severity_level.CRITICAL)
@allure.feature("Hero card")
class TestHeroCard(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = get_driver()
        global do
        do = Actions(self.driver)
        do.open_app()

    def tearDown(self):
        self.driver.quit()

    @allure.story("Swipe card 10 times")
    def test1_swipe_card(self):
        i = 0
        while i < 6:
            do.swipe_left_card()
            do.swipe_right_card()
            i += 1
        print('swipe card success')

