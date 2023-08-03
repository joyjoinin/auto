import unittest
import allure
from config.setup import get_driver
from data.params import test_account
from utils.locator_info import logo_title
from utils.user_actions import Actions


@allure.severity(allure.severity_level.CRITICAL)
@allure.feature("Home logos")
class TestHomeLogos(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = get_driver()
        global do
        do = Actions(self.driver)
        do.login_flow(test_account)

    def tearDown(self):
        self.driver.quit()

    @allure.story("Swipe logo")
    def test1_swipe_logo(self):
        i = 1
        swipe_times = len(do.get_all_logo()) / 2
        while i < swipe_times:
            do.logo_scroll_left()
            i += 1
        print(f'\nswipe left logo {swipe_times - 1}')
        while i > 0:
            do.logo_scroll_right()
            i -= 1
        print(f'\nswipe right logo {swipe_times - 1}')

    @allure.story("tap all logo")
    def test2_tap_all_logo(self):
        logo_list = do.get_all_logo()
        for logo in logo_list:
            do.tap_logo(logo)
            do.assert_element_by_attr(logo_title, 'name', logo, f'tap {logo} success', 2)
        do.tap_back()
