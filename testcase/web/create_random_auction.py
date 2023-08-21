import unittest

from utils.web.common import get_title, get_driver
from utils.web.user_actions import WebActions
from datetime import datetime, timedelta


class TestCreateLive(unittest.TestCase):

    def test_create_random_auction(self):
        show_title = get_title('Auto_R_A')
        do = WebActions(get_driver())
        end_time = datetime.now() + timedelta(days=1)
        do.login_flow(show_title,'ra')
        do.run_forever(end_time, do.random_auction())
        do.after_test()
