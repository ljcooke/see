#!/usr/bin/env python
"""
see.old_see

Copyright (c) 2009-2017 Liam Cooke
https://araile.github.io/see/

"""
import fnmatch
import inspect
import math
import re
import sys
import textwrap
import unicodedata

from .features import FEATURES, PY3
from .term import term_width


DEFAULT_LINE_WIDTH = 78
MAX_LINE_WIDTH = 120


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


def char_width(char):
    """
    Get the display length of a unicode character.

    """
    if ord(char) < 128:
        return 1
    elif unicodedata.east_asian_width(char) in ('F', 'W'):
        return 2
    elif unicodedata.category(char) in ('Mn',):
        return 0
    else:
        return 1


def display_len(text):
    """
    Get the display length of a string. This can differ from the character
    length if the string contains wide characters.

    """
    text = unicodedata.normalize('NFD', text)
    return sum(char_width(char) for char in text)


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
    get_len = display_len if PY3 else len
    lens = sorted(map(get_len, tokens or [])) or [0]
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
    tok_len = display_len(tok) if PY3 else len(tok)
    diff_len = tok_len - len(tok) if PY3 else 0

    cols = (int(math.ceil(float(tok_len) / col_width))
            if col_width < tok_len + 4 else 1)

    if cols > 1:
        return tok.ljust((col_width * cols) + (4 * cols) - diff_len)
    else:
        return tok.ljust(col_width + 4 - diff_len)


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
            get_len = display_len if PY3 else len
            indent = ' ' * get_len(sys.ps1)
        else:
            indent = '    '

        return textwrap.fill(''.join(padded), line_width(),
                             initial_indent=indent,
                             subsequent_indent=indent)


class _SeeDefault(object):

    def __repr__(self):
        return 'anything'

_LOCALS = _SeeDefault()


def display_name(name, obj, local):
    """
    Get the display name of an object.

    Keyword arguments:
    name -- the name of the object as a string
    obj -- the object itself
    local -- whether the object is in local scope or owned by an object

    """
    prefix = '' if local else '.'

    if isinstance(obj, SeeError):
        suffix = '?'
    elif hasattr(obj, '__call__'):
        suffix = '()'
    else:
        suffix = ''

    return ''.join((prefix, name, suffix))


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

    if use_locals:
        obj.__dict__ = inspect.currentframe().f_back.f_locals
    attrs = dir(obj)

    if not use_locals:
        for feature in FEATURES:
            if feature.match(obj, attrs):
                actions.append(feature.symbol)

    for attr in filter(lambda a: not a.startswith('_'), attrs):
        try:
            prop = getattr(obj, attr)
        except (AttributeError, Exception):
            prop = SeeError()
        actions.append(display_name(name=attr, obj=prop, local=use_locals))

    if pattern is not None:
        actions = fn_filter(actions, pattern)
    if r is not None:
        actions = regex_filter(actions, r)

    return _SeeOutput(actions)


if __name__ == '__main__':
    help(see)
