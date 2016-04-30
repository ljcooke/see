#!/usr/bin/env python
# coding: utf-8
"""
Unit tests for see.py

"""
try:
    import unittest2 as unittest
except ImportError:
    import unittest

import see


class ObjectWithAttributeError(object):

    @property
    def bad_attribute(self):
        raise Exception


class ObjectWithLongAttrName(dict):

    def dajsgkljsdgklajsdgkljdsgkldsjaglkjasdgkldajsgkl(self):
        pass


class TestSee(unittest.TestCase):

    def test_line_width(self):
        # Arrange
        default_width = 1
        max_width = 1

        # Act
        width = see.line_width(default_width, max_width)
        width_no_args = see.line_width()

        # Assert
        self.assertIsInstance(width, int)
        self.assertEqual(width, 1)
        self.assertLessEqual(width_no_args, see.MAX_LINE_WIDTH)

    def test_char_width(self):
        # Arrange
        char_ascii = u'a'   # narrow char
        char_accent = u'á'  # narrow char
        char_combo = u'q̇'   # narrow char + zero-width combining char
        char_cjk = u'猫'    # wide character

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
        attr_ascii = u'.hello_world()'
        attr_cyrillic = u'.hello_мир()'
        attr_cjk = u'.hello_世界()'
        attr_combo = u'.hello_q̇()'
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

    def test_see_accessor_raises_exception(self):
        # Arrange
        normal_obj = 1
        err_obj = ObjectWithAttributeError()

        # Act
        normal_see = see.see(normal_obj)
        err_see = see.see(err_obj)

        # Assert
        self.assertTrue(not any(attr.endswith('?')
                                for attr in normal_see))
        self.assertTrue(any(attr.endswith('?')
                            for attr in err_see))
        self.assertIn('.bad_attribute?', err_see)

    def test_see_regex_filter(self):
        # Arrange
        obj = []

        # Act
        out = see.see(obj, r='[aeiou]{2}')

        # Assert
        self.assertIn('.count()', out)
        self.assertNotIn('.pop()', out)

    def test_see_pattern_filter(self):
        # Arrange
        obj = []

        # Act
        out = see.see(obj, '*()')

        # Assert
        self.assertIn('.count()', out)
        self.assertNotIn('+=', out)

    def test_see_repr(self):
        # Act
        out = see.see()

        # Assert
        self.assertEqual(str(out), out.__repr__())

    def test_see_justify_attributes(self):
        # Arrange
        obj = ObjectWithLongAttrName()

        # Act
        out = see.see(obj)
        col_width = see.column_width(out)
        padded = [see.justify_token(tok, col_width) for tok in out]
        lens = sorted(map(len, padded))
        factors = tuple(float(num) / lens[0] for num in lens[1:])

        # Assert
        self.assertNotEqual(lens[0], lens[-1],
                            'Expected differing column widths')
        self.assertTrue(any(factors))
        self.assertTrue(all(int(factor) == factor for factor in factors),
                        'Irregular column widths')


if __name__ == '__main__':
    unittest.main()
