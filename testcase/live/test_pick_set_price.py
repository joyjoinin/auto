import unittest
import allure
from config.setup import get_driver
from utils.user_actions import Actions


@allure.severity(allure.severity_level.CRITICAL)
@allure.feature("Live")
class TestPickSetPrice(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = get_driver()
        global do
        do = Actions(self.driver)

    def tearDown(self):
        self.driver.quit()

    @allure.story("Buy a spot")
    def test1_buy_a_spot(self) -> None:
        pass
