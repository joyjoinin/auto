import unittest

from testcase.profile.test_card import TestCard

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCard)
    unittest.TextTestRunner(verbosity=2).run(suite)
