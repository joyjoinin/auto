import unittest
import allure
from config.setup import get_driver
from utils.locator_info import contact_us_page
from utils.user_actions import Actions


@allure.severity(allure.severity_level.CRITICAL)
@allure.feature("Contact us")
class TestPurchases(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = get_driver()
        global do
        do = Actions(self.driver)

    def tearDown(self):
        do.back_to_setting()
        self.driver.quit()

    @allure.story("contact us")
    def test1_contact_us(self):
        do.tap_contact_us()
        do.assert_element(contact_us_page,'show contact us page success')
