import unittest
import allure
from config.setup import get_driver
from mobile.mobile_locator_info import schedule_title
from mobile.mobile_user_actions import Actions


@allure.severity(allure.severity_level.CRITICAL)
@allure.feature("Live")
class TestViewSchedule(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = get_driver(no_rest=True)
        global do
        do = Actions(self.driver)

    def tearDown(self):
        self.driver.quit()

    @allure.story("View schedule")
    def test1_view_schedule(self) -> None:
        do.tap_view_schedule()
        do.assert_element(schedule_title,'Open schedule success')
        do.swap_down_schedule()
