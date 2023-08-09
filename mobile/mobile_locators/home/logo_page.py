from utils.common_mobile import LocatorInfo

logo_scroll_view = LocatorInfo(locator='//XCUIElementTypeAny[@name="Fanatics Live '
                                       'Development"]/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther'
                                       '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                                       '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                                       '/XCUIElementTypeOther/XCUIElementTypeOther['
                                       '2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                                       '/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther'
                                       '/XCUIElementTypeScrollView')

logo_items = LocatorInfo(locator='//XCUIElementTypeAny[@name="Fanatics Live '
                                 'Development"]/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther'
                                 '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                                 '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                                 '/XCUIElementTypeOther/XCUIElementTypeOther['
                                 '2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                                 '/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther'
                                 '/XCUIElementTypeScrollView/XCUIElementTypeOther/XCUIElementTypeStaticText')

logo_item = LocatorInfo('accessibility id')
logo_title = LocatorInfo('class name', 'XCUIElementTypeNavigationBar')