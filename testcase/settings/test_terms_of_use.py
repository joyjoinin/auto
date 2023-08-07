import unittest
import allure
from config.setup import get_driver
from utils.mobile_utils.mobile_locator_info import text_container
from utils.mobile_utils.mobile_user_actions import Actions


@allure.severity(allure.severity_level.CRITICAL)
@allure.feature("Privacy policy")
class TestTermsOfUse(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = get_driver()
        global do
        do = Actions(self.driver)
        do.get_to_settings()

    def tearDown(self):
        self.driver.quit()

    @allure.story("privacy policy")
    def test1_terms_of_use(self):
        do.tap_setting_terms_of_use()
        do.assert_element_by_xpath(text_container, 'go terms of use success')
