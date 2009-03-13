Change log
==========


v0.5.1
------

  * Filename pattern matching is now the default. For example:

        > see('', '.is*')
          .isalnum()   .isalpha()   .isdigit()   .islower()   .isspace()
          .istitle()   .isupper()

    Regular expression matching can still be done, using the `r` argument.

  * Two bugs fixed for Python 3.0:

      * After the first `see()` call, subsequent calls would give no
        output for some objects.

      * Regular expression and filename pattern matching would also result
        in nothing being output.


v0.5
----

  * Now returns a list-like object, for iterating through the results, while
    still showing the human-readable output when run interactively.
    _(Contributed by Bob Farrell.)_


  * Optional `regex` and `fn` arguments, for regular expression and filename
    pattern matching, respectively.
    _(Contributed by [Ed Page][epage].)_


v0.4.1
------

  * New attributes: `str()` and `repr()`.
    _(`str()` contributed by [Guff][guff].)_


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
[epage]: http://github.com/epage
[ghoseb]: http://github.com/ghoseb
[guff]: http://github.com/Guff
[igowen]: http://ian.gowen.cc/
[jdunck]: http://github.com/jdunck
