import unittest
import allure
from config.setup import get_driver
from data.mobile_params import test_message_on_live, long_message_on_live, system_message_for_long_message
from utils.mobile.user_actions import Actions


@allure.severity(allure.severity_level.CRITICAL)
@allure.feature("Live")
class TestMessages(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = get_driver(no_rest=True)
        global do
        do = Actions(self.driver)

    def tearDown(self):
        self.driver.quit()

    @allure.story("Send message")
    def test1_send_normal_message(self) -> None:
        do.input_message_on_live(test_message_on_live)
        do.send_message_on_live()
        message = do.get_latest_message()
        assert test_message_on_live in message

    @allure.story("Send long message")
    def test2_send_long_message(self) -> None:
        do.input_message_on_live(long_message_on_live)
        do.send_message_on_live()
        message = do.get_error_message_on_live()
        assert message == system_message_for_long_message

    @allure.story("Send more than 10 messages")
    def test3_send_more_messages(self) -> None:
        i = 0
        while i < 10:
            do.input_message_on_live(test_message_on_live)
            do.send_message_on_live()
            message = do.get_latest_message()
            assert test_message_on_live in message
            i += 1
