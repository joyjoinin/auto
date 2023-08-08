from utils.find_element import get_element_attr_by_xpath, get_element_attr
from appium.webdriver.common.touch_action import TouchAction


class CommonActions:

    def __init__(self, driver) -> None:
        self.driver = driver

    def common_swipe_vertical(self, element, direction):
        text_location = element.location
        text_size = element.size
        target_y = text_location['y'] + text_size['height'] / 2
        target_x = text_location['x'] + text_size['width'] / 2
        touch_action = TouchAction(self.driver)
        touch_action.press(x=target_x, y=target_y).wait(200).move_to(x=target_x, y=target_y + direction)
        touch_action.release().perform()

    def common_swipe_horizontal(self, element, direction):
        text_location = element.location
        text_size = element.size
        target_y = text_location['y'] + text_size['height'] / 2
        target_x = text_location['x'] + text_size['width'] / 2
        touch_action = TouchAction(self.driver)
        touch_action.press(x=target_x, y=target_y).wait(200).move_to(x=target_x + direction, y=target_y)
        touch_action.release().perform()

    def get_attr_xpath(self, locator, attr):
        return get_element_attr_by_xpath(self.driver, locator, attr)

    def get_attr(self, locator, attr):
        return get_element_attr(self.driver, locator, attr)

    def get_price(self, locator):
        return float('{:.2f}'.format(float(self.get_attr_xpath(locator, 'label').replace('$', '').replace(',', ''))))
