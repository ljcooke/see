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
__version__ = '0.3.1'
__copyright__ = 'Copyright (c) 2009 Liam Cooke'
__license__ = 'GNU General Public License v3'

import textwrap

def see(obj):
    """
    Inspect 'obj'. Like dir(obj), but easier on the eyes.

    Some symbols:

        ?       documentation available using help(obj)
        .*      may have dynamic attributes
        []      allows obj[key]
        for     allows iteration
        in      allows membership tests (e.g. x in obj)
        +@      unary positive operator (e.g. +2)
        -@      unary negative operator (e.g. -3)
    """

    # http://docs.python.org/reference/datamodel.html#specialnames
    symbols = (
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
        ('__div__', '/'),
        ('__rdiv__', '/'),
        ('__truediv__', '/'),
        ('__rtruediv__', '/'),
        ('__floordiv__', '/'),
        ('__rfloordiv__', '/'),
        ('__divmod__', '/'),
        ('__rdivmod__', '/'),
        ('__idiv__', '/='),
        ('__itruediv__', '/='),
        ('__ifloordiv__', '/='),
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
        ('__le__', '<='),
        ('__eq__', '=='),
        ('__ne__', '!='),
        ('__gt__', '>'),
        ('__ge__', '>='),

        ('__abs__', 'abs()'),
        ('__nonzero__', 'bool()'),
        ('__complex__', 'complex()'),
        ('__float__', 'float()'),
        ('__hex__', 'hex()'),
        ('__int__', 'int()'),
        ('__len__', 'len()'),
        ('__long__', 'long()'),
        ('__oct__', 'oct()'),
        ('__reversed__', 'reversed()'),
        ('__unicode__', 'unicode()'),
    )
    attrs = dir(obj)
    actions = []
    func = lambda f: hasattr(f, '__call__') and '()' or ''
    name = lambda a,f: '.%s%s' % (a, func(f))

    if obj.__doc__ and obj.__doc__.strip():
        actions.append('?')
    for var, symbol in symbols:
        if var in attrs and symbol not in actions:
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
