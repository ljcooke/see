#!/usr/bin/env python
"""
Unit tests for the output of see for various types of object.

"""
import itertools

try:
    import unittest2 as unittest
except ImportError:
    import unittest

import see


def union(*sets):
    return set(itertools.chain(*sets))


SIGN_OPS = set(['+obj', '-obj'])

NUMBER_OPS = set('+ - * / // % **'.split())
NUMBER_ASSIGN_OPS = set()

BITWISE_OPS = set('<< >> & ^ | ~'.split())
BITWISE_ASSIGN_OPS = set(op + '=' for op in BITWISE_OPS)

COMPARE_OPS = set('< <= == != > >='.split())

MATRIX_OPS = set(['@'])
MATRIX_ASSIGN_OPS = set(['@='])

ALL_OPS = union(
    SIGN_OPS,
    NUMBER_OPS,
    NUMBER_ASSIGN_OPS,
    BITWISE_OPS,
    BITWISE_ASSIGN_OPS,
    COMPARE_OPS,
    MATRIX_OPS,
    MATRIX_ASSIGN_OPS,
)


class TestSeeOutput(unittest.TestCase):

    def check_ops(self, obj_type, expected_ops, see_output):
        for op in ALL_OPS:
            if op in expected_ops:
                self.assertIn(
                    op, see_output,
                    'expected %s to support %s' % (obj_type, op))
            else:
                self.assertNotIn(
                    op, see_output,
                    'expected %s not to support %s' % (obj_type, op))

    def test_int(self):
        obj = 1
        lit_ops = union(
            SIGN_OPS,
            NUMBER_OPS,
            BITWISE_OPS,
            COMPARE_OPS,
        )
        obj_ops = union(
            lit_ops,
        )

        lit_see = see.see(1)
        obj_see = see.see(obj)

        self.check_ops('int literal', lit_ops, lit_see)
        self.check_ops('int object', obj_ops, obj_see)

    def test_float(self):
        obj = 1.0
        lit_ops = union(
            SIGN_OPS,
            NUMBER_OPS,
            COMPARE_OPS,
        )
        obj_ops = union(
            lit_ops,
        )

        lit_see = see.see(1.0)
        obj_see = see.see(obj)

        self.check_ops('float literal', lit_ops, lit_see)
        self.check_ops('float object', obj_ops, obj_see)


if __name__ == '__main__':
    unittest.main()
