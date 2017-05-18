"""
see.tools
Filtering and other tasks

Copyright (c) 2009-2017 Liam Cooke
https://araile.github.io/see/

"""
import fnmatch
import re


def compact(cls, objects):
    """
    Filter out any falsey objects in a sequence.
    """
    return cls(filter(bool, objects or []))


def filter_regex(names, pat):
    """
    Return a tuple of strings that match the regular expression pattern.
    """
    pat = re.compile(pat)

    def match(name, fn=pat.search):
        return fn(name) is not None

    return tuple(filter(match, names))


def filter_wildcard(names, pat):
    """
    Return a tuple of strings that match a shell-style pattern.
    """
    def match(name, fn=fnmatch.fnmatch, pat=pat):
        return fn(name, pat)

    return tuple(filter(match, names))
