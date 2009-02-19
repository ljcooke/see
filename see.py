"""
see
An alternative to dir(). Easy to type; easy to read. For humans only.

http://github.com/inky/see

    >>> from see import see
    >>> help(see)

Copyright (c) 2009 Liam Cooke

Licensed under the GNU General Public License v3.
See COPYING for the full license text.

"""
__author__ = 'Liam Cooke'
__version__ = '0.4.0'
__copyright__ = 'Copyright (c) 2009 Liam Cooke'
__license__ = 'GNU General Public License v3'

import sys
import textwrap

def see(obj):
    """
    Inspect 'obj'. Like dir(obj), but easier on the eyes.

    Some symbols:

        .*      may have dynamic attributes
        []      allows obj[key]
        for     allows iteration
        in      allows membership tests (e.g. x in obj)
        +@      unary positive operator (e.g. +2)
        -@      unary negative operator (e.g. -3)
    """
    attrs = dir(obj)
    actions = []
    func = lambda f: hasattr(f, '__call__') and '()' or ''
    name = lambda a,f: '.%s%s' % (a, func(f))

    for var, symbol in __see_symbols:
        if var not in attrs or symbol in actions:
            continue
        elif var == '__doc__' and not(obj.__doc__ and obj.__doc__.strip()):
            continue
        actions.append(symbol)
    attrs = filter(lambda a: not a.startswith('_'), attrs)
    for attr in attrs:
        try:
            prop = getattr(obj, attr)
        except AttributeError:
            continue
        actions.append(name(attr, prop))
    print(textwrap.fill('   '.join(actions), 78,
            initial_indent='  ', subsequent_indent='  '))

PY_300 = sys.version_info >= (3, 0)
PY_301 = sys.version_info >= (3, 0, 1)

__see_symbols = tuple(filter(lambda x: x[0], (
    ('__call__', '()'),
    ('__getattr__', '.*'),
    ('__getitem__', '[]'),
    ('__setitem__', '[]'),
    ('__delitem__', '[]'),

    ('__iter__', 'for'),
    ('__enter__', 'with'),
    ('__exit__', 'with'),
    ('__contains__', 'in'),

    ('__add__', '+'),
    ('__radd__', '+'),
    ('__iadd__', '+='),
    ('__sub__', '-'),
    ('__rsub__', '-'),
    ('__isub__', '-='),
    ('__mul__', '*'),
    ('__rmul__', '*'),
    ('__imul__', '*='),
    (not PY_300 and '__div__', '/'),
    (not PY_301 and '__rdiv__', '/'),
    ('__truediv__', '/'),
    ('__rtruediv__', '/'),
    ('__floordiv__', '//'),
    ('__rfloordiv__', '//'),
    (not PY_300 and '__idiv__', '/='),
    ('__itruediv__', '/='),
    ('__ifloordiv__', '//='),
    ('__mod__', '%'),
    ('__rmod__', '%'),
    ('__divmod__', '%'),
    ('__imod__', '%='),
    ('__pow__', '**'),
    ('__rpow__', '**'),
    ('__ipow__', '**='),
    ('__lshift__', '<<'),
    ('__rlshift__', '<<'),
    ('__ilshift__', '<<='),
    ('__rshift__', '>>'),
    ('__rrshift__', '>>'),
    ('__irshift__', '>>='),
    ('__and__', '&'),
    ('__rand__', '&'),
    ('__iand__', '&='),
    ('__xor__', '^'),
    ('__rxor__', '^'),
    ('__ixor__', '^='),
    ('__or__', '|'),
    ('__ror__', '|'),
    ('__ior__', '|='),

    ('__pos__', '+@'),
    ('__neg__', '-@'),
    ('__invert__', '~'),
    ('__lt__', '<'),
    (not PY_301 and '__cmp__', '<'),
    ('__le__', '<='),
    (not PY_301 and '__cmp__', '<='),
    ('__eq__', '=='),
    (not PY_301 and '__cmp__', '=='),
    ('__ne__', '!='),
    (not PY_301 and '__cmp__', '!='),
    ('__gt__', '>'),
    (not PY_301 and '__cmp__', '>'),
    ('__ge__', '>='),
    (not PY_301 and '__cmp__', '>='),

    ('__abs__', 'abs()'),
    (PY_300 and '__bool__' or '__nonzero__', 'bool()'),
    ('__complex__', 'complex()'),
    (PY_300 and '__dir__', 'dir()'),
    ('__divmod__', 'divmod()'),
    ('__rdivmod__', 'divmod()'),
    ('__float__', 'float()'),
    ('__doc__', 'help()'),
    (PY_300 and '__index__' or '__hex__', 'hex()'),
    ('__int__', 'int()'),
    ('__len__', 'len()'),
    (not PY_300 and '__long__', 'long()'),
    (PY_300 and '__index__' or '__oct__', 'oct()'),
    ('__reversed__', 'reversed()'),
    (PY_300 and '__round__', 'round()'),
    (PY_300 and '__unicode__', 'unicode()'),
)))
