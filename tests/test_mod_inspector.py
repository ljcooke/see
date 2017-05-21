"""
Unit tests for the see.inspector module.

"""
try:
    import unittest2 as unittest
except ImportError:
    import unittest

from see import inspector, output, see


class ObjectWithAttributeError(object):

    @property
    def bad_attribute(self):
        raise Exception


class ObjectWithDocstring(object):
    """
    Hello, world
    """
    pass


class ObjectWithEmptyDocstring(object):
    """
    """
    pass


class TestDefaultArgClass(unittest.TestCase):

    def test_global_instance(self):
        self.assertIsInstance(inspector.DEFAULT_ARG, inspector.DefaultArg)

    def test_repr(self):
        arg = inspector.DefaultArg()

        self.assertEqual(repr(arg), 'anything')


class TestNamespaceClass(unittest.TestCase):

    def test_namespace(self):
        attributes = {
            'hello': 'hello world',
        }

        namespace = inspector.Namespace(attributes)

        self.assertEqual(namespace.hello, 'hello world')
        self.assertIn('hello', dir(namespace))
        self.assertIn('.hello', see(namespace))


class TestSeeFunction(unittest.TestCase):

    def test_see_with_args(self):
        result = see([])

        self.assertTrue(any(result))

    def test_see_without_args(self):
        result = see()

        self.assertTrue(any(result))

    def test_see_with_new_default_arg_instance(self):
        result_with_obj = see(inspector.DefaultArg())
        result_without_args = see()

        self.assertNotEqual(result_with_obj, result_without_args)

    def test_see_accessor_raises_exception(self):
        normal_obj = 1
        err_obj = ObjectWithAttributeError()

        normal_result = see(normal_obj)
        err_result = see(err_obj)

        self.assertTrue(not any(attr.endswith('?')
                                for attr in normal_result))
        self.assertTrue(any(attr.endswith('?')
                            for attr in err_result))
        self.assertIn('.bad_attribute?', err_result)

    def test_see_object_has_help(self):
        obj_help = ObjectWithDocstring()
        obj_nohelp = ObjectWithEmptyDocstring()

        out_help = see(obj_help)
        out_nohelp = see(obj_nohelp)

        self.assertTrue('help()' in out_help)
        self.assertFalse('help()' in out_nohelp)

    # Deprecated filtering API -- see test_mod_output

    def test_see_deprecated_r_arg(self):
        obj = []
        pattern = '[aeiou]{2}'

        filtered_result = see(obj, r=pattern)
        filtered_result_pos_arg = see(obj, '*', pattern)

        # Assert
        self.assertIn('.count()', filtered_result)
        self.assertNotIn('.pop()', filtered_result)

    def test_see_deprecated_pattern_arg(self):
        obj = []
        pattern = '*()'

        filtered_result = see(obj, pattern=pattern)
        filtered_result_pos_arg = see(obj, pattern)

        # Assert
        self.assertEqual(filtered_result, filtered_result_pos_arg)
        self.assertIn('.count()', filtered_result)
        self.assertNotIn('+=', filtered_result)
