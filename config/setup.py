import pytest
from appium import webdriver
import subprocess
import plistlib


def get_driver_on_real_device():
    caps = webdriver.webdriver.AppiumOptions()
    device_info = get_device_info(get_app_name())
    for i in device_info.keys():
        caps.set_capability(i, device_info[i])
    driver = webdriver.Remote(
        command_executor='http://127.0.0.1:4723',
        options=caps
    )
    return driver


def get_driver():
    caps = webdriver.webdriver.AppiumOptions()
    caps.set_capability("platformName", "iOS")
    caps.set_capability("appium:automationName", "XCUITest")
    caps.set_capability("appium:noReset", True)
    caps.set_capability("appium:udid", "93C67BC8-E00B-42DA-B10C-D6C7418E5547")
    caps.set_capability("appium:includeSafariInWebviews", True)
    caps.set_capability("appium:newCommandTimeout", 3600)
    caps.set_capability("appium:connectHardwareKeyboard", True)
    caps.set_capability("appium:enablePerformanceLogging", True)
    driver = webdriver.Remote(
        command_executor='http://127.0.0.1:4723',
        options=caps
    )
    return driver


# make sure installed unique app version
def get_app_name():
    command = ['/usr/local/bin/ideviceinstaller', '-l', '-o', 'list_user']
    output = subprocess.check_output(command, universal_newlines=True)

    app_list = []
    lines = output.strip().split('\n')
    for line in lines:
        if 'live.fanatics' in line:
            app_list.append(line.split(',')[0])

    return app_list


def get_simulator_devices():
    command = ['xcrun', 'simctl', 'list']
    output = subprocess.check_output(command, universal_newlines=True)

    devices_list = []
    lines = output.strip().split('\n')
    for line in lines:
        if 'iPhone' in line:
            devices_list.append(line)

    return devices_list


def get_device_info(app):
    command = ['/usr/local/bin/ideviceinfo', '-x']
    output = subprocess.check_output(command)

    plist_data = plistlib.loads(output)
    device_info = {'appium:platformVersion': plist_data.get('ProductVersion'),
                   'appium:deviceName': plist_data.get('ProductType'),
                   'appium:udid': plist_data.get('UniqueDeviceID'),
                   'platformName': 'iOS',
                   'appium:automationName': 'XCUITest',
                   'appium:noReset': True,
                   'appium:includeSafariInWebviews': True,
                   'appium:connectHardwareKeyboard': True,
                   'appium:newCommandTimeout': 3600,
                   'appium:enablePerformanceLogging': True,
                   'app': app}

    return device_info
