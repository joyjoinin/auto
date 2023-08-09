from utils.common_mobile import LocatorInfo

search_field = LocatorInfo(locator='//XCUIElementTypeApplication[@name="Fanatics Live '
                                   'Development"]/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther'
                                   '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                                   '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                                   '/XCUIElementTypeOther/XCUIElementTypeOther['
                                   '3]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                                   '/XCUIElementTypeOther/XCUIElementTypeTextField')
popular_streams_title = LocatorInfo('accessibility id', 'sectionheaderPopularStreams')
close_search_page = LocatorInfo(locator='//XCUIElementTypeButton[@name="Close"]')