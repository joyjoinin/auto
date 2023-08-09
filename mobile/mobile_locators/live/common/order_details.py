from utils.common_mobile import LocatorInfo

cancel_order = LocatorInfo(locator='//XCUIElementTypeButton[@name="Cancel"]')
nav_arrow_down = LocatorInfo('accessibility id', 'navArrowDown')
order_total_price = LocatorInfo(
    locator='//XCUIElementTypeImage[@name="navArrowUp"]/following-sibling::XCUIElementTypeStaticText')
nav_arrow_up = LocatorInfo('accessibility id', 'navArrowUp')
gift_name = LocatorInfo(locator='//XCUIElementTypeImage[@name="Gift"]/following-sibling::*[2]')
gift_subtotal = LocatorInfo(locator='//XCUIElementTypeImage[@name="Gift"]/following-sibling::*[3]')
change_card = LocatorInfo(locator='(//XCUIElementTypeButton[@name="Change"])[1]')
change_address = LocatorInfo(locator='(//XCUIElementTypeButton[@name="Change"])[2]')
pay_now = LocatorInfo(locator='//XCUIElementTypeStaticText[@name="Pay now"]')
subtotal = LocatorInfo(
    locator='//XCUIElementTypeStaticText[@name="Subtotal"]/following-sibling::XCUIElementTypeStaticText')
shipping = LocatorInfo(
    locator='//XCUIElementTypeStaticText[@name="Shipping"]/following-sibling::XCUIElementTypeStaticText')
tax = LocatorInfo(locator='//XCUIElementTypeStaticText[@name="Tax"]/following-sibling::XCUIElementTypeStaticText')
total = LocatorInfo(locator='//XCUIElementTypeStaticText[@name="Total"]/following-sibling::XCUIElementTypeStaticText')