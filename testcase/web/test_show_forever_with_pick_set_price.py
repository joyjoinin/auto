import unittest
from time import sleep
from web.web_user_actions import WebActions
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from datetime import datetime, timedelta
class TestLiveStream(unittest.TestCase):

    def setUp(self) -> None:
        chrome_options = Options()
        chrome_options.add_argument("--use-fake-ui-for-media-stream")
        chrome_options.add_argument("--use-fake-device-for-media-stream")
        # chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(options=chrome_options)
        global do
        do = WebActions(self.driver)

    def tearDown(self):
        self.driver.close()
        self.driver.quit()

    def test1_add_live(self) -> None:
        start_time = datetime.now()
        end_time = start_time + timedelta(days=1)
        do.login()
        do.sign_in()
        do.schedule_a_show()
        do.create_pick_spot_set_price()
        do.publish()
        do.search()
        do.show_detail()
        do.set_inputs()
        do.run_a_listing()
        do.go_live()
        do.run_giveaway_thread()
        sleep(10)
        do.run_overlays_thread()
        is_forever = True
        while is_forever:
            current_time = datetime.now()
            if current_time > end_time:
                do.end_stream()
                break
            try:
                do.tap_start_ripping()
                do.create_listing()
                do.create_pick_spot_set_price()
                do.close_create()
                do.start_next_listing()
                try:
                    do.tap_start_ripping()
                    do.start_next_listing()
                except:
                    raise
            except:
                print('Listing not sold out yet')

