import unittest
import allure
from time import sleep
from config.setup import get_driver
from data.params import address_info
from utils.locator_info import login
from utils.user_actions import Actions


@allure.severity(allure.severity_level.CRITICAL)
@allure.feature("Shipping address")
class TestShippingAddress(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = get_driver()
        global do
        do = Actions(self.driver)
        do.get_to_settings()

    def tearDown(self):
        self.driver.quit()

    @allure.story("Add shipping address")
    def test1_add_address(self) -> None:
        sleep(2)
        do.tap_my_address()
        address_before_add = do.find_address_items()
        do.tap_add_shipping()
        do.add_address_flow(address_info)
        sleep(10)
        address_after_add = do.find_address_items()
        try:
            assert (len(address_after_add) == len(address_before_add) + 1)
            print('Add address success')
        except Exception:
            raise

    @allure.story("Delete shipping address")
    def test2_delete_address(self) -> None:
        sleep(2)
        do.tap_my_address()
        address_before_delete = do.find_address_items()
        do.delete_address()
        sleep(2)
        do.confirm_delete_address()
        sleep(10)
        address_after_delete = do.find_address_items()
        try:
            assert (len(address_after_delete) == len(address_before_delete) - 1)
            print('Delete address success')
        except Exception:
            raise
        do.back_to_setting()
        do.logout_flow()
        do.assert_element(login, 'Logout success')
