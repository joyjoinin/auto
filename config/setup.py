import re
import subprocess
import plistlib
from appium import webdriver
from data.params import app_environment, device_type


def get_driver_on_real_device():
    # start_wda()
    caps = webdriver.webdriver.AppiumOptions()
    device_info = get_device_info(get_app_name(app_environment))
    for i in device_info.keys():
        caps.set_capability(i, device_info[i])
    driver = webdriver.Remote(
        command_executor='http://127.0.0.1:4723',
        options=caps
    )
    return driver


def get_device_on_simulator():
    # start_wda()
    caps = webdriver.webdriver.AppiumOptions()
    caps.set_capability("platformName", "iOS")
    caps.set_capability("appium:automationName", "XCUITest")
    caps.set_capability("appium:noReset", True)
    caps.set_capability("appium:udid", "93C67BC8-E00B-42DA-B10C-D6C7418E5547")  # change device udid
    caps.set_capability("appium:includeSafariInWebviews", True)
    caps.set_capability("appium:newCommandTimeout", 3600)
    caps.set_capability("appium:connectHardwareKeyboard", True)
    caps.set_capability("appium:enablePerformanceLogging", True)
    driver = webdriver.Remote(
        command_executor='http://127.0.0.1:4723',
        options=caps
    )
    return driver

def get_driver():
    if device_type == 'Real':
        return get_driver_on_real_device()
    else:
        return get_device_on_simulator()


# make sure installed unique app version
def get_app_name(app_type):
    command = ['/usr/local/bin/ideviceinstaller', '-l', '-o', 'list_user']
    output = subprocess.check_output(command, universal_newlines=True)
    app_list = []
    lines = output.strip().split('\n')
    for line in lines:
        if 'live.fanatics' in line:
            app_list.append(line.split(',')[0])
    for app in app_list:
        if app_type in app:
            app_name = app
            return app_name


def get_simulator_devices():
    command = ['xcrun', 'simctl', 'list']
    output = subprocess.check_output(command, universal_newlines=True)

    devices_list = []
    lines = output.strip().split('\n')
    for line in lines:
        if 'iPhone' in line:
            devices_list.append(line)

    return devices_list


def get_plist_data():
    command = ['/usr/local/bin/ideviceinfo', '-x']
    output = subprocess.check_output(command)
    plist_data = plistlib.loads(output)
    return plist_data


def get_device_info(app_name):
    data = get_plist_data()
    device_info = {'appium:platformVersion': data.get('ProductVersion'),
                   'appium:deviceName': data.get('ProductType'),
                   'appium:udid': data.get('UniqueDeviceID'),
                   'platformName': 'iOS',
                   'appium:automationName': 'XCUITest',
                   'appium:noReset': True,
                   'appium:includeSafariInWebviews': True,
                   'appium:connectHardwareKeyboard': True,
                   'appium:newCommandTimeout': 3600,
                   'appium:enablePerformanceLogging': True,
                   'app': app_name}

    return device_info


def start_wda():
    device_id = get_plist_data().get('UniqueDeviceID')
    print(device_id)
    cmd = f'xcodebuild -project WebDriverAgent.xcodeproj -scheme WebDriverAgentRunner -destination id={device_id} test'
    subprocess.Popen(cmd, shell=True)


