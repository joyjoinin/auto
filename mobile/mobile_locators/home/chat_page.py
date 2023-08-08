from utils.common import LocatorInfo

message_title = LocatorInfo('accessibility id', 'Messages')
add_chat = LocatorInfo(locator='//XCUIElementTypeButton[@name="chatAdd"]')
empty_chat_page = LocatorInfo(locator='(//XCUIElementTypeStaticText[@name="ChatChannelListView"])[1]')

# new message
cancel_add_message = LocatorInfo('accessibility id', 'Cancel')
new_message_title = LocatorInfo('accessibility id', 'New Message')
message_search_bar = LocatorInfo('class name', 'XCUIElementTypeTextField')
clear_message_search_bar = LocatorInfo(locator='//XCUIElementTypeButton[@name="SearchBar"]')
message_welcome = LocatorInfo('accessibility id', 'Helloooooo?')