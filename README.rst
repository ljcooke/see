see: dir for humans
===================

.. image:: https://img.shields.io/pypi/v/see.svg
    :target: https://pypi.python.org/pypi/see

.. see/docs <common-badges>

.. image:: https://travis-ci.org/araile/see.svg?branch=develop
    :target: https://travis-ci.org/araile/see

.. image:: https://coveralls.io/repos/github/araile/see/badge.svg?branch=develop
    :target: https://coveralls.io/github/araile/see?branch=develop

.. see/docs </common-badges>


.. see/docs <summary>

**see** is a legible alternative to ``dir()``, for Python 2.6+ and 3.3+.

It neatly summarises what you can do with an object.
Use it to inspect your code or learn new APIs.

.. see/docs </summary>


Example
-------

.. For examples, use a 64-column terminal and set sys.ps1 = '>>> '

.. see/docs <example>

Try inspecting an object with ``see``::

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

This reveals some information about the ``timedelta`` object, such as:

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

.. see/docs </example>


Documentation
-------------

Documentation is available at https://araile.github.io/see/

* `Installation <https://araile.github.io/see/install.html>`_
* `Usage <https://araile.github.io/see/usage.html>`_
* `Startup File <https://araile.github.io/see/startup.html>`_
* `Developer Reference <https://araile.github.io/see/dev/index.html>`_


Contributing
------------

The source code is maintained
`on GitHub <https://github.com/araile/see>`_.
Contributions are welcome.

* `Change Log <https://github.com/araile/see/blob/develop/CHANGELOG.rst>`_
* `Code of Conduct <https://github.com/araile/see/blob/develop/CODE_OF_CONDUCT.md>`_
* `Authors <https://github.com/araile/see/blob/develop/AUTHORS.rst>`_
* `License <https://github.com/araile/see/blob/develop/LICENSE>`_
