import unittest

from utils.common_web import get_title, get_driver
from web.web_user_actions import WebActions
from datetime import datetime, timedelta


class TestAccountCreation(unittest.TestCase):
    def test_create_random_set_price(self):
        show_title = get_title('Auto_R_S')
        do = WebActions(get_driver())
        end_time = datetime.now() + timedelta(days=1)
        do.login_flow(show_title, 'rs')
        do.run_forever(end_time, do.random_set_price())
        do.after_test()
