# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# import unittest
# from config.setup import get_driver
# from data.mobile_params import random_spot_name
# from mobile.mobile_locator_info import input_message, close_live
# from mobile.mobile_user_actions import Actions
# from web.web_user_actions import WebActions
#
#
# class TestLiveStream(unittest.TestCase):
#
#     def test1_add_live(self) -> None:
#         mobile_driver = get_driver(no_rest=True)
#         chrome_options = Options()
#         chrome_options.add_argument("--use-fake-ui-for-media-stream")
#         chrome_options.add_argument("--use-fake-device-for-media-stream")
#         chrome_options.add_argument("--headless")
#         web_driver = webdriver.Chrome(options=chrome_options)
#         web = WebActions(web_driver)
#         web.login()
#         web.sign_in()
#         web.schedule_a_show()
#         web.add_listings()
#         web.publish()
#         web.search()
#         web.show_detail()
#         web.set_inputs()
#         web.run_a_listing()
#         web.go_live()
#         web_driver.quit()
#         mobile_driver.switch_to.context('NATIVE_APP')
#         name = new_title
#         do = Actions(mobile_driver)
#         do.tap_view_all()
#         is_find = False
#         while is_find is False:
#             try:
#                 do.tap_live_at_view_all(name)
#                 do.assert_element(close_live, 'get in live success',0.5)
#                 is_find = True
#                 break
#             except:
#                 do.swipe_up(-800)
#         buy_spot_num = do.get_buy_spots_num()
#         single_spot_price = do.get_single_price()
#         while buy_spot_num != 1:
#             do.decrease_spot()
#             buy_spot_num -= 1
#         beginning_remained = do.get_all_spots_num()[0]
#         do.tap_to_buy()
#         do.asser_order_detail(random_spot_name,single_spot_price)
#         after_remained = do.get_all_spots_num()[0]
#         assert beginning_remained == after_remained + 1
#         mobile_driver.quit()
#
#
#
#
#
#
