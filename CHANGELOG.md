Change Log
==========

All notable changes to this project will be documented in this file.
This project adheres to [Semantic Versioning][semver] as of v1.1.0.

## [v1.1.1][] / 2015-04-17

### Fixed

  * Broken on Windows due to a dependency on the fcntl module.
    _(Spotted by Christopher Toth.)_


## [v1.1.0][] / 2015-03-27

### Added

  * Output is adjusted to fit the terminal width.

  * Print '?' after any attributes that raised an exception.
    _(Contributed by Andrei Fokau.)_

### Fixed

  * Unhandled exceptions when reading attributes.
    _(Patch contributed by Andrei Fokau.)_


## [v1.0.1][] / 2010-10-17

### Changed

  * Changed the license from GPL to BSD.


## [v1.0][] / 2010-07-31

### Added

  * Justified columns.
    _(Contributed by Steve Losh.)_

### Changed

  * Output is indented to line up with the prompt. For example, if the prompt
    string is "<code>&gt;&nbsp;</code>", the output will be indented by two
    spaces. _(Contributed by Liam Cooke with a bug fix from Adam Lloyd.)_

### Fixed

  * Exception raised when `see()` has nothing to display.


## [v0.5.4][] / 2009-07-23

### Fixed

  * Calling `see()` first with no arguments would return nothing.


## [v0.5.3][] / 2009-04-12

### Added

  * Running `see.py` as a script will show documentation, equivalent
    to `help(see)`.

  * If you want to be lazy, you can '`from see import *`', and only `see()`
    will be imported.

### Changed

  * Results are spaced out more, and line up with the default interpreter prompt.
    For example:

        >>> see(int, pattern='h*')
            hash()    help()    hex()

  * Unary operator symbols changed from `+@` and `-@` to `+obj` and `-obj`
    respectively.

  * Revised code documentation and examples.

  * New project homepage: http://inky.github.com/see/

### Fixed

  * `see()` output could be modified, but would still print the original
    results. The output list now acts like a tuple.


## [v0.5.2][] / 2009-03-16

### Added

  * Calling `see()` without arguments shows local variables.
    _(Contributed by Charlie Nolan.)_


## [v0.5.1][] / 2009-03-13

### Changed

  * Filename pattern matching is now the default. For example:

        > see('', '.is*')
          .isalnum()   .isalpha()   .isdigit()   .islower()   .isspace()
          .istitle()   .isupper()

    Regular expression matching can still be done, using the `r` argument.

### Fixed

  * Python 3.0: After the first `see()` call, subsequent calls would give no
    output for some objects.

  * Python 3.0: Regular expression and filename pattern matching would also
    result in nothing being output.


## [v0.5][] / 2009-03-07

### Added

  * Now returns a list-like object, for iterating through the results, while
    still showing the human-readable output when run interactively.
    _(Contributed by Bob Farrell.)_

  * Optional `regex` and `fn` arguments, for regular expression and filename
    pattern matching, respectively.
    _(Contributed by Ed Page.)_


## [v0.4.1][] / 2009-02-23

### Added

  * New attributes: `str()` and `repr()`.
    _(`str()` contributed by Guff.)_


## [v0.4][] / 2009-02-19

### Added

  * For Python 3.0, new attributes are included, and deprecated attributes
    are no longer shown.
    _(Contributed by Gabriel Genellina.)_

  * Instructions added for using this with iPython.
    _(Contributed by Baishampayan Ghose.)_

### Changed

  * (Pseudo-)static variables moved outside the `see()` function.
    This may or may not be more efficient.

  * If the object has a docstring set, 'help()' is shown in the list
    instead of '?'.
    _(Suggested by Eduardo de Oliveira Padoan.)_

### Fixed

  * AttributeError with Django class attributes fixed.
    _(Contributed by Jeremy Dunck.)_

  * The correct symbols are now shown for objects implementing
    `__divmod__`, `__floordiv__` and `__cmp__`.
    _(Contributed by Gabriel Genellina.)_


## [v0.3.1][] / 2009-02-18

### Added

  * Symbols for binary arithmetic operations using reflected
    (swapped) operands.

  * 'with' and 'reversed()' symbols.


## [v0.3][] / 2009-02-18

### Added

  * Rudimentary Python 3.0 support.
    _(Suggestions by CommodoreGuff.)_

  * Created a _setup.py_ installation script.

### Fixed

  * Outdated documentation link in the _README_ file.
    _(Spotted by Ian Gowen.)_


## v0.2 / 2009-02-17

### Added

  * Added '.\*' symbol for the `__getattr__` attribute.

  * `help()` documentation added.

### Changed

  * Special attribute symbols reordered.

  * Unary addition and subtraction changed to `+@` and `-@` respectively.


## v0.1 / 2009-02-16

  * Original release.


[unreleased]: https://github.com/inky/see/compare/v1.1.1...develop
[v1.1.1]: https://github.com/inky/see/compare/v1.1.0...v1.1.1
[v1.1.0]: https://github.com/inky/see/compare/v1.0.1...v1.1.0
[v1.0.1]: https://github.com/inky/see/compare/v1.0-fixed...v1.0.1
[v1.0]: https://github.com/inky/see/compare/v0.5.4...v1.0-fixed
[v0.5.4]: https://github.com/inky/see/compare/v0.5.3...v0.5.4
[v0.5.3]: https://github.com/inky/see/compare/v0.5.2...v0.5.3
[v0.5.2]: https://github.com/inky/see/compare/v0.5.1...v0.5.2
[v0.5.1]: https://github.com/inky/see/compare/v0.5...v0.5.1
[v0.5]: https://github.com/inky/see/compare/v0.4.1...v0.5
[v0.4.1]: https://github.com/inky/see/compare/v0.4...v0.4.1
[v0.4]: https://github.com/inky/see/compare/v0.3.1...v0.4
[v0.3.1]: https://github.com/inky/see/compare/v0.3...v0.3.1
[v0.3]: https://github.com/inky/see/compare/v0.2...v0.3

[semver]: http://semver.org/
[keepachangelog]: http://keepachangelog.com/
