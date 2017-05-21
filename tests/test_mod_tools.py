"""
Unit tests for the see.tools module.

"""
import re

try:
    import unittest2 as unittest
except ImportError:
    import unittest

from see import tools


class TestToolsModule(unittest.TestCase):

    def test_compact(self):
        # Arrange
        items = [0, 1, '', 'foo', True, False, [], ['a'], {}, {1: 2}]
        expected = (1, 'foo', True, ['a'], {1: 2})

        # Act
        compacted = tools.compact(items)

        # Assert
        self.assertEqual(compacted, expected)

    def test_filter_regex(self):
        # Arrange
        names = ["george", "helen"]
        pat_wildcard = re.compile("e.*g")
        pat_start = re.compile("^h")
        pat_end = re.compile("n$")

        # Act
        out_wildcard = tools.filter_regex(names, pat_wildcard)
        out_start = tools.filter_regex(names, pat_start)
        out_end = tools.filter_regex(names, pat_end)

        # Assert
        self.assertIsInstance(out_wildcard, tuple)
        self.assertIsInstance(out_start, tuple)
        self.assertIsInstance(out_end, tuple)
        self.assertEqual(out_wildcard, ("george",))
        self.assertEqual(out_start, ("helen",))
        self.assertEqual(out_end, ("helen",))

    def test_filter_wildcard(self):
        # Arrange
        names = ["george", "helen"]
        pat_wildcard = "*or*"
        pat_single = "h?l?n"
        pat_partial = "e*"

        # Act
        out_wildcard = tools.filter_wildcard(names, pat_wildcard)
        out_single = tools.filter_wildcard(names, pat_single)
        out_partial = tools.filter_wildcard(names, pat_partial)

        # Assert
        self.assertIsInstance(out_wildcard, tuple)
        self.assertIsInstance(out_single, tuple)
        self.assertIsInstance(out_partial, tuple)
        self.assertEqual(out_wildcard, ("george",))
        self.assertEqual(out_single, ("helen",))
        self.assertEqual(out_partial, ())
