import subprocess
from utils.logger_config import logger


def get_connected_devices():
    adb_path = "//home/user/Android/Sdk/platform-tools/adb"
    devices_output = subprocess.check_output([adb_path, 'devices']).decode().splitlines()
    devices = [device.split('\t')[0] for device in devices_output[1:] if '\tdevice' in device]
    return devices[0] if devices else None


def android_get_desired_capabilities():
    log = logger()

    udid = get_connected_devices()

    if udid:
        log.info("Device found: {}".format(udid))
        desired_caps = {
            'autoGrantPermissions': True,
            'automationName': 'uiautomator2',
            'newCommandTimeout': 500,
            'noSign': True,
            'platformName': 'Android',
            'platformVersion': '11',
            'resetKeyboard': True,
            'systemPort': 8301,
            'takesScreenshot': True,
            'udid': udid,
            'appPackage': 'com.ajaxsystems',
            'appActivity': 'com.ajaxsystems.ui.activity.LauncherActivity'
        }
        return desired_caps
    else:
        log.error("Device not found.")
        print("Device not found.")
        return {}
