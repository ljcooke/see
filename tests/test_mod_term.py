"""
Unit tests for the see.term module.

"""
try:
    import unittest2 as unittest
except ImportError:
    import unittest

from see import term


class TestTermModule(unittest.TestCase):

    def test_line_width(self):
        # Arrange
        default_width = 1
        max_width = 1

        # Act
        width = term.line_width(default_width, max_width)
        width_no_args = term.line_width()

        # Assert
        self.assertIsInstance(width, int)
        self.assertEqual(width, 1)
        self.assertLessEqual(width_no_args, term.MAX_LINE_WIDTH)
