#!/usr/bin/env python
"""
see
dir for humans

    >>> from see import see
    >>> help(see)

Copyright (c) 2009-2016 Liam Cooke
http://araile.github.io/see/

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this
list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice,
this list of conditions and the following disclaimer in the documentation
and/or other materials provided with the distribution.

3. The name of the author may not be used to endorse or promote products
derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY LIAM COOKE "AS IS" AND ANY EXPRESS OR IMPLIED
WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO
EVENT SHALL THE AUTHOR BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT
OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING
IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY
OF SUCH DAMAGE.

"""
import fnmatch
import inspect
import math
import platform
import re
import struct
import sys
import textwrap

try:
    if platform.system() == 'Windows':
        from ctypes import windll, create_string_buffer
        fcntl, termios = None, None
    else:
        import fcntl
        import termios
        windll, create_string_buffer = None, None
except ImportError:
    fcntl, termios = None, None
    windll, create_string_buffer = None, None

__all__ = ['see']

__author__ = 'Liam Cooke'
__contributors__ = 'See AUTHORS.rst'
__version__ = '1.3.1'
__copyright__ = 'Copyright (c) 2009-2016 Liam Cooke'
__license__ = 'BSD License'


DEFAULT_LINE_WIDTH = 78
MAX_LINE_WIDTH = 120


def term_width():
    """
    Return the column width of the terminal, or None if it can't be determined.

    """
    if fcntl and termios:
        try:
            winsize = fcntl.ioctl(0, termios.TIOCGWINSZ, '    ')
            _, width = struct.unpack('hh', winsize)
            return width
        except IOError:
            pass
    elif windll and create_string_buffer:
        stderr_handle, struct_size = -12, 22
        handle = windll.kernel32.GetStdHandle(stderr_handle)
        csbi = create_string_buffer(struct_size)
        res = windll.kernel32.GetConsoleScreenBufferInfo(handle, csbi)
        if res:
            (_, _, _, _, _, left, _, right, _,
             _, _) = struct.unpack('hhhhHhhhhhh', csbi.raw)
            return right - left + 1


def line_width(default_width=DEFAULT_LINE_WIDTH, max_width=MAX_LINE_WIDTH):
    """
    Return the ideal column width for see() output, taking the terminal width
    into account to avoid wrapping.

    """
    width = term_width()
    if width:
        return min(width, max_width)
    else:
        return default_width


def regex_filter(names, pat):
    """
    Return a tuple of strings that match the regular expression pattern.

    """
    pat = re.compile(pat)

    def match(name, fn=pat.search):
        return fn(name) is not None

    return tuple(filter(match, names))


def fn_filter(names, pat):
    """
    Return a tuple of strings that match a shell-style pattern.

    """
    def match(name, fn=fnmatch.fnmatch, pat=pat):
        return fn(name, pat)

    return tuple(filter(match, names))


class SeeError(Exception):
    pass


def column_width(tokens):
    """
    Return a suitable column width to display one or more strings.

    """
    lens = sorted(map(len, tokens or [])) or [0]
    width = lens[-1]

    # adjust for disproportionately long strings
    if width >= 18:
        most = lens[int(len(lens) * 0.9)]
        if most < width + 6:
            return most

    return width


def justify_token(tok, col_width):
    """
    Justify a string to fill one or more columns.

    """
    tok_len = len(tok)
    cols = (int(math.ceil(float(tok_len) / col_width))
            if col_width < tok_len + 4 else 1)

    if cols > 1:
        return tok.ljust((col_width * cols) + (4 * cols))
    else:
        return tok.ljust(col_width + 4)


class _SeeOutput(tuple):
    """
    Tuple-like object with a pretty string representation.

    """
    def __new__(self, actions=None):
        return tuple.__new__(self, actions or [])

    def __repr__(self):
        col_width = column_width(self)

        padded = [justify_token(tok, col_width) for tok in self]
        if hasattr(sys, 'ps1'):
            indent = ' ' * len(sys.ps1)
        else:
            indent = '    '

        return textwrap.fill(''.join(padded), line_width(),
                             initial_indent=indent,
                             subsequent_indent=indent)


class _SeeDefault(object):

    def __repr__(self):
        return 'anything'

_LOCALS = _SeeDefault()


def see(obj=_LOCALS, pattern=None, r=None):
    """
    Inspect an object. Like the dir() builtin, but easier on the eyes.

    Keyword arguments (all optional):
    obj -- object to be inspected
    pattern -- shell-style search pattern (e.g. '*len*')
    r -- regular expression

    If obj is omitted, objects in the current scope are listed instead.

    Some unique symbols are used:

        .*      implements obj.anything
        []      implements obj[key]
        in      implements membership tests (e.g. x in obj)
        +obj    unary positive operator (e.g. +2)
        -obj    unary negative operator (e.g. -2)
        ?       raised an exception

    """
    use_locals = obj is _LOCALS
    actions = []
    dot = not use_locals and '.' or ''
    name = lambda a, f: ''.join((dot, a, suffix(f)))

    def suffix(f):
        if isinstance(f, SeeError):
            return '?'
        elif hasattr(f, '__call__'):
            return '()'
        else:
            return ''

    if use_locals:
        obj.__dict__ = inspect.currentframe().f_back.f_locals
    attrs = dir(obj)
    if not use_locals:
        for var, symbol in SYMBOLS:
            if var not in attrs or symbol in actions:
                continue
            elif var == '__doc__':
                if not obj.__doc__ or not obj.__doc__.strip():
                    continue
            actions.append(symbol)

    for attr in filter(lambda a: not a.startswith('_'), attrs):
        try:
            prop = getattr(obj, attr)
        except (AttributeError, Exception):
            prop = SeeError()
        actions.append(name(attr, prop))

    if pattern is not None:
        actions = fn_filter(actions, pattern)
    if r is not None:
        actions = regex_filter(actions, r)

    return _SeeOutput(actions)


PY_300 = sys.version_info >= (3, 0)
PY_301 = sys.version_info >= (3, 0, 1)
PY_350 = sys.version_info >= (3, 5, 0)


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
    (PY_350 and '__matmul__', '@'),
    (PY_350 and '__rmatmul__', '@'),
    (PY_350 and '__imatmul__', '@='),
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
    ('__pos__', '+obj'),
    ('__neg__', '-obj'),
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


if __name__ == '__main__':
    help(see)
