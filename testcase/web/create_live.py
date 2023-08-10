import unittest
from web.web_user_actions import WebActions
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class TestLiveStream(unittest.TestCase):

    def setUp(self) -> None:
        chrome_options = Options()
        chrome_options.add_argument("--use-fake-ui-for-media-stream")
        chrome_options.add_argument("--use-fake-device-for-media-stream")
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(options=chrome_options)
        global do
        do = WebActions(self.driver)

    def tearDown(self):
        self.driver.close()
        self.driver.quit()

    def test1_add_live(self) -> None:
        do.login()
        do.sign_in()
        do.schedule_a_show()
        do.add_listings()
        do.publish()
        do.search()
        do.show_detail()
        do.set_inputs()
        do.run_a_listing()
        do.go_live()




