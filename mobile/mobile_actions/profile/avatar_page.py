import random
from utils.find_element import get_element, get_element_by_xpath, get_elements_by_xpath
from typing import NoReturn
from mobile.mobile_locators.profile.avatar_page import *


class AvatarActions:

    def __init__(self, driver) -> None:
        self.driver = driver

    def tap_camera_add(self) -> NoReturn:
        get_element(self.driver, camera_add).click()

    def tap_add_media_image(self) -> NoReturn:
        get_element(self.driver, add_media_image).click()

    def tap_avatar_colorful(self) -> NoReturn:
        all_avatar = get_elements_by_xpath(self.driver, avatar_colorful)
        select_index = random.randint(0, len(all_avatar) - 1)
        all_avatar[select_index].click()

    def tap_save_avatar(self) -> NoReturn:
        get_element_by_xpath(self.driver, save_avatar).click()