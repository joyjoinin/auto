from utils.common_mobile import LocatorInfo

loading_status = LocatorInfo(locator='(//XCUIElementTypeActivityIndicator[@name="In progress"])[1]')
close_live = LocatorInfo('accessibility id', 'cancelShadow')
signal = LocatorInfo('accessibility id', 'antennaSignalShadow')
signal_value = LocatorInfo(
    locator='//XCUIElementTypeImage[@name="antennaSignalShadow"]/following-sibling::XCUIElementTypeStaticText')
shop_avatar = LocatorInfo(
    locator='//XCUIElementTypeApplication[@name="Fanatics Live Development"]/XCUIElementTypeWindow/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeButton[2]')
flag = LocatorInfo('accessibility id', 'flagShadow')
share = LocatorInfo('accessibility id', 'shareIosShadow')
schedule = LocatorInfo('accessibility id', 'shopAlt')
input_message = LocatorInfo('class name', 'XCUIElementTypeTextField')
send_message = LocatorInfo(locator='(//XCUIElementTypeButton[@name="ChatChannelView"])[1]')
latest_message = LocatorInfo(locator='(//XCUIElementTypeOther[@name="MessageContainerView"])[1]//XCUIElementTypeStaticText[last()]')
error_message_for_too_long = LocatorInfo(locator='(//XCUIElementTypeStaticText[@name="SystemMessageView"])[1]')
live_name_location = LocatorInfo('accessibility id')
first_card_location = LocatorInfo(
    locator='//XCUIElementTypeApplication[@name="Fanatics Live Development"]/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther/XCUIElementTypeImage[1]')
live = LocatorInfo('accessibility id', 'LIVE')