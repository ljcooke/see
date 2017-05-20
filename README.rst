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

**see** is an alternative to Python's ``dir()``.
It shows you a neat summary of what you can do with an object.
Use it to debug your code or learn new APIs.

For Python 2.6+ and 3.3+.

.. see/docs </summary>


Example
-------

.. For examples, use a 64-column terminal and set sys.ps1 = '>>> '

.. see/docs <example>

Try inspecting a list with ``see``::

    >>> see(list)
        []            in            +             +=            *
        *=            <             <=            ==            !=
        >             >=            dir()         hash()
        help()        iter()        len()         repr()
        reversed()    str()         .append()     .clear()
        .copy()       .count()      .extend()     .index()
        .insert()     .pop()        .remove()     .reverse()
        .sort()

Some of the information revealed here:

* You can use the ``in`` keyword with a list.
* You can get the length of a list with ``len()``.
* The list has a ``count`` attribute that is a function.

Compare with the output of ``dir``::

    >>> dir(list)
    ['__add__', '__class__', '__contains__', '__delattr__', '__delit
    em__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '
    __getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd_
    _', '__imul__', '__init__', '__init_subclass__', '__iter__', '__
    le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__r
    educe__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__
    ', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__sub
    classhook__', 'append', 'clear', 'copy', 'count', 'extend', 'ind
    ex', 'insert', 'pop', 'remove', 'reverse', 'sort']

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
