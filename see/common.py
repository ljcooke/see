"""
see
Common code

Copyright (c) 2009-2017 Liam Cooke
https://araile.github.io/see/

"""


def compact(cls, objects):
    """
    Filter out any falsey objects in a sequence.

    """
    return cls(filter(bool, objects or []))
