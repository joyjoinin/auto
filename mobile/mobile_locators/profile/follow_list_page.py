from utils.common_mobile import LocatorInfo

search_glass = LocatorInfo('accessibility id', 'magnifyingGlass')
following_list_title = LocatorInfo(locator='//XCUIElementTypeStaticText[@name="Following"]')
followers_list_title = LocatorInfo(locator='//XCUIElementTypeStaticText[@name="Followers"]')
empty_following_list = LocatorInfo('accessibility id', 'Hello darkness...')
empty_followers_list = LocatorInfo('accessibility id', 'Who needs followers?')