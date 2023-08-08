from time import sleep
from selenium.webdriver.support.ui import Select
from utils.common import get_random_username, get_image_path
from utils.find_element import get_element, get_element_by_xpath, get_elements_by_xpath
from web.web_locator_info import *


class Actions:

    def __init__(self, driver) -> None:
        self.driver = driver

    def login(self):
        self.driver.get("https://zerocool:XQZlx6iprxItlugXiiYcTp@dev.fanatics.live")
        self.driver.maximize_window()
        sleep(2)

    def sign_in(self):
        get_element(self.driver, login).click()
        get_element(self.driver, username).send_keys('joy@57blocks.com')
        get_element(self.driver, user_password).send_keys('joy159753ty,.')
        get_element(self.driver, sign_in).click()
        sleep(2)
        self.driver.get('https://dev.fanatics.live/shops/fanatics-live/manage')

    def schedule_a_show(self):
        title_name = get_random_username()
        new_path = get_image_path()
        get_element(self.driver, schedule_a_show).click()
        get_element(self.driver, title).send_keys('Auto' + title_name )
        sleep(2)
        upload_file = get_element(self.driver, upload)
        upload_file.send_keys(new_path)
        sleep(2)
        get_element(self.driver, date).send_keys('0020230808')
        get_element(self.driver, time).send_keys('0808AM')
        channel_dropdown = get_element(self.driver, channel)
        channel_dropdown.click()
        select = Select(channel_dropdown)
        select.select_by_visible_text("joy test auction channel")
        creator_dropdown = get_element(self.driver, creator)
        creator_dropdown.click()
        select = Select(creator_dropdown)
        select.select_by_visible_text("joy@57blocks.com")
        get_element_by_xpath(self.driver, add_listing).click()

    def create_random_set_price_listing(self):
        title_name = get_random_username()
        list_title = 'AutoTest random_set_price' + title_name
        sleep(2)
        get_element(self.driver,listing_title).send_keys(list_title)
        sleep(1)
        option_dropdown = get_element(self.driver,select_an_option)
        option_dropdown.click()
        select = Select(option_dropdown)
        select.select_by_visible_text('NBA 30 Team')
        sleep(1)
        get_element_by_xpath(self.driver,random).click()
        sleep(1)
        get_element_by_xpath(self.driver,set_price).click()
        get_element(self.driver, price_per_spot).send_keys(999)
        sleep(1)
        get_element_by_xpath(self.driver,save_listing).click()

    def create_random_auction(self):
        title_name = get_random_username()
        list_title = 'AutoTest random_set_price' + title_name
        sleep(2)
        get_element(self.driver, listing_title).send_keys(list_title)
        sleep(1)
        option_dropdown = get_element(self.driver,select_an_option)
        option_dropdown.click()
        select = Select(option_dropdown)
        select.select_by_visible_text('NBA 30 Team')
        sleep(1)
        get_element_by_xpath(self.driver,random).click()
        sleep(1)
        get_element_by_xpath(self.driver,auction).click()
        get_element(self.driver, min_bid).send_keys(999)
        sleep(1)
        get_element_by_xpath(self.driver,save_listing).click()

    def create_pick_spot_auction(self):
        title_name = get_random_username()
        list_title = 'AutoTest random_set_price' + title_name
        sleep(2)
        get_element(self.driver, listing_title).send_keys(list_title)
        sleep(1)
        option_dropdown = get_element(self.driver,select_an_option)
        option_dropdown.click()
        select = Select(option_dropdown)
        select.select_by_visible_text('NBA 30 Team')
        sleep(1)
        get_element_by_xpath(self.driver,pick_your_spot).click()
        sleep(1)
        get_element_by_xpath(self.driver,auction).click()
        get_element(self.driver, min_bid).send_keys(999)
        sleep(1)
        get_element_by_xpath(self.driver,save_listing).click()

    def create_pick_spot_set_price(self):
        title_name = get_random_username()
        list_title = 'AutoTest random_set_price' + title_name
        sleep(2)
        get_element(self.driver, listing_title).send_keys(list_title)
        sleep(1)
        option_dropdown = get_element(self.driver, select_an_option)
        option_dropdown.click()
        select = Select(option_dropdown)
        select.select_by_visible_text('NBA 30 Team')
        sleep(1)
        get_element_by_xpath(self.driver, pick_your_spot).click()
        sleep(1)
        get_element_by_xpath(self.driver, set_price).click()
        sleep(1)
        get_element(self.driver,assign_price).click()
        sleep(1)
        spots = get_elements_by_xpath(self.driver,assign_list)
        for spot in spots:
            spot.send_keys(999)
            sleep(0.5)
        get_element(self.driver,assign_prices).click()
        sleep(1)
        get_element_by_xpath(self.driver, save_listing).click()

    def publish(self):
        sleep(1)
        get_element_by_xpath(self.driver,publish).click()
