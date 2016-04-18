#!/usr/bin/env python
# encoding: utf-8
"""
Unit tests for see.py
"""
from __future__ import print_function, unicode_literals
try:
    import unittest2 as unittest
except ImportError:
    import unittest

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))

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
        pat = "or*"

        # Act
        out = see.regex_filter(names, pat)

        # Assert
        self.assertIsInstance(out, tuple)
        self.assertEqual(out, ("george",))

    def test_fn_filter(self):
        # Arrange
        names = ["george", "helen"]
        pat = "*or*"

        # Act
        out = see.fn_filter(names, pat)

        # Assert
        self.assertIsInstance(out, tuple)
        self.assertEqual(out, ("george",))

    def test_see_with_no_args(self):
        # Act
        out = see.see()

        # Assert
        self.assertIsInstance(out, see._SeeOutput)


if __name__ == '__main__':
    unittest.main()

# End of file
