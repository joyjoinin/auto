from utils.common_mobile import LocatorInfo

back_to_score = LocatorInfo(locator='(//XCUIElementTypeButton[@name="Back"])[2]')
order_details_title = LocatorInfo(locator='//XCUIElementTypeStaticText[@name="Order details"]')
order_date = LocatorInfo(
    locator='//XCUIElementTypeStaticText[@name="Date"]/following-sibling::XCUIElementTypeStaticText')
order_id = LocatorInfo(
    locator='//XCUIElementTypeStaticText[@name="Order #"]/following-sibling::XCUIElementTypeStaticText')
order_stream = LocatorInfo(
    locator='//XCUIElementTypeStaticText[@name="Stream"]/following-sibling::XCUIElementTypeStaticText')
order_spot = LocatorInfo(
    locator='//XCUIElementTypeStaticText[@name="Spot"]/following-sibling::XCUIElementTypeStaticText')
order_status = LocatorInfo(
    locator='//XCUIElementTypeStaticText[@name="Status"]/following-sibling::XCUIElementTypeStaticText')
order_seller = LocatorInfo(
    locator='//XCUIElementTypeStaticText[@name="Seller"]/following-sibling::XCUIElementTypeStaticText')
order_spot_name = LocatorInfo(locator='//XCUIElementTypeStaticText[@name="Order '
                                      'summary"]/following-sibling::XCUIElementTypeStaticText')
order_price = LocatorInfo(locator='//XCUIElementTypeStaticText[@name="Order summary"]/preceding-sibling::*[-2]')
order_subtotal = LocatorInfo(locator='//XCUIElementTypeStaticText[@name="Subtotal"]/preceding-sibling::*[-1]')
order_shipping = LocatorInfo(
    locator='//XCUIElementTypeStaticText[@name="Shipping"]/following-sibling::XCUIElementTypeStaticText')
order_tax = LocatorInfo(locator='//XCUIElementTypeStaticText[@name="Tax"]/following-sibling::XCUIElementTypeStaticText')
order_insurance = LocatorInfo(
    locator='//XCUIElementTypeStaticText[@name="Insurance"]/following-sibling::XCUIElementTypeStaticText')
order_total = LocatorInfo(
    locator='//XCUIElementTypeStaticText[@name="Total"]/following-sibling::XCUIElementTypeStaticText')
order_shipping_address = LocatorInfo(
    locator='//XCUIElementTypeStaticText[@name="Shipping address"]/following-sibling::XCUIElementTypeStaticText')
order_shipping_method = LocatorInfo(
    locator='//XCUIElementTypeStaticText[@name="Shipping method"]/following-sibling::XCUIElementTypeStaticText')
order_tracking_number = LocatorInfo(
    locator='//XCUIElementTypeStaticText[@name="Tracking number"]/following-sibling::XCUIElementTypeStaticText')
order_billing_method = LocatorInfo(
    locator='//XCUIElementTypeStaticText[@name="Billing method"]/following-sibling::XCUIElementTypeStaticText')
contact_fanatics_live = LocatorInfo('accessibility id', 'Contact Fanatics Live')
