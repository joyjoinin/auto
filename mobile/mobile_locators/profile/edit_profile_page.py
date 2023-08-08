from utils.common import LocatorInfo

edit_avatar = LocatorInfo(locator='//XCUIElementTypeImage[@name="pencil"]')
edit_username = LocatorInfo(locator='(//XCUIElementTypeButton[@name="pencil"])[1]')
profile_username = LocatorInfo(locator='//XCUIElementTypeStaticText['
                                       '@name="Username"]/following-sibling::XCUIElementTypeStaticText')
edit_self_intro = LocatorInfo(locator='(//XCUIElementTypeButton[@name="pencil"])[2]')
profile_self_intro = LocatorInfo(locator='//XCUIElementTypeStaticText['
                                         '@name="Biography"]/following-sibling::XCUIElementTypeStaticText')
add_interests = LocatorInfo('accessibility id', 'plusClear')
all_interests = LocatorInfo(
    locator='//XCUIElementTypeStaticText[@name="My '
            'Interests"]/following-sibling::XCUIElementTypeOther/XCUIElementTypeStaticText')