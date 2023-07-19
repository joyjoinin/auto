import unittest
import allure
from time import sleep
from config.setup import get_driver
from data.params import card_info, test_account
from utils.user_actions import Actions


@allure.feature("Bank Card")
class TestCard(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = get_driver()
        global do
        do = Actions(self.driver)

    def tearDown(self):
        self.driver.quit()

    @allure.story("Add card")
    def test1_add_card(self) -> None:
        do.login_flow(test_account)
        do.tap_profile()
        do.tap_setting()
        sleep(2)
        do.tap_my_wallet()
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

    @allure.story("Delete card")
    def test2_delete_card(self) -> None:
        cards_before_delete = do.get_wallet_list()
        do.edit_card_list()
        do.delete_card()
        do.confirm_delete_card()
        do.tap_done_edit_card()
        cards_after_delete = do.get_wallet_list()
        do.exit_add_payment()
        do.tap_back()
        try:
            assert (len(cards_after_delete) == len(cards_before_delete) - 1)
            print('Delete card success')
        except Exception:
            raise
        do.logout_flow()