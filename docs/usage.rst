.. index::
   single: Usage

Usage
=====

.. module:: see


Import see
----------

The function named ``see`` is all you need.
In the Python interpreter, run::

    >>> from see import see

.. include:: install.rst
   :start-after: see/docs <use-startup>
   :end-before: see/docs </use-startup>


Inspect an object
-----------------

.. autofunction:: see
   :noindex:


Examine the results
-------------------

.. autoclass:: see.output.SeeResult
   :noindex:
   :members:
   :undoc-members:
   :inherited-members:


Symbols
-------

Some special symbols are used in the output from ``see`` to show the features
of the object.

``()``
    | Object is a function or may be called like a function.
    | Example: ``obj()``
``.*``
    | Object implements ``__getattr__``, so it may allow you to access
      attributes that are not defined.
    | Example: ``obj.anything``.
``[]``
    | Object supports the ``[]`` syntax.
    | Example: ``obj[index]``
``with``
    | Object can be used in a ``with`` statement.
    | Example: ``with obj as target``
``in``
    | Object supports the ``in`` operator.
    | Example: ``for item in obj``
``+ - * / // % **``
    | Object supports these arithmetic operators.
    | Example: ``obj + 1``
``<< >> & ^ |``
    | Object supports these bitwise operators.
    | Example: ``obj << 1``
``+obj -obj``
    | Object supports the unary arithmetic operators ``+`` (positive)
      and ``-`` (negative) respectively.
    | Example: ``+1``, ``-1``
``~``
    | Object supports the unary bitwise operator ``~`` (invert).
    | Example: ``~1``
``< <= == != > >=``
    | Object supports these comparison operators.
    | Example: ``obj << 1``
``@``
    | Object supports the ``@`` operator (matrix multiplication),
      introduced in Python 3.5.
    | Example: ``obj @ matrix``
