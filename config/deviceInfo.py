import subprocess
import plistlib


def get_device_info():
    command = ['ideviceinfo', '-x']
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
                   'app': 'Fanatics Live.ipa'}

    return device_info
