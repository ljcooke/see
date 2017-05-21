"""
Python feature definitions.

Reference links:

  * `What's New in Python
    <https://docs.python.org/3/whatsnew/index.html>`__

  * `Data model
    <https://docs.python.org/3/reference/datamodel.html>`__

  * `Standard operators as functions
    <https://docs.python.org/3/library/operator.html>`__

"""
# -----------------------------------------------------------------------------
# Relevant Python changes
#
# 3.5
# - Introduced the @ operator and __matmul__, __imatmul__
# - Introduced __await__, __aiter__, __anext__, __aenter__, __aexit__
#   (see PEP 492)
#
# 3.0-3.3
# - Dropped __cmp__
# - Dropped __div__
# -----------------------------------------------------------------------------

import sys

from .tools import compact


PY_VERSION = sys.version_info

if (PY_VERSION < (2, 6)) or ((3, 0) <= PY_VERSION < (3, 3)):  # pragma: nocover
    sys.stderr.write('Warning: see() is not supported here. '
                     'Please use Python 3.3+ or 2.6+.\n')

PY2 = PY_VERSION < (3, 0)
PY3 = not PY2
PY3_5 = (3, 5) <= PY_VERSION


class Feature(object):
    """
    Definition of a Python feature that an object might support (such as
    performing an arithmetic operation or returning a length), and a symbol
    to indicate this in the output from :func:`see.see`.

    >>> add_feature = Feature(symbol='+', attrs=[
    ...     '__add__',
    ...     '__radd__',
    ... ])

    Support for this feature is detected by checking for one or more special
    attributes on the object.
    """

    def __init__(self, symbol, attrs=None):
        self.symbol = symbol
        self.attrs = set(compact(attrs))

    def match(self, obj, attrs):
        """
        Return whether the feature represented by this symbol is supported by
        a given object and its attributes.
        """
        # pylint: disable=unused-argument
        return not self.attrs.isdisjoint(attrs)


class HelpFeature(Feature):
    """
    Help feature.
    """

    def match(self, obj, attrs):
        """
        Only match if the object contains a non-empty docstring.
        """
        if '__doc__' in attrs:
            lstrip = getattr(obj.__doc__, 'lstrip', False)
            return lstrip and any(lstrip())


FEATURES = compact((

    # -------------------------------------------------------------------------
    # Callable

    Feature(symbol='()', attrs=['__call__']),

    # -------------------------------------------------------------------------
    # Element/attribute access

    Feature(symbol='.*', attrs=['__getattr__']),
    Feature(symbol='[]', attrs=['__getitem__', '__setitem__', '__delitem__']),

    # -------------------------------------------------------------------------
    # Iteration

    Feature(symbol='with', attrs=['__enter__', '__exit__']),
    Feature(symbol='in', attrs=['__contains__']),

    # -------------------------------------------------------------------------
    # Operators

    Feature(symbol='+', attrs=['__add__', '__radd__']),
    Feature(symbol='+=', attrs=['__iadd__']),

    Feature(symbol='-', attrs=['__sub__', '__rsub__']),
    Feature(symbol='-=', attrs=['__isub__']),

    Feature(symbol='*', attrs=['__mul__', '__rmul__']),
    Feature(symbol='*=', attrs=['__imul__']),

    Feature(symbol='@', attrs=['__matmul__', '__rmatmul__']) if PY3_5 else 0,
    Feature(symbol='@=', attrs=['__imatmul__']) if PY3_5 else 0,

    # Python 2.x uses __div__ for a/b, but will look for __truediv__ instead
    # if this is enabled with `from __future__ import division`.
    Feature(symbol='/', attrs=[
        '__truediv__',
        '__rtruediv__',
        PY2 and '__div__',
        PY2 and '__rdiv__',
    ]),
    Feature(symbol='/=', attrs=[
        '__itruediv__',
        PY2 and '__idiv__',
    ]),

    Feature(symbol='//', attrs=['__floordiv__', '__rfloordiv__']),
    Feature(symbol='//=', attrs=['__ifloordiv__']),

    Feature(symbol='%', attrs=['__mod__', '__rmod__', '__divmod__']),
    Feature(symbol='%=', attrs=['__imod__']),

    Feature(symbol='**', attrs=['__pow__', '__rpow__']),
    Feature(symbol='**=', attrs=['__ipow__']),

    Feature(symbol='<<', attrs=['__lshift__', '__rlshift__']),
    Feature(symbol='<<=', attrs=['__ilshift__']),

    Feature(symbol='>>', attrs=['__rshift__', '__rrshift__']),
    Feature(symbol='>>=', attrs=['__irshift__']),

    Feature(symbol='&', attrs=['__and__', '__rand__']),
    Feature(symbol='&=', attrs=['__iand__']),

    Feature(symbol='^', attrs=['__xor__', '__rxor__']),
    Feature(symbol='^=', attrs=['__ixor__']),

    Feature(symbol='|', attrs=['__or__', '__ror__']),
    Feature(symbol='|=', attrs=['__ior__']),

    Feature(symbol='+obj', attrs=['__pos__']),
    Feature(symbol='-obj', attrs=['__neg__']),
    Feature(symbol='~', attrs=['__invert__']),

    Feature(symbol='<', attrs=['__lt__', PY2 and '__cmp__']),
    Feature(symbol='<=', attrs=['__le__', PY2 and '__cmp__']),
    Feature(symbol='==', attrs=['__eq__', PY2 and '__cmp__']),
    Feature(symbol='!=', attrs=['__ne__', PY2 and '__cmp__']),
    Feature(symbol='>', attrs=['__gt__', PY2 and '__cmp__']),
    Feature(symbol='>=', attrs=['__ge__', PY2 and '__cmp__']),

    # -------------------------------------------------------------------------
    # Builtin functions

    Feature(symbol='abs()', attrs=['__abs__']),
    Feature(symbol='bool()', attrs=[
        '__bool__' if PY3 else '__nonzero__'
    ]),
    Feature(symbol='complex()', attrs=['__complex__']),
    Feature(symbol='dir()', attrs=['__dir__']) if PY3 else 0,
    Feature(symbol='divmod()', attrs=['__divmod__', '__rdivmod__']),
    Feature(symbol='float()', attrs=['__float__']),
    Feature(symbol='hash()', attrs=['__hash__']),
    HelpFeature(symbol='help()'),
    Feature(symbol='hex()', attrs=[
        '__index__' if PY3 else '__hex__'
    ]),
    Feature(symbol='int()', attrs=['__int__']),
    Feature(symbol='iter()', attrs=['__iter__']),
    Feature(symbol='len()', attrs=['__len__']),
    Feature(symbol='long()', attrs=['__long__']) if PY2 else 0,
    Feature(symbol='oct()', attrs=[
        '__index__' if PY3 else '__oct__'
    ]),
    Feature(symbol='repr()', attrs=['__repr__']),
    Feature(symbol='reversed()', attrs=['__reversed__']),
    Feature(symbol='round()', attrs=['__round__']) if PY3 else 0,
    Feature(symbol='str()', attrs=['__str__']),
    Feature(symbol='unicode()', attrs=['__unicode__']) if PY3 else 0,

))
