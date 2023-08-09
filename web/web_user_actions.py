import random
from time import sleep
from selenium.webdriver.support.ui import Select
from data.web_params import *
from utils.common_web import get_image_path, get_date, get_time, get_title, save_data, get_args_list
from utils.find_element import get_element, get_element_by_xpath, get_elements_by_xpath
from web.web_locator_info import *

new_title = get_title()
args_list = get_args_list()


class WebActions:

    def __init__(self, driver) -> None:
        self.driver = driver

    def login(self):
        self.driver.get(login_url)
        self.driver.maximize_window()
        sleep(2)

    def sign_in(self):
        get_element(self.driver, login).click()
        get_element(self.driver, username).send_keys(account)
        get_element(self.driver, user_password).send_keys(password)
        get_element(self.driver, sign_in).click()
        sleep(2)
        self.driver.get(manage_url)

    def schedule_a_show(self):
        new_show = Show(title=new_title, cover_image=get_image_path(), date=get_date(), time=get_time())
        get_element(self.driver, schedule_a_show).click()
        get_element(self.driver, title).send_keys(new_show.title)
        save_data(new_show.title)
        sleep(2)
        upload_file = get_element(self.driver, upload)
        upload_file.send_keys(new_show.cover_image)
        sleep(2)
        get_element(self.driver, date).send_keys(new_show.date)
        get_element(self.driver, time).send_keys(new_show.time)
        channel_dropdown = get_element(self.driver, channel)
        channel_dropdown.click()
        select = Select(channel_dropdown)
        select.select_by_visible_text(new_show.channel)
        creator_dropdown = get_element(self.driver, creator)
        creator_dropdown.click()
        select = Select(creator_dropdown)
        select.select_by_visible_text(new_show.creator)
        get_element_by_xpath(self.driver, add_listing).click()

    def common_create_steps(self, listing):
        sleep(2)
        get_element(self.driver, listing_title).send_keys(listing.title)
        sleep(1)
        option_dropdown = get_element(self.driver, select_an_option)
        option_dropdown.click()
        select = Select(option_dropdown)
        select.select_by_visible_text(listing.option)
        sleep(1)
        get_element_by_xpath(self.driver, listing.assign_type).click()
        sleep(1)
        get_element_by_xpath(self.driver, listing.sell_type).click()
        if listing.min_bid is not None:
            get_element(self.driver, min_bid).send_keys(listing.min_bid)
        elif listing.assign_price is not None:
            get_element(self.driver, assign_price).click()
            sleep(1)
            spots = get_elements_by_xpath(self.driver, assign_list)
            for spot in spots:
                spot.send_keys(listing.assign_price)
                sleep(0.5)
            get_element(self.driver, assign_prices).click()
        elif listing.price_per_spot is not None:
            get_element(self.driver, price_per_spot).send_keys(listing.price_per_spot)
        sleep(1)
        get_element_by_xpath(self.driver, save_listing).click()

    def create_random_set_price_listing(self, num=1):
        i = 0
        while i < num:
            listing = Listing(title='random set price', assign_type=random, sell_type=set_price, price_per_spot=10000)
            self.common_create_steps(listing)
            i += 1

    def create_random_auction(self, num=1):
        i = 0
        while i < num:
            listing = Listing(title='random auction', assign_type=random, sell_type=auction, min_bid=1000)
            self.common_create_steps(listing)
            i += 1

    def create_pick_spot_auction(self, num=1):
        i = 0
        while i < num:
            listing = Listing(title='pick auction', assign_type=pick_your_spot, sell_type=auction, min_bid=5000)
            self.common_create_steps(listing)
            i += 1

    def create_pick_spot_set_price(self, num=1):
        i = 0
        while i < num:
            listing = Listing(title='pick set price', assign_type=pick_your_spot, sell_type=set_price, assign_price=100)
            self.common_create_steps(listing)
            i += 1

    def publish(self):
        sleep(1)
        get_element_by_xpath(self.driver, publish).click()

    def search(self):
        sleep(1)
        get_element_by_xpath(self.driver, search_streams).send_keys(new_title)
        sleep(1)

    def edit(self):
        get_element_by_xpath(self.driver, edit_show).click()
        sleep(3)

    def show_detail(self):
        show_detail = LocatorInfo(locator=f"//*[contains(text(), '{new_title}')]/../../footer//*[@title='Details']")
        get_element_by_xpath(self.driver, show_detail).click()
        sleep(10)

    def set_media(self, item, option):
        sleep(1)
        option_dropdown = get_element(self.driver, item)
        option_dropdown.click()
        select = Select(option_dropdown)
        select.select_by_visible_text(option)

    def set_inputs(self):
        self.set_media(camera_1, fake_device)
        self.set_media(camera_2, fake_device)
        self.set_media(camera_3, fake_device)
        self.set_media(audio, fake_audio)

    def go_live(self):
        sleep(1)
        on_live = False
        get_element_by_xpath(self.driver, go_live).click()
        while on_live is False:
            try:
                get_element_by_xpath(self.driver, end_stream)
                on_live = True
                break
            except:
                sleep(0.5)

    def add_listings(self):
        i = 0
        while i < args_list[0]:
            sleep(1)
            # self.create_pick_spot_set_price(args_list[1])
            # self.create_pick_spot_auction(args_list[2])
            self.create_random_set_price_listing(args_list[3])
            # self.create_random_auction(args_list[4])
            i += 1

    def run_a_listing(self):
        sleep(1)
        get_elements_by_xpath(self.driver, listings_list)[0].click()
