from appium import webdriver
import subprocess
import plistlib

# from deviceInfo import get_device_info

def get_driver():
    caps = webdriver.webdriver.AppiumOptions()
    # device_info = get_device_info()
    # for i in device_info.keys():
    #     caps.set_capability(i,device_info[i])
    caps.set_capability("platformName", "iOS")
    caps.set_capability("appium:automationName", "XCUITest")
    caps.set_capability("appium:noReset", True)
    caps.set_capability("appium:udid", "93C67BC8-E00B-42DA-B10C-D6C7418E5547")
    caps.set_capability("appium:includeSafariInWebviews", True)
    caps.set_capability("appium:newCommandTimeout", 3600)
    caps.set_capability("appium:connectHardwareKeyboard", True)
    driver = webdriver.Remote(
        command_executor='http://127.0.0.1:4723',
        options=caps
    )
    return driver
