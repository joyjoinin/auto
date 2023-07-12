import unittest
from config.test_setup import get_driver
from utils.user_actions import Actions


class TestExistedAccount(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = get_driver()
        global do
        do = Actions(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test1_join(self) -> None:
        pass

    def test2_join(self) -> None:
        pass


