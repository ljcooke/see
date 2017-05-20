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

.. image:: https://travis-ci.org/araile/see.svg?branch=develop
    :target: https://travis-ci.org/araile/see

.. image:: https://coveralls.io/repos/github/araile/see/badge.svg?branch=develop
    :target: https://coveralls.io/github/araile/see?branch=develop

**see** is an alternative to ``dir()`` in Python.
It shows you a summary of what you can do with an object.

To get started, see the :doc:`install` and :doc:`usage` pages.


Example
-------

Compare the following::

    >>> dir([])
    ['__add__', '__class__', '__contains__', '__delattr__', '__delit
    em__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '
    __getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd_
    _', '__imul__', '__init__', '__init_subclass__', '__iter__', '__
    le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__r
    educe__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__
    ', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__sub
    classhook__', 'append', 'clear', 'copy', 'count', 'extend', 'ind
    ex', 'insert', 'pop', 'remove', 'reverse', 'sort']

::

    >>> see([])
        []            in            +             +=            *
        *=            <             <=            ==            !=
        >             >=            dir()         hash()
        help()        iter()        len()         repr()
        reversed()    str()         .append()     .clear()
        .copy()       .count()      .extend()     .index()
        .insert()     .pop()        .remove()     .reverse()
        .sort()


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
