"""
Filtering and other tasks.

"""
import fnmatch
import re


def compact(objects):
    """
    Filter out any falsey objects in a sequence.
    """
    return tuple(filter(bool, objects or []))


def filter_regex(names, pattern):
    """
    Return a tuple of strings that match the regular expression pattern.
    """
    pattern = re.compile(pattern)

    def match(name, fn=pattern.search):
        return fn(name) is not None

    return tuple(filter(match, names))


def filter_wildcard(names, pattern):
    """
    Return a tuple of strings that match a shell-style pattern.
    """
    def match(name, fn=fnmatch.fnmatch, pattern=pattern):
        return fn(name, pattern)

    return tuple(filter(match, names))
