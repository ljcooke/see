"""
see.see
Object inspector

Copyright (c) 2009-2017 Liam Cooke
https://araile.github.io/see/

"""
import inspect
import sys
import textwrap

from . import output, term, tools
from .exceptions import SeeError
from .features import FEATURES, PY3


class LocalScope(object):
    """
    Local scope proxy object.
    """
    def __repr__(self):
        return 'anything'

    def _update(self, frame=None):
        """
        Replace this object's namespace with the local namespace of a given
        stack frame.
        """
        self.__dict__ = frame.f_locals

LOCALS = LocalScope()


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
            get_len = output.display_len if PY3 else len
            indent = ' ' * get_len(sys.ps1)
        else:
            indent = '    '

        return textwrap.fill(''.join(padded), term.line_width(),
                             initial_indent=indent,
                             subsequent_indent=indent)


def see(obj=LOCALS, pattern=None, r=None):
    """
    Inspect an object. Like the ``dir()`` builtin, but easier on the eyes.

    Keyword arguments (all optional):

        obj         object to be inspected
        pattern     shell-style search pattern (e.g. '*len*')
        r           regular expression

    If obj is omitted, objects in the current scope are listed instead.

    Some unique symbols are used::

        .*      implements obj.anything
        []      implements obj[key]
        in      implements membership tests (e.g. x in obj)
        +obj    unary positive operator (e.g. +2)
        -obj    unary negative operator (e.g. -2)
        ?       raised an exception

    """
    use_locals = obj is LOCALS
    if use_locals:
        # Get the local scope from the caller's stack frame.
        LOCALS._update(inspect.currentframe().f_back)

    actions = []
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
        actions = tools.filter_wildcard(actions, pattern)

    if r is not None:
        actions = tools.filter_regex(actions, r)

    return SeeResult(actions)
