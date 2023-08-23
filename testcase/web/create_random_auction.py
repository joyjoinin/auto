import unittest
import pytest
from utils.web.common import get_title, get_driver
from utils.web.user_actions import WebActions
from datetime import datetime, timedelta


class TestCreateLive(unittest.TestCase):
    @pytest.mark.flaky(reruns=3)
    def test_create_random_auction(self):
        show_title = get_title('RandomAuction')
        do = WebActions(get_driver())
        end_time = datetime.now() + timedelta(days=1)
        do.login_flow(show_title,'ra')
        do.run_forever(end_time, do.random_auction())
        do.after_test()
