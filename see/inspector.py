"""
Object inspector.

"""
import inspect
import sys

from . import output, tools
from .exceptions import SeeError
from .features import FEATURES, PY3


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
    An object that provides attribute access to its namespace.

    See the SimpleNamespace_ class introduced in Python 3.

    .. _SimpleNamespace:  https://
       docs.python.org/3/library/types.html#types.SimpleNamespace
    """
    def __init__(self, namespace):
        self.__dict__.update(namespace)


# Get all the 'is' functions from the inspect module.
INSPECT_FUNCS = tuple((name, getattr(inspect, name))
                      for name in dir(inspect) if name.startswith('is'))


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

    """
    arg = obj
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
        except (AttributeError, Exception):
            prop = SeeError()
        action = output.display_name(name=attr, obj=prop, local=use_locals)
        tokens.append(action)

    # Backwards compatibility:
    # Filter the output with arguments named pattern and r
    old_args = len(args)
    pattern = args[0] if old_args else kwargs.get('pattern', None)
    regex = args[1] if old_args > 1 else kwargs.get('r', None)
    if pattern is not None:
        tokens = tools.filter_wildcard(tokens, pattern)
        sys.stderr.write(
            'The "pattern" argument is deprecated and will be removed in a '
            'later release. Please use see(%s).match() now.\n' % repr(arg))
    if regex is not None:
        tokens = tools.filter_regex(tokens, regex)
        sys.stderr.write(
            'The "r" argument is deprecated and will be removed in a '
            'later release. Please use see(%s).re() now.\n' % repr(arg))

    return output.SeeResult(tokens)
