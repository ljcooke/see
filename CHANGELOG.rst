Release History
===============

.. See http://keepachangelog.com/

All notable changes to this project will be documented in this file. This
project adheres to `Semantic Versioning <http://semver.org>`__  as of v1.1.0.


.. Unreleased_
.. --------------------

.. v1.4.0_ / 2017-05-20
.. --------------------

**Added**

- New API for filtering the output of ``see``. Instead of passing in
  a ``pattern`` or ``r`` argument, call ``see().match()`` or ``see().re()``
  respectively.

- Test each of the ``is`` functions from the *inspect* module, such as
  ``isclass`` and ``isgenerator``, and include them in the result.

- Documentation using Sphinx.

**Deprecated**

- Dropped the ``pattern`` and ``r`` arguments. These are still
  this release (via ``*args`` and ``**kwargs``) but they will be removed


v1.3.2_ / 2016-04-30
--------------------

**Fixed**

- Misaligned columns with Unicode attribute names that include wide CJK
  characters or combining characters.


v1.3.1_ / 2016-04-26
--------------------

**Fixed**

- Misaligned columns when some attributes have unusually long names.


v1.3.0_ / 2016-04-24
--------------------

**Added**

- Unit tests, continuous integration with Travis, and coverage reports
  published on Coveralls.io.

- For Windows, adjust the output to fit the terminal width as on other
  platforms.

**Fixed**

- Replaced one instance of ``dir`` with ``hasattr``.


v1.2.0_ / 2016-04-17
--------------------

**Added**

- Support for Python 3.5's matrix multiplication operators.


v1.1.1_ / 2015-04-17
--------------------

**Fixed**

- Broken on Windows due to a dependency on the fcntl module.


v1.1.0_ / 2015-03-27
--------------------

**Added**

- Output is adjusted to fit the terminal width.
- Print ``?`` after any attributes that raised an exception.

**Fixed**

- Unhandled exceptions when reading attributes.


v1.0.1_ / 2010-10-17
--------------------

**Changed**

- License is now BSD (was GPL).


v1.0_ / 2010-07-31
------------------

**Added**

- Justified columns.

**Changed**

- Output is indented to line up with the prompt. For example, if the prompt
  is a single ``>`` followed by a space, the output will be indented by two
  spaces.

**Fixed**

- Exception raised when ``see()`` has nothing to display.


v0.5.4_ / 2009-07-23
--------------------

**Fixed**

- Calling ``see()`` first with no arguments would return nothing.


v0.5.3_ / 2009-04-12
--------------------

**Added**

- Running *see.py* as a script will show documentation, equivalent to
  ``help(see)``.
- If you want to be lazy, you can ``from see import *``, and only ``see()``
  will be imported.

**Changed**

- Results are spaced out more, and line up with the default interpreter prompt.
- Unary operator symbols changed from ``+@`` and ``-@`` to ``+obj`` and
  ``-obj`` respectively.
- Revised code documentation and examples.
- New project homepage.

**Fixed**

- ``see()`` output could be modified, but would still print the original
  results. The output list now acts like a tuple.


v0.5.2_ / 2009-03-16
--------------------

**Added**

- Calling ``see()`` without arguments shows local variables.


v0.5.1_ / 2009-03-13
--------------------

**Changed**

- Filename pattern matching is now the default, e.g. ``see('', '.is*')``.
  Regular expression matching can still be done by using the ``r`` argument.

**Fixed**

- Python 3.0: After the first ``see()`` call, subsequent calls would give no
  output for some objects.
- Python 3.0: Regular expression and filename pattern matching would also
  result in nothing being output.


v0.5_ / 2009-03-07
------------------

**Added**

- Now returns a list-like object, for iterating through the results, while
  still showing the human-readable output when run interactively.
- Optional ``regex`` and ``fn`` arguments, for regular expression and filename
  pattern matching, respectively.


v0.4.1_ / 2009-02-23
--------------------

**Added**

- New attributes: ``str()`` and ``repr()``.


v0.4_ / 2009-02-19
------------------

**Added**

- For Python 3.0, new attributes are included, and deprecated attributes are no
  longer shown.
- Instructions added for using this with iPython.

**Changed**

- (Pseudo-)static variables moved outside the ``see()`` function. This may or
  may not be more efficient.
- If the object has a docstring set, ``help()`` is shown in the list instead of
  ``?``.

**Fixed**

- AttributeError with Django class attributes fixed.
- The correct symbols are now shown for objects implementing ``__divmod__``,
  ``__floordiv__`` and ``__cmp__``.


v0.3.1_ / 2009-02-18
--------------------

**Added**

- Symbols for binary arithmetic operations using reflected (swapped) operands.
- ``with`` and ``reversed()`` symbols.


v0.3_ / 2009-02-18
------------------

**Added**

- Rudimentary Python 3.0 support.
- Created a *setup.py* installation script.

**Fixed**

- Outdated documentation link in the *README* file.


v0.2 / 2009-02-17
-----------------

**Added**

- ``.*`` symbol for the ``__getattr__`` attribute.
- ``help()``` documentation.

**Changed**

- Special attribute symbols reordered.
- Unary addition and subtraction changed to ``+@`` and ``-@`` respectively.


v0.1 / 2009-02-16
-----------------

- Original release.


.. _unreleased: https://github.com/inky/see/compare/v1.3.2...develop

.. _v1.3.2: https://github.com/inky/see/compare/v1.3.1...v1.3.2
.. _v1.3.1: https://github.com/inky/see/compare/v1.3.0...v1.3.1
.. _v1.3.0: https://github.com/inky/see/compare/v1.2.0...v1.3.0
.. _v1.2.0: https://github.com/inky/see/compare/v1.1.1...v1.2.0
.. _v1.1.1: https://github.com/inky/see/compare/v1.1.0...v1.1.1
.. _v1.1.0: https://github.com/inky/see/compare/v1.0.1...v1.1.0

.. _v1.0.1: https://github.com/inky/see/compare/v1.0-fixed...v1.0.1
.. _v1.0:   https://github.com/inky/see/compare/v0.5.4...v1.0-fixed
.. _v0.5.4: https://github.com/inky/see/compare/v0.5.3...v0.5.4
.. _v0.5.3: https://github.com/inky/see/compare/v0.5.2...v0.5.3
.. _v0.5.2: https://github.com/inky/see/compare/v0.5.1...v0.5.2
.. _v0.5.1: https://github.com/inky/see/compare/v0.5...v0.5.1
.. _v0.5:   https://github.com/inky/see/compare/v0.4.1...v0.5
.. _v0.4.1: https://github.com/inky/see/compare/v0.4...v0.4.1
.. _v0.4:   https://github.com/inky/see/compare/v0.3.1...v0.4
.. _v0.3.1: https://github.com/inky/see/compare/v0.3...v0.3.1
.. _v0.3:   https://github.com/inky/see/compare/v0.2...v0.3
