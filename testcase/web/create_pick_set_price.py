import unittest

from utils.web.common import get_title, get_driver
from utils.web.user_actions import WebActions
from datetime import datetime, timedelta


class TestCreateLive(unittest.TestCase):

    def test_create_pick_set_price(self):
        show_title = get_title('Auto_P_S')
        do = WebActions(get_driver())
        end_time = datetime.now() + timedelta(days=1)
        do.login_flow(show_title, 'ps')
        do.run_forever(end_time, do.p_s_flow())
        do.after_test()
