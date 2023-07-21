import unittest
import allure
from config.setup import get_driver
from data.params import test_account
from utils.user_actions import Actions


@allure.severity(allure.severity_level.CRITICAL)
@allure.feature("You might also like")
class TestYouMightAlsoLike(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = get_driver()
        global do
        do = Actions(self.driver)
        do.open_app()

    def tearDown(self):
        self.driver.quit()

    @allure.story("follow a channel")
    def test1_follow_a_channel(self):
        # do.login_flow(test_account)
        pass

    @allure.story("follow all channels")
    def test2_follow_all_channels(self):
        # do.login_flow(test_account)
        pass

