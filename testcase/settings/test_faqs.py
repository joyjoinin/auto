import unittest
import allure
from config.setup import get_driver
from utils.locator_info import FAQs_page
from utils.user_actions import Actions


@allure.severity(allure.severity_level.CRITICAL)
@allure.feature("FAQs")
class TestFAQs(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = get_driver()
        global do
        do = Actions(self.driver)

    def tearDown(self):
        do.back_to_setting()
        self.driver.quit()

    @allure.story("FAQs")
    def test1_FAQs(self):
        do.tap_FAQs()
        do.assert_element_by_xpath(FAQs_page,'Show FAQs success')
