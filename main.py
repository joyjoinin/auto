import unittest
from testcase.login_logout.test_login_logout import TestExistedAccount
from testdebug import Test_debugs

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Test_debugs)
    unittest.TextTestRunner(verbosity=2).run(suite)
