import unittest
from time import sleep

from config.test_setup import get_driver
from data.test_params import card_info
from utils.user_actions import Actions


class TestCard(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = get_driver()
        global do
        do = Actions(self.driver)
        do.tap_profile()
        do.tap_setting()
        sleep(2)
        do.tap_my_wallet()

    def tearDown(self):
        do.tap_card_set_up()
        do.tap_back()
        do.tap_home()
        self.driver.quit()

    def test1_add_address(self) -> None:
        cards_before_add = do.get_wallet_list()
        do.tap_add_card()
        do.add_card_flow(card_info)
        sleep(5)
        do.tap_my_wallet()
        cards_after_add = do.get_wallet_list()
        try:
            assert (len(cards_after_add) == len(cards_before_add) + 1)
            print('Add card success')
        except Exception:
            raise

    def test2_delete_address(self) -> None:
        cards_before_delete = do.get_wallet_list()
        do.edit_card_list()
        do.delete_card()
        do.confirm_delete_card()
        do.tap_done_edit_card()
        cards_after_delete = do.get_wallet_list()
        try:
            assert (len(cards_after_delete) == len(cards_before_delete) - 1)
            print('Delete card success')
        except Exception:
            raise
