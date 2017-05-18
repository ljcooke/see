"""
Unit tests for getting the terminal width.

There are separate test cases to simulate unsupported environments (not
Unixlike or Windows), where information about the terminal is not easily
available. To do this, we prevent Python from importing some modules while it
loads see.

"""
import platform
import sys
from imp import reload

try:
    import unittest2 as unittest
except ImportError:
    import unittest

try:
    import unittest.mock as mock
except ImportError:
    import mock

try:
    import builtins  # Python 3
except ImportError:
    import __builtin__ as builtins  # Python 2

import see
from see import term


MOCK_EXCLUDE_MODULES = (
    'ctypes',
    'fcntl',
    'termios',
)

PY3 = sys.version_info >= (3, 0)

REAL_IMPORT = builtins.__import__


def mock_import(name,
                globals=None if PY3 else {},
                locals=None if PY3 else {},
                fromlist=None if PY3 else [],
                level=0 if PY3 else -1):
    if name in MOCK_EXCLUDE_MODULES:
        raise ImportError
    return REAL_IMPORT(name, globals, locals, fromlist, level)


class TestSupportedTerminal(unittest.TestCase):

    def setUp(self):
        self.system = platform.system()
        self.windows = (self.system == 'Windows')

    def test_system(self):
        self.assertTrue(self.system, 'System/OS name could not be determined')

    def test_import_success(self):
        if self.windows:
            self.assertIsNone(term.fcntl)
            self.assertIsNone(term.termios)
            self.assertIsNotNone(term.windll)
            self.assertIsNotNone(term.create_string_buffer)
        else:
            self.assertIsNotNone(term.fcntl)
            self.assertIsNotNone(term.termios)
            self.assertIsNone(term.windll)
            self.assertIsNone(term.create_string_buffer)

    def test_term_width(self):
        width = term.term_width()

        self.assertIsNotNone(width)

        # Note: terminal info is not available in Travis
        # self.assertGreater(width, 0)

    def test_ioctl_fail(self):
        if self.windows:
            return

        package = 'see.term.fcntl.ioctl'
        with mock.patch(package, side_effect=IOError('')) as patch:
            width = term.term_width()

            self.assertIsNone(width)

    def test_indent_to_prompt(self):
        if hasattr(sys, 'ps1'):
            self.fail('expected sys.ps1 to be absent during unit testing')

        # Arrange
        sys.ps1 = '[arbitrary prompt string]'

        # Act
        out = see.see()
        indent = len(str(out)) - len(str(out).lstrip())

        # Assert
        self.assertEqual(indent, len(sys.ps1))


class TestMockWindowsTerminal(unittest.TestCase):

    def setUp(self):
        builtins.__import__ = mock_import
        reload(term)

    def tearDown(self):
        builtins.__import__ = REAL_IMPORT
        reload(term)


class TestMockUnsupportedTerminal(unittest.TestCase):

    def setUp(self):
        builtins.__import__ = mock_import
        reload(term)

    def tearDown(self):
        builtins.__import__ = REAL_IMPORT
        reload(term)

    def test_import_fail(self):
        self.assertIsNone(term.fcntl)
        self.assertIsNone(term.termios)

    def test_term_width_not_available(self):
        term_width = term.term_width()

        self.assertIsNone(term_width)

    def test_default_line_width(self):
        line_width = term.line_width()

        self.assertEqual(line_width, term.DEFAULT_LINE_WIDTH)
