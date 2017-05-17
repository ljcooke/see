"""
Unit tests for see.py

"""
try:
    import unittest2 as unittest
except ImportError:
    import unittest

import see
from see import output


class ObjectWithAttributeError(object):

    @property
    def bad_attribute(self):
        raise Exception


class ObjectWithLongAttrName(dict):

    def dajsgkljsdgklajsdgkljdsgkldsjaglkjasdgkldajsgkl(self):
        pass


class TestSee(unittest.TestCase):

    def test_see_with_no_args(self):
        # Act
        out = see.see()
        default_arg = see.inspector.LOCALS

        # Assert
        self.assertIsInstance(out, see.inspector.SeeResult)
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

    def test_see_filter_by_regex(self):
        # Arrange
        obj = []

        # Act
        out = see.see(obj, r='[aeiou]{2}')

        # Assert
        self.assertIn('.count()', out)
        self.assertNotIn('.pop()', out)

    def test_see_filter_by_wildcard(self):
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
        col_width = output.column_width(out)
        padded = [output.justify_token(tok, col_width) for tok in out]
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
