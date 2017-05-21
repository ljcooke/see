"""
Manipulating strings for output.

"""
import math
import sys
import textwrap

from . import term, tools
from .exceptions import SeeError
from .features import PY3


class SeeResult(object):
    """
    The output of the :func:`see` function.

    If there are too many results, you can filter them using the
    :func:`match` and :func:`regex` functions.

    This object acts like a tuple of strings, so you can iterate over the
    results::

        >>> first_result = see()[0]

        >>> for string in see():
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
            indent = ' ' * get_len(ps1)
        else:
            indent = '    '

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

    def match(self, pattern):
        """
        Filter the result using a shell-style wildcard pattern. ::

            >>> see([]).match('*op*')
                .copy()    .pop()

        See fnmatch_ in the Python documentation.

        .. _fnmatch: https://docs.python.org/3/library/fnmatch.html
        """
        return SeeResult(tools.filter_wildcard(self, pattern))

    def regex(self, pattern):
        """
        Filter the result using a regular expression. ::

            >>> see([]).regex('[aeiou]{2}')
                .clear()    .count()

        """
        return SeeResult(tools.filter_regex(self, pattern))


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
