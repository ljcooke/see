#!/usr/bin/env python
"""
Unit tests for see.py

"""
try:
    import unittest2 as unittest
except ImportError:
    import unittest

import see


class TestSee(unittest.TestCase):

    def test_line_width(self):
        # Arrange
        default_width = 1
        max_width = 1

        # Act
        width = see.line_width(default_width, max_width)

        # Assert
        self.assertIsInstance(width, int)
        self.assertEqual(width, 1)

    def test_regex_filter(self):
        # Arrange
        names = ["george", "helen"]
        pat_wildcard = "e.*g"
        pat_start = "^h"
        pat_end = "n$"

        # Act
        out_wildcard = see.regex_filter(names, pat_wildcard)
        out_start = see.regex_filter(names, pat_start)
        out_end = see.regex_filter(names, pat_end)

        # Assert
        self.assertIsInstance(out_wildcard, tuple)
        self.assertIsInstance(out_start, tuple)
        self.assertIsInstance(out_end, tuple)
        self.assertEqual(out_wildcard, ("george",))
        self.assertEqual(out_start, ("helen",))
        self.assertEqual(out_end, ("helen",))

    def test_fn_filter(self):
        # Arrange
        names = ["george", "helen"]
        pat_wildcard = "*or*"
        pat_single = "h?l?n"
        pat_partial = "e*"

        # Act
        out_wildcard = see.fn_filter(names, pat_wildcard)
        out_single = see.fn_filter(names, pat_single)
        out_partial = see.fn_filter(names, pat_partial)

        # Assert
        self.assertIsInstance(out_wildcard, tuple)
        self.assertIsInstance(out_single, tuple)
        self.assertIsInstance(out_partial, tuple)
        self.assertEqual(out_wildcard, ("george",))
        self.assertEqual(out_single, ("helen",))
        self.assertEqual(out_partial, ())

    def test_see_with_no_args(self):
        # Act
        out = see.see()
        default_arg = see._LOCALS

        # Assert
        self.assertIsInstance(out, see._SeeOutput)
        self.assertEqual(repr(default_arg), 'anything')


if __name__ == '__main__':
    unittest.main()
