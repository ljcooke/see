"""
Unit tests for the see.tools module.

"""
try:
    import unittest2 as unittest
except ImportError:
    import unittest

from see import tools


class TestToolsModule(unittest.TestCase):

    def test_filter_by_regex(self):
        # Arrange
        names = ["george", "helen"]
        pat_wildcard = "e.*g"
        pat_start = "^h"
        pat_end = "n$"

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

    def test_filter_by_wildcard(self):
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


if __name__ == '__main__':
    unittest.main()
