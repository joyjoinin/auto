from selenium.webdriver.support.ui import WebDriverWait


def get_element(driver, locator, wait_time=10):
    try:
        element = WebDriverWait(driver, wait_time).until(
            lambda x: x.find_element(by=locator.type, value=locator.locator)
        )
        return element

    except Exception as e:
        raise e


def get_elements(driver, locator, wait_time=10):
    try:
        elements = WebDriverWait(driver, wait_time).until(
            lambda x: x.find_elements(by=locator.type, value=locator.locator)
        )
        return elements

    except Exception as e:
        raise e


def get_element_by_xpath(driver, locator, wait_time=10):
    try:
        element = WebDriverWait(driver, wait_time).until(
            lambda x: x.find_element(by='xpath', value=locator.locator)
        )
        return element

    except Exception as e:
        raise e


def get_elements_by_xpath(driver, locator, wait_time=10):
    try:
        elements = WebDriverWait(driver, wait_time).until(
            lambda x: x.find_elements(by='xpath', value=locator.locator)
        )
        return elements

    except Exception as e:
        raise e

