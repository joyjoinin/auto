from utils.common_mobile import LocatorInfo

auction_type_is_pick = LocatorInfo('accessibility id', 'Pick your favorite team')
auction_soon = LocatorInfo('accessibility id', 'Auction starting soon')
view_spot = LocatorInfo('accessibility id', 'View Spots')
auction_failed = LocatorInfo('accessibility id', 'False start. The auction will restart shortly.')
custom_bid = LocatorInfo('accessibility id', 'Custom bid')
bid_button = LocatorInfo(locator='//XCUIElementTypeButton[@name="Custom bid"]/following-sibling::*[2]')