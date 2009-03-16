#!/usr/bin/env python

"""
see
An alternative to dir(). Easy to type; easy to read. For humans only.

    >>> from see import see
    >>> help(see)

Copyright (c) 2009 Liam Cooke
http://github.com/inky/see

Licensed under the GNU General Public License v3.
See COPYING for the full license text.

"""

__author__ = 'Liam Cooke'
__version__ = '0.5.2'
__copyright__ = 'Copyright (c) 2009 Liam Cooke'
__license__ = 'GNU General Public License v3'


import fnmatch
import inspect
import re
import sys
import textwrap


def regex_filter(names, pat):
    pat = re.compile(pat)

    def match(name, fn=pat.search):
        return fn(name) is not None
    return tuple(filter(match, names))


def fn_filter(names, pat):

    def match(name, fn=fnmatch.fnmatch, pat=pat):
        return fn(name, pat)
    return tuple(filter(match, names))


class SeeOutput(list):
    """
    List-like class with a pretty __repr__ and __str__ output to retain
    iterability of the return from see() while also permitting convenient use
    of e.g. "print see(obj)" or just "see(obj)" in the interactive interpreter.
    """

    def __init__(self, actions=None):
        if actions is None:
            actions = []
        self.actions = actions
        super(SeeOutput, self).__init__(actions)

    def __str__(self):
        return textwrap.fill('   '.join(self.actions), 78,
            initial_indent='  ', subsequent_indent='  ')

    def __repr__(self):
        return textwrap.fill('   '.join(self.actions), 78,
            initial_indent='  ', subsequent_indent='  ')


class _LocalsProxy(object):
    pass

_NO_OBJ = _LocalsProxy()


def see(obj=_NO_OBJ, pattern=None, r=None):
    """
    Inspect 'obj'. Like dir(obj), but easier on the eyes.

    Some symbols:

        .*      may have dynamic attributes
        []      allows obj[key]
        in      allows membership tests (e.g. x in obj)
        +@      unary positive operator (e.g. +2)
        -@      unary negative operator (e.g. -3)
    """
    locals = obj is _NO_OBJ
    if locals:
        obj.__dict__ = inspect.currentframe().f_back.f_locals
    attrs = dir(obj)
    actions = []

    dot = not locals and '.' or ''
    func = lambda f: hasattr(f, '__call__') and '()' or ''
    name = lambda a, f: ''.join((dot, a, func(f)))

    if not locals:
        for var, symbol in SYMBOLS:
            if var not in attrs or symbol in actions:
                continue
            elif var == '__doc__':
                try:
                    obj.__doc__.strip()[0]
                except (AttributeError, IndexError):
                    continue
            actions.append(symbol)

    for attr in filter(lambda a: not a.startswith('_'), attrs):
        try:
            prop = getattr(obj, attr)
        except AttributeError:
            continue
        actions.append(name(attr, prop))

    if pattern is not None:
        actions = fn_filter(actions, pattern)
    if r is not None:
        actions = regex_filter(actions, r)

    return SeeOutput(actions=actions)


PY_300 = sys.version_info >= (3, 0)
PY_301 = sys.version_info >= (3, 0, 1)

SYMBOLS = tuple(filter(lambda x: x[0], (
    # callable
    ('__call__', '()'),

    # element/attribute access
    ('__getattr__', '.*'),
    ('__getitem__', '[]'),
    ('__setitem__', '[]'),
    ('__delitem__', '[]'),

    # iteration
    ('__enter__', 'with'),
    ('__exit__', 'with'),
    ('__contains__', 'in'),

    # operators
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

    # built-in functions
    ('__abs__', 'abs()'),
    (PY_300 and '__bool__' or '__nonzero__', 'bool()'),
    ('__complex__', 'complex()'),
    (PY_300 and '__dir__', 'dir()'),
    ('__divmod__', 'divmod()'),
    ('__rdivmod__', 'divmod()'),
    ('__float__', 'float()'),
    ('__hash__', 'hash()'),
    ('__doc__', 'help()'),
    (PY_300 and '__index__' or '__hex__', 'hex()'),
    ('__int__', 'int()'),
    ('__iter__', 'iter()'),
    ('__len__', 'len()'),
    (not PY_300 and '__long__', 'long()'),
    (PY_300 and '__index__' or '__oct__', 'oct()'),
    ('__repr__', 'repr()'),
    ('__reversed__', 'reversed()'),
    (PY_300 and '__round__', 'round()'),
    ('__str__', 'str()'),
    (PY_300 and '__unicode__', 'unicode()'),
)))
