from selenium import webdriver
from time import sleep

from utils.find_element import *
from utils.web_utils.web_locator_info import *

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://zerocool:XQZlx6iprxItlugXiiYcTp@dev.fanatics.live")
driver.maximize_window()
sleep(5)
get_element(driver,login).click()
get_element(driver,username).send_keys('joy@57blocks.com')
get_element(driver,user_password).send_keys('joy159753ty,.')
get_element(driver,sign_in).click()
sleep(2)
driver.get('https://dev.fanatics.live/shops/fanatics-live/manage')
# get_element(driver,schedule_a_show).click()
# sleep(1)
# get_element(driver,title).send_keys('joy test')
# get_element(driver,date).send_keys('0020230808')
# upload_file = get_element(driver,upload)
# upload_file.send_keys(r'C:\Users\57block\Desktop\test.jpg')
# get_element(driver,time).send_keys('0808AM')
# channel_dropdown = get_element(driver,channel)
# channel_dropdown.click()
# select = Select(channel_dropdown)
# select.select_by_visible_text("joy test auction channel")
# creator_dropdown = get_element(driver,creator)
# creator_dropdown.click()
# select = Select(creator_dropdown)
# select.select_by_visible_text("joy@57blocks.com")
# get_element_by_xpath(driver,add_listing).click()
# sleep(10)