from utils.common_mobile import LocatorInfo

button_new_stream_added = LocatorInfo(locator='//XCUIElementTypeSwitch[@name="New stream added, Your favorite channel '
                                              'scheduled something new"]/XCUIElementTypeSwitch')
button_stream_going_live = LocatorInfo(
    locator='//XCUIElementTypeSwitch[@name="Stream going live, A stream is starting now"]/XCUIElementTypeSwitch')
button_giveaways = LocatorInfo(
    locator='//XCUIElementTypeSwitch[@name="Giveaways, Your chance at something great — for free!"]/XCUIElementTypeSwitch')
button_suggested_streams = LocatorInfo(
    locator='//XCUIElementTypeSwitch[@name="Suggested streams, We found something we think you’ll like"]/XCUIElementTypeSwitch')
button_push_notifications = LocatorInfo(
    locator='//XCUIElementTypeSwitch[@name="Push Notifications"]/XCUIElementTypeSwitch')
button_email = LocatorInfo(locator='//XCUIElementTypeSwitch[@name="Email"]/XCUIElementTypeSwitch')
back_to_notifications = LocatorInfo('accessibility id', 'Notifications')