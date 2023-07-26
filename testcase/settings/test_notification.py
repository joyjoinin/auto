import unittest
import allure
from config.setup import get_driver
from utils.locator_info import livestreams, marketing_rewards, community, button_new_stream_added, \
    button_stream_going_live, button_giveaways, button_suggested_streams, button_push_notifications, button_email, \
    button_breaking_news, button_offers_rewards, button_events, button_direct_messages, button_new_followers
from utils.user_actions import Actions


@allure.severity(allure.severity_level.CRITICAL)
@allure.feature("Notifications")
class TestNotifications(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = get_driver()
        global do
        do = Actions(self.driver)
        do.get_to_settings()
        do.tap_notifications()

    def tearDown(self):
        self.driver.quit()

    @allure.story("notifications")
    def test1_notifications(self):
        do.assert_element(livestreams, 'find livestreams')
        do.assert_element(marketing_rewards, 'find marketing rewards')
        do.assert_element(community, 'find community')

    @allure.story("check all livestreams buttons")
    def test2_check_all_livestreams_buttons(self):
        buttons = [button_new_stream_added, button_stream_going_live, button_giveaways, button_suggested_streams,
                   button_push_notifications, button_email]
        do.tap_notifications_flow(livestreams, buttons, '0', 'Close all livestreams buttons success')
        do.tap_notifications_flow(livestreams, buttons, '1', 'Open all livestreams buttons success')

    @allure.story("check all marketing & rewards buttons")
    def test2_check_all_marketing_rewards_buttons(self):
        buttons = [button_breaking_news, button_offers_rewards, button_events, button_push_notifications, button_email]
        do.tap_notifications_flow(marketing_rewards, buttons, '0', 'Close all marketing & rewards buttons success')
        do.tap_notifications_flow(marketing_rewards, buttons, '1', 'Open all marketing & rewards buttons success')

    @allure.story("check all community buttons")
    def test3_check_all_community_buttons(self):
        buttons = [button_direct_messages, button_new_followers, button_push_notifications, button_email]
        do.tap_notifications_flow(community, buttons, '0', 'Close all community buttons success')
        do.tap_notifications_flow(community, buttons, '1', 'Open all community buttons success')
        do.back_to_setting()
