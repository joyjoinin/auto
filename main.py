import pytest
from datetime import datetime
testcase_file = {
    './testcase/account_creation/test_create_account.py': True,
    './testcase/account_creation/test_username_creation.py': True,
    './testcase/login_logout/test_login_logout.py': True,
    './testcase/login_logout/test_login_page_functions.py': True,
    './testcase/login_logout/test_login_with_wrong_info.py': True,
    './testcase/profile/test_edit_profile.py': True,
    './testcase/profile/test_favorite_shops.py': False,
    './testcase/profile/test_follow.py': True,
    './testcase/profile/test_invite_friends.py': True,
    './testcase/settings/test_contact_us.py': True,
    './testcase/settings/test_faqs.py': True,
    './testcase/settings/test_notification.py': True,
    './testcase/settings/test_privacy_policy.py': True,
    './testcase/settings/test_purchases.py': True,
    './testcase/wallet_addresses/test_card.py': True,
    './testcase/wallet_addresses/test_shipping_address.py': True
}

now = datetime.now()
dt_string = now.strftime("%Y_%m_%d_%H_%M_%S")
report_summary_folder = 'report/report_results/{}'.format(dt_string)
html_summary_folder = 'report/report_html/{}'.format(dt_string)

if __name__ == '__main__':

    for case, flag in testcase_file.items():
        if flag:
            pass
            pytest.main([case, '--capture=sys', '-q', '--alluredir', report_summary_folder, '--reruns=3'])
        else:
            print('skip test for {}'.format(case))
