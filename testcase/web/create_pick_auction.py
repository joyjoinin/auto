import unittest
from datetime import datetime, timedelta
from utils.common_web import get_title, get_driver
from web.web_user_actions import WebActions


class TestCreateLive(unittest.TestCase):

    def test_create_pick_auction(self):
        show_title = get_title('Auto_P_A')
        do = WebActions(get_driver())
        end_time = datetime.now() + timedelta(days=1)
        do.login_flow(show_title, 'pa')
        do.run_forever(end_time, do.pick_auction())
        do.after_test()
