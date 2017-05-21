"""
Exception classes.

"""


class SeeError(Exception):
    """
    This is used internally by :func:`see.see` to indicate an invalid
    attribute, such as one that raises an exception when it is accessed.
    """
    pass
