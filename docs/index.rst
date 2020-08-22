.. see documentation master file.
   This should contain the root `toctree` directive.

.. For Python examples, use the following:
   * 64-column terminal
   * sys.ps1 = '>>> '
   * sys.ps2 = '... '


see: dir for humans
===================

.. module:: see

Release v\ |release|.

**see** is an alternative to ``dir()``, for Python 2.7 and 3.4+.

It neatly summarises what you can do with an object.
Use it to inspect your code or learn new APIs.

To get started, see the :doc:`install` and :doc:`usage` pages.


Example
-------

Say you have an object which you'd like to know more about::

    >>> from datetime import timedelta

Try inspecting the object with ``see``::

    >>> see(timedelta)
        isclass             +                   -
        *                   /                   //
        %                   +obj                -obj
        <                   <=                  ==
        !=                  >                   >=
        abs()               bool()              dir()
        divmod()            hash()              help()
        repr()              str()               .days
        .max                .microseconds       .min
        .resolution         .seconds            .total_seconds()

Here we can discover some things about it, such as:

* The object is a class.
* You can add something to it with the ``+`` operator.
* It has a ``seconds`` attribute.
* It has a ``total_seconds`` attribute which is a function.

Compare with the output of ``dir``::

    >>> dir(timedelta)
    ['__abs__', '__add__', '__bool__', '__class__', '__delattr__', '
    __dir__', '__divmod__', '__doc__', '__eq__', '__floordiv__', '__
    format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '
    __init__', '__init_subclass__', '__le__', '__lt__', '__mod__', '
    __mul__', '__ne__', '__neg__', '__new__', '__pos__', '__radd__',
     '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rf
    loordiv__', '__rmod__', '__rmul__', '__rsub__', '__rtruediv__',
    '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclassho
    ok__', '__truediv__', 'days', 'max', 'microseconds', 'min', 'res
    olution', 'seconds', 'total_seconds']

You can filter the results of ``see`` using a wildcard pattern
or a regular expression::

    >>> see(timedelta).filter('*sec*')
        .microseconds       .seconds            .total_seconds()

    >>> see(timedelta).filter('/^d/')
        dir()       divmod()


Contents
--------

.. toctree::
   :maxdepth: 2

   install
   usage
   startup
   dev/index
   authors
   license


Indices and tables
------------------

- :ref:`genindex`
- :ref:`modindex`
- :ref:`search`
