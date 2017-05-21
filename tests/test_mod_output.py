"""
Unit tests for the see.output module.

"""
import re

try:
    import unittest2 as unittest
except ImportError:
    import unittest

from see import output, see
from see.features import PY3


class ObjectWithLongAttrName(dict):

    def lorem_ipsum_dolor_sit_amet_consectetur_adipiscing_elit(self):
        pass


class TestSeeResultClass(unittest.TestCase):

    def test_see_returns_result_instance(self):
        result_for_obj = see([])
        result_for_locals = see()

        isinstance(result_for_obj, output.SeeResult)
        isinstance(result_for_locals, output.SeeResult)

    def test_repr(self):
        result = see()

        self.assertEqual(str(result), result.__repr__())

    def test_acts_like_tuple(self):
        result = see([])

        self.assertIsNotNone(tuple(result))
        self.assertIsNotNone(result[0])
        self.assertIsNotNone(result[-1])
        self.assertTrue(any(result))
        self.assertTrue(len(result) > 0)

    def test_justify_attributes(self):
        obj = ObjectWithLongAttrName()

        result = see(obj)
        col_width = output.column_width(result)
        padded = [output.justify_token(tok, col_width) for tok in result]
        lens = sorted(map(len, padded))
        factors = tuple(float(num) / lens[0] for num in lens[1:])

        # Assert
        self.assertNotEqual(lens[0], lens[-1],
                            'Expected differing column widths')
        self.assertTrue(any(factors))
        self.assertTrue(all(int(factor) == factor for factor in factors),
                        'Irregular column widths')

    def test_filter_with_wildcard(self):
        obj = []
        pattern = '*op*'
        expected = ('.copy()', '.pop()') if PY3 else ('.pop()',)

        filtered_result = see(obj).filter(pattern)

        self.assertIsInstance(filtered_result, output.SeeResult)
        self.assertEqual(expected, filtered_result)

    def test_filter_with_regex_string(self):
        obj = []
        pattern = '/[aeiou]{2}/'
        expected = ('.clear()', '.count()') if PY3 else ('.count()',)

        filtered_result = see(obj).filter(pattern)

        self.assertIsInstance(filtered_result, output.SeeResult)
        self.assertEqual(expected, filtered_result)

    def test_filter_with_regex_object(self):
        obj = []
        pattern = re.compile('[aeiou]{2}')
        expected = ('.clear()', '.count()') if PY3 else ('.count()',)

        filtered_result = see(obj).filter(pattern)

        self.assertIsInstance(filtered_result, output.SeeResult)
        self.assertEqual(expected, filtered_result)
