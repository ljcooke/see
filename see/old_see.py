"""
see.old_see

Copyright (c) 2009-2017 Liam Cooke
https://araile.github.io/see/

"""
import fnmatch
import inspect
import re
import sys
import textwrap

from . import output, term
from .exceptions import SeeError
from .features import FEATURES


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


class _SeeDefault(object):

    def __repr__(self):
        return 'anything'

_LOCALS = _SeeDefault()


class SeeResult(tuple):
    """
    Tuple-like output with a pretty string representation.
    """

    def __new__(self, actions=None):
        return tuple.__new__(self, actions or [])

    def __repr__(self):
        col_width = output.column_width(self)
        padded = [output.justify_token(tok, col_width) for tok in self]

        if hasattr(sys, 'ps1'):
            indent = ' ' * output.display_len(sys.ps1)
        else:
            indent = '    '

        return textwrap.fill(''.join(padded), term.line_width(),
                             initial_indent=indent,
                             subsequent_indent=indent)


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
        action = output.display_name(name=attr, obj=prop, local=use_locals)
        actions.append(action)

    if pattern is not None:
        actions = fn_filter(actions, pattern)
    if r is not None:
        actions = regex_filter(actions, r)

    return SeeResult(actions)
