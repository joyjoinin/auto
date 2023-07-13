import unittest
from time import sleep

from config.test_setup import get_driver
from data.test_params import address_info, app_name
from utils.locator_info import address_item
from utils.user_actions import Actions


class Test_add_address(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = get_driver()
        self.driver.activate_app(app_name)
        global do
        do = Actions(self.driver)

    def tearDown(self):
        self.driver.terminate_app(app_name)

    def test1_add_address(self) -> None:
        do.tap_profile()
        do.tap_setting()
        do.tap_my_address()
        items_before_add = do.find_address_items()
        do.tap_add_shipping()
        do.add_address_flow(address_info)
        sleep(5)
        items_after_add = do.find_address_items()
        try:
            assert (len(items_after_add) == len(items_before_add) + 1)
            print('Add address success')
        except Exception:
            raise

    def test2_delete_address(self) -> None:
        items_before_delete = do.find_address_items()
        do.delete_address()
        do.confirm_delete_address()
        sleep(5)
        items_after_delete = do.find_address_items()
        try:
            assert (len(items_after_delete) == len(items_before_delete) - 1)
            print('Delete address success')
        except Exception:
            raise



