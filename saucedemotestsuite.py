import unittest
from test_cart import OpenSauceCart
from test_login import OpenSauceLogin

open_sauce_cart = unittest.TestLoader().loadTestsFromTestCase(OpenSauceCart)
open_sauce_login = unittest.TestLoader().loadTestsFromTestCase(OpenSauceLogin)

test_suite = unittest.TestSuite([open_sauce_cart, open_sauce_login])

unittest.TextTestRunner(verbosity=2).run(test_suite)