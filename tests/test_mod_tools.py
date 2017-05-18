"""
Unit tests for the see.tools module.

"""
try:
    import unittest2 as unittest
except ImportError:
    import unittest

from see import tools


class TestToolsModule(unittest.TestCase):

    def test_compact_list(self):
        # Arrange
        items = [0, 1, '', 'foo', True, False, [], ['a'], {}, {1: 2}]
        expected = [1, 'foo', True, ['a'], {1: 2}]

        # Act
        compact_list = tools.compact(list, items)
        compact_tuple = tools.compact(tuple, items)

        # Assert
        self.assertEqual(compact_list, list(expected))
        self.assertEqual(compact_tuple, tuple(expected))

    def test_compact_set(self):
        # Arrange
        hashable = [0, 1, '', 'foo', True, False, (), ('a',)]
        unhashable = [0, 1, '', 'foo', True, False, [], ['a']]
        expected = [1, 'foo', True, ('a',)]

        # Act
        compact_set = tools.compact(set, hashable)

        def compact_unhashable():
            return tools.compact(set, unhashable)

        # Assert
        self.assertEqual(compact_set, set(expected))
        self.assertRaises(TypeError, compact_unhashable)

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
