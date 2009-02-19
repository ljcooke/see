Change log
==========


v0.4
----

  * For Python 3.0, new attributes are included, and deprecated attributes
    are no longer shown.
    _(Contributed by Gabriel Genellina.)_

  * AttributeError with Django class attributes fixed.
    _(Contributed by [jdunck][jdunck].)_

  * The correct symbols are now shown for objects implementing
    `__divmod__`, `__floordiv__` and `__cmp__`.
    _(Contributed by Gabriel Genellina.)_

  * (Pseudo-)static variables moved outside the `see()` function.
    This may or may not be more efficient.

  * If the object has a docstring set, 'help()' is shown in the list
    instead of '?'.
    _(Suggested by [edcrypt][edcrypt].)_

  * Instructions added for using this with iPython.
    _(Contributed by [Baishampayan Ghose][ghoseb].)_


v0.3.1
------

  * Added symbols for binary arithmetic operations using reflected
    (swapped) operands.

  * 'with' and 'reversed()' symbols added.


v0.3
----

  * Rudimentary Python 3.0 support, using suggestions from
    [CommodoreGuff][CommodoreGuff].

  * Created a _setup.py_ installation script.

  * Change an outdated documentation link in the _README_ file.
    _(Suggested by [Ian Gowen][igowen].)_


v0.2
----

  * Special attribute symbols reordered.

  * Unary addition and subtraction changed to `+@` and `-@` respectively.

  * Added '.*' symbol for the `__getattr__` attribute.

  * `help()` documentation added.


v0.1
----

  * Original.


[CommodoreGuff]: http://www.reddit.com/user/CommodoreGuff/
[edcrypt]: http://github.com/edcrypt
[ghoseb]: http://github.com/ghoseb
[igowen]: http://ian.gowen.cc/
[jdunck]: http://github.com/jdunck
