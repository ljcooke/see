#!/usr/bin/env python
"""
Unit tests to simulate non-Unixlike environments where we can't easily get
information about the terminal.

To do this, we prevent Python from importing some modules while it loads see.

"""
import sys

try:
    import unittest2 as unittest
except ImportError:
    import unittest

try:
    import builtins  # Python 3
except ImportError:
    import __builtin__ as builtins  # Python 2

#------------------------------------------------------------------------------

DISABLED_MODULES = (
    'fcntl',
    'termios',
)

PY3 = sys.version_info >= (3, 0)

real_import = builtins.__import__

def mock_import(name,
                globals=None if PY3 else {},
                locals=None if PY3 else {},
                fromlist=None if PY3 else [],
                level=0 if PY3 else -1):
    if name in DISABLED_MODULES:
        raise ImportError
    return real_import(name, globals, locals, fromlist, level)

import see

#------------------------------------------------------------------------------

class TestNonUnixlike(unittest.TestCase):

    def setUp(self):
        builtins.__import__ = mock_import
        reload(see)
        builtins.__import__ = real_import

    def tearDown(self):
        reload(see)

    def test_import_success(self):
        reload(see)
        self.assertIsNotNone(see.fcntl)
        self.assertIsNotNone(see.termios)

    def test_import_fail(self):
        self.assertIsNone(see.fcntl)
        self.assertIsNone(see.termios)

    def test_term_width_not_available(self):
        term_width = see.term_width()

        self.assertIsNone(term_width)

    def test_default_line_width(self):
        line_width = see.line_width()

        self.assertEqual(line_width, see.DEFAULT_LINE_WIDTH)


if __name__ == '__main__':
    unittest.main()
