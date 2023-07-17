import pytest
from datetime import datetime
testcase_file = {
    './testcase/account_creation/test_create_account.py': False,
    './testcase/login_logout/test_login_logout.py': True,
    './testcase/profile/test_card.py': False,
    './testcase/profile/test_shipping_address.py': False
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
