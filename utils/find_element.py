from selenium.webdriver.support.ui import WebDriverWait


def get_element(driver, locator):
    try:
        element = WebDriverWait(driver, 5).until(
            lambda x: x.find_element(by=locator.type, value=locator.locator)
        )
        return element

    except Exception as e:
        raise e


def get_elements(driver, locator_type, locator_expression):
    try:
        elements = WebDriverWait(driver, 5).until(
            lambda x: x.find_element(by=locator_type, value=locator_expression)
        )
        return elements

    except Exception as e:
        raise e


def get_element_by_xpath(driver, locator):
    try:
        element = WebDriverWait(driver, 5).until(
            lambda x: x.find_element(by='xpath', value=locator.locator)
        )
        return element

    except Exception as e:
        raise e


def get_elements_by_xpath(driver, locator_expression):
    try:
        elements = WebDriverWait(driver, 5).until(
            lambda x: x.find_element(by='xpath', value=locator_expression)
        )
        return elements

    except Exception as e:
        raise e

