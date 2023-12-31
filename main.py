import os
import subprocess
import time
import pytest
from datetime import datetime
from utils.mobile.common import get_file_direction, kill_appium

testcase_file = {
    './testcase/mobile/account_creation/test_create_account.py': True,
    './testcase/mobile/account_creation/test_username_creation.py': True,
    './testcase/mobile/login_logout/test_login_logout.py': True,
    './testcase/mobile/login_logout/test_login_page_functions.py': True,
    './testcase/mobile/login_logout/test_login_with_error_info.py': True,
    './testcase/mobile/home/test_dm.py': True,
    './testcase/mobile/home/test_hero_card.py': True,
    './testcase/mobile/home/test_logos.py': False,
    './testcase/mobile/home/test_search.py': True,
    './testcase/mobile/home/test_view_all.py': True,
    './testcase/mobile/home/test_you_might_also_like.py': True,
    './testcase/mobile/profile/test_edit_profile.py': True,
    './testcase/mobile/profile/test_favorite_shops.py': False,
    './testcase/mobile/profile/test_follow.py': True,
    './testcase/mobile/profile/test_invite_friends.py': False,  # disabled
    './testcase/mobile/profile/test_share_profile.py': True,
    './testcase/mobile/settings/test_become_a_seller.py': True,
    './testcase/mobile/settings/test_contact_us.py': True,
    './testcase/mobile/settings/test_faqs.py': True,
    './testcase/mobile/settings/test_notification.py': True,
    './testcase/mobile/settings/test_privacy_policy.py': True,
    './testcase/mobile/settings/test_purchases.py': True,
    './testcase/mobile/wallet_addresses/test_card.py': True,
    './testcase/mobile/wallet_addresses/test_shipping_address.py': True,
    './testcase/mobile/wallet_addresses/test_complete_profile.py': True,
}
os.environ['PATH'] = '/usr/local/bin:' + os.environ['PATH']
now = datetime.now()
dt_string = now.strftime("%Y_%m_%d_%H_%M_%S")
report_summary_folder = 'report/report_results/{}'.format(dt_string)
html_summary_folder = 'report/report_html/{}'.format(dt_string)
appium_process = subprocess.Popen([get_file_direction('appium')])
time.sleep(5)

if __name__ == '__main__':
    os.mkdir(report_summary_folder)
    os.mkdir(html_summary_folder)
    for case, flag in testcase_file.items():
        if flag:
            pytest.main([case, '--capture=sys', '-q', '--alluredir', report_summary_folder, '--reruns=5'])
        else:
            print('skip test for {}'.format(case))
    result_dir = report_summary_folder
    report_dir = html_summary_folder
    file_direction = get_file_direction('allure')
    cmd = [file_direction, "generate", result_dir, "-o", report_dir, '--clean']
    subprocess.run(cmd, check=True)
    kill_appium()

