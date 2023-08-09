from utils.common_mobile import LocatorInfo

home_navigation_bar = LocatorInfo(
    locator='//XCUIElementTypeNavigationBar[@name="_TtGC7SwiftUI32NavigationStackHosting"]')
home = LocatorInfo('accessibility id', 'Home')
profile = LocatorInfo('accessibility id', 'Profile')
complete_profile = LocatorInfo('accessibility id', 'Complete your profile')
close_complete_profile = LocatorInfo('accessibility id', 'Close')
view_all = LocatorInfo('accessibility id', 'View all')
view_all_xpath = LocatorInfo(locator='//XCUIElementTypeStaticText[@name="View all"]')
complete_and_ready = LocatorInfo()
search_on_homepage = LocatorInfo(locator='//XCUIElementTypeButton[@name="magnifyingGlass"]')
chat_on_homepage = LocatorInfo(locator='//XCUIElementTypeButton[@name="chatBubbleEmpty"]')
you_might_also_like = LocatorInfo('accessibility id', 'sectionheaderYouMightAlsoLike')
you_might_also_like_xpath = LocatorInfo(locator='//XCUIElementTypeStaticText[@name="sectionheaderYouMightAlsoLike"]')
recommend_location = LocatorInfo(locator='//XCUIElementTypeStaticText[@name="sectionheaderYouMightAlsoLike"]/following'
                                         '-sibling::XCUIElementTypeOther')
recommend_shops_to_follow = LocatorInfo(locator='(//XCUIElementTypeButton[@name="Follow"])')
recommend_shops_already_following = LocatorInfo(locator='(//XCUIElementTypeButton[@name="Following"])')