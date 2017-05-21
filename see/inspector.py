"""
Object inspector.

"""
import inspect
import re
import sys

from . import output, tools
from .exceptions import SeeError
from .features import FEATURES


class DefaultArg(object):
    """
    A global instance of this class is used as the default argument to
    :func:`see.see`. This allows for a distinction between calling ``see()``
    without arguments and calling it with a falsey argument like ``see(None)``.
    """
    def __repr__(self):
        return 'anything'


DEFAULT_ARG = DefaultArg()


class Namespace(object):
    """
    An object whose attributes are initialised with a dictionary.
    Similar to the SimpleNamespace_ class introduced in Python 3.

    .. _SimpleNamespace:  https://
       docs.python.org/3/library/types.html#types.SimpleNamespace
    """
    def __init__(self, attrs):
        self.__dict__.update(attrs)


# Get all the 'is' functions from the inspect module.
INSPECT_FUNCS = tuple((name, getattr(inspect, name))
                      for name in dir(inspect) if name.startswith('is'))


def handle_deprecated_args(tokens, args, kwargs):
    """
    Backwards compatibility with deprecated arguments ``pattern`` and ``r``.
    """
    num_args = len(args)
    pattern = args[0] if num_args else kwargs.get('pattern', None)
    regex = args[1] if num_args > 1 else kwargs.get('r', None)

    if pattern is not None:
        tokens = tools.filter_wildcard(tokens, pattern)
        sys.stderr.write(
            'Please use see().match() now. The "pattern" argument is '
            'deprecated and will be removed in a later release. \n')

    if regex is not None:
        tokens = tools.filter_regex(tokens, re.compile(regex))
        sys.stderr.write(
            'Please use see().match() now. The "r" argument is '
            'deprecated and will be removed in a later release. \n')

    return tokens


def see(obj=DEFAULT_ARG, *args, **kwargs):
    """
    see(obj=anything)

    Show the features and attributes of an object.

    This function takes a single argument, ``obj``, which can be of any type.
    A summary of the object is printed immediately in the Python interpreter.
    For example::

        >>> see([])
            []            in            +             +=            *
            *=            <             <=            ==            !=
            >             >=            dir()         hash()
            help()        iter()        len()         repr()
            reversed()    str()         .append()     .clear()
            .copy()       .count()      .extend()     .index()
            .insert()     .pop()        .remove()     .reverse()
            .sort()

    If this function is run without arguments, it will instead list the objects
    that are available in the current scope. ::

        >>> see()
            os        random    see()     sys

    The return value is an instance of :class:`SeeResult`.
    """
    use_locals = obj is DEFAULT_ARG

    if use_locals:
        # Get the local scope from the caller's stack frame.
        # Typically this is the scope of an interactive Python session.
        obj = Namespace(inspect.currentframe().f_back.f_locals)

    tokens = []
    attrs = dir(obj)

    if not use_locals:

        for name, func in INSPECT_FUNCS:
            if func(obj):
                tokens.append(name)

        for feature in FEATURES:
            if feature.match(obj, attrs):
                tokens.append(feature.symbol)

    for attr in filter(lambda a: not a.startswith('_'), attrs):
        try:
            prop = getattr(obj, attr)
        except (AttributeError, Exception):  # pylint: disable=broad-except
            prop = SeeError()
        action = output.display_name(name=attr, obj=prop, local=use_locals)
        tokens.append(action)

    if args or kwargs:
        tokens = handle_deprecated_args(tokens, args, kwargs)

    return output.SeeResult(tokens)
