"""
Manipulating strings for output.

"""
import math
import re
import sys
import textwrap

from . import term, tools
from .exceptions import SeeError
from .features import PY3


REGEX_TYPE = type(re.compile('.'))

MAX_INDENT = 4


class SeeResult(object):
    """
    The output of the :func:`see` function.

    Acts like a tuple of strings, so you can iterate over the output::

        >>> first = see()[0]

        >>> for string in see([]):
        ...     print(string)

    """
    def __init__(self, tokens):
        self._tokens = tuple(tokens)

    def __repr__(self):
        col_width = column_width(self)
        padded = [justify_token(tok, col_width) for tok in self]

        ps1 = getattr(sys, 'ps1', None)
        if ps1:
            get_len = tools.display_len if PY3 else len
            indent = ' ' * min(get_len(ps1), MAX_INDENT)
        else:
            indent = ' ' * MAX_INDENT

        return textwrap.fill(''.join(padded), term.line_width(),
                             initial_indent=indent,
                             subsequent_indent=indent)

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __iter__(self):
        return iter(self._tokens)

    def __len__(self):
        return len(self._tokens)

    def __getitem__(self, index):
        return self._tokens[index]

    def filter(self, pattern):
        """
        Filter the results using a pattern.

        This accepts a shell-style wildcard pattern (as used by the fnmatch_
        module)::

            >>> see([]).filter('*op*')
                .copy()    .pop()

        It also accepts a regular expression. This may be a compiled regular
        expression (from the re_ module) or a string that starts with a ``/``
        (forward slash) character::

            >>> see([]).filter('/[aeiou]{2}/')
                .clear()    .count()

        .. _fnmatch: https://docs.python.org/3/library/fnmatch.html
        .. _re: https://docs.python.org/3/library/re.html
        """
        if isinstance(pattern, REGEX_TYPE):
            func = tools.filter_regex
        elif pattern.startswith('/'):
            pattern = re.compile(pattern.strip('/'))
            func = tools.filter_regex
        else:
            func = tools.filter_wildcard

        return SeeResult(func(self, pattern))


def column_width(tokens):
    """
    Return a suitable column width to display one or more strings.
    """
    get_len = tools.display_len if PY3 else len
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
    get_len = tools.display_len if PY3 else len
    tok_len = get_len(tok)
    diff_len = tok_len - len(tok) if PY3 else 0

    cols = (int(math.ceil(float(tok_len) / col_width))
            if col_width < tok_len + 4 else 1)

    if cols > 1:
        return tok.ljust((col_width * cols) + (4 * cols) - diff_len)
    else:
        return tok.ljust(col_width + 4 - diff_len)


def display_name(name, obj, local):
    """
    Get the display name of an object.

    Keyword arguments (all required):

    * ``name`` -- the name of the object as a string.
    * ``obj`` -- the object itself.
    * ``local`` -- a boolean value indicating whether the object is in local
      scope or owned by an object.

    """
    prefix = '' if local else '.'

    if isinstance(obj, SeeError):
        suffix = '?'
    elif hasattr(obj, '__call__'):
        suffix = '()'
    else:
        suffix = ''

    return ''.join((prefix, name, suffix))
