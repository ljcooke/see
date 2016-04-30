#!/usr/bin/env python
# coding: utf-8
from __future__ import unicode_literals
"""
Unit tests that require Unicode string literals in Python 2.

"""
try:
    import unittest2 as unittest
except ImportError:
    import unittest

import see


class TestSeeUnicode(unittest.TestCase):

    def test_char_width(self):
        # Arrange
        char_ascii = 'a'   # narrow char
        char_accent = 'á'  # narrow char
        char_combo = 'q̇'   # narrow char + zero-width combining char
        char_cjk = '猫'    # wide character

        # Act
        len_ascii = len(char_ascii)
        len_accent = len(char_accent)
        len_combo = len(char_combo)
        len_cjk = len(char_cjk)
        width_ascii = see.display_len(char_ascii)
        width_accent = see.display_len(char_accent)
        width_combo = see.display_len(char_combo)
        width_cjk = see.display_len(char_cjk)

        # Assert
        self.assertEqual(len_ascii, 1)
        self.assertEqual(len_accent, 1)
        self.assertEqual(len_combo, 2)
        self.assertEqual(len_cjk, 1)
        self.assertEqual(width_ascii, 1)
        self.assertEqual(width_accent, 1)
        self.assertEqual(width_combo, 1)
        self.assertEqual(width_cjk, 2)

    def test_display_len(self):
        # Arrange
        attr_ascii = '.hello_world()'
        attr_cyrillic = '.hello_мир()'
        attr_cjk = '.hello_世界()'
        attr_combo = '.hello_q̇()'
        diff_cjk = 2 if see.PY_300 else 0
        diff_combo = -1 if see.PY_300 else 0

        # Act
        width_ascii = see.display_len(attr_ascii)
        width_cyrillic = see.display_len(attr_cyrillic)
        width_cjk = see.display_len(attr_cjk)
        width_combo = see.display_len(attr_combo)
        justify_ascii = len(see.justify_token(attr_ascii, 20))
        justify_cyrillic = len(see.justify_token(attr_cyrillic, 20))
        justify_cjk = len(see.justify_token(attr_cjk, 20))
        justify_combo = len(see.justify_token(attr_combo, 20))

        # Assert
        self.assertEqual(width_ascii, 14)
        self.assertEqual(width_cyrillic, 12)
        self.assertEqual(width_cjk, 13)
        self.assertEqual(width_combo, 10)
        self.assertEqual(justify_cyrillic, justify_ascii)
        self.assertEqual(justify_cjk, justify_ascii - diff_cjk)
        self.assertEqual(justify_combo, justify_ascii - diff_combo)


if __name__ == '__main__':
    unittest.main()
