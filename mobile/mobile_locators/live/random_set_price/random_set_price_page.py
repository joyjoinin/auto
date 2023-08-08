from utils.common import LocatorInfo

spots_randomly = LocatorInfo('accessibility id', 'Spots randomly assigned')
spot_price = LocatorInfo(locator='//XCUIElementTypeStaticText[@name="Price"]/following-sibling::*[2]')
random_title = LocatorInfo(locator='(//XCUIElementTypeStaticText[@name="Random"])[1]')
spots_value_button = LocatorInfo('class name', 'XCUIElementTypeStepper')
buy_spots_button = LocatorInfo(
    locator='//XCUIElementTypeApplication[@name="Fanatics Live Development"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeStepper/following-sibling::XCUIElementTypeButton')
