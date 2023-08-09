from utils.common_mobile import LocatorInfo

camera_add = LocatorInfo('accessibility id', 'cameraAdd')
add_media_image = LocatorInfo('accessibility id', 'addMediaImage')
avatar_colorful = LocatorInfo(
    locator='//XCUIElementTypeButton[@name="addMediaImage"]/following-sibling::XCUIElementTypeOther'
            '/XCUIElementTypeButton')
save_avatar = LocatorInfo(locator='//XCUIElementTypeButton[@name="Save"]')