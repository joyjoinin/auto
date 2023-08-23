import unittest
import pytest
from datetime import datetime, timedelta
from utils.web.common import get_title, get_driver
from utils.web.user_actions import WebActions


class TestCreateLive(unittest.TestCase):

    @pytest.mark.flaky(reruns=3)
    def test_create_pick_auction(self):
        show_title = get_title('PickAuction')
        do = WebActions(get_driver())
        end_time = datetime.now() + timedelta(days=1)
        do.login_flow(show_title, 'pa')
        do.run_forever(end_time, do.pick_auction())
        do.after_test()
