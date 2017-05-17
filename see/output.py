"""
see.output
Manipulating strings for output

Copyright (c) 2009-2017 Liam Cooke
https://araile.github.io/see/

"""
import math
import unicodedata

from .exceptions import SeeError
from .features import PY3


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


def display_len(text, py2_fallback=len):
    """
    Get the display length of a string. This can differ from the character
    length if the string contains wide characters.
    """
    if PY3 or not py2_fallback:
        text = unicodedata.normalize('NFD', text)
        return sum(char_width(char) for char in text)
    else:
        return py2_fallback(text)


def column_width(tokens):
    """
    Return a suitable column width to display one or more strings.
    """
    lens = sorted(map(display_len, tokens or [])) or [0]
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
    tok_len = display_len(tok)
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
