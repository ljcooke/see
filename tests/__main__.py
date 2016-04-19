"""
Main entry point which allows the tests to be run with the command::

    python -m tests

"""
try:
    import unittest2 as unittest
except ImportError:
    import unittest

import os

loader = unittest.TestLoader()
test_suite = loader.discover(os.path.dirname(__file__))

runner = unittest.TextTestRunner()
runner.run(test_suite)
