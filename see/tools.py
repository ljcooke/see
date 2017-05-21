"""
Filtering and other tasks.

"""
import fnmatch
import unicodedata


def compact(objects):
    """
    Filter out any falsey objects in a sequence.
    """
    return tuple(filter(bool, objects or []))


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


def filter_regex(names, regex):
    """
    Return a tuple of strings that match the regular expression pattern.
    """
    return tuple(name for name in names
                 if regex.search(name) is not None)


def filter_wildcard(names, pattern):
    """
    Return a tuple of strings that match a shell-style wildcard pattern.
    """
    return tuple(name for name in names
                 if fnmatch.fnmatch(name, pattern))
