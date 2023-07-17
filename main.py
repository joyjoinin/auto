import shutil
from datetime import datetime
from pathlib import Path

import pytest
import os
import subprocess

testcase_file = {
    './testcase/account_creation/test_create_account.py': True
}
now = datetime.now()
dt_string = now.strftime("%Y_%m_%d_%H_%M_%S")
report_summary_folder = 'report/report_results/{}'.format(dt_string)
html_summary_folder = 'report/report_html/{}'.format(dt_string)

if __name__ == '__main__':

    pytest.main(['./testcase/login_logout/test_login_logout.py','--capture=sys','-q','--alluredir',report_summary_folder])