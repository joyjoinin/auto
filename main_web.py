# coding = utf-8

import pytest

testcase_file = {
    './testcase/web/create_live.py': True,
}
if __name__ == '__main__':
    for case, flag in testcase_file.items():
        if flag:
            pytest.main([case])