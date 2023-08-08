import unittest
import allure
from config.setup import get_driver
from mobile.mobile_locator_info import contact_us_page
from mobile.mobile_user_actions import Actions


@allure.severity(allure.severity_level.CRITICAL)
@allure.feature("Contact us")
class TestContactUs(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = get_driver()
        global do
        do = Actions(self.driver)
        do.get_to_settings()

    def tearDown(self):
        self.driver.quit()

    @allure.story("contact us")
    def test1_contact_us(self):
        do.tap_contact_us()
        do.assert_element(contact_us_page,'show contact us page success')
