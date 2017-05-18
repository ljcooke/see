see: dir for humans
===================

.. image:: https://img.shields.io/pypi/v/see.svg
    :target: https://pypi.python.org/pypi/see

.. image:: https://travis-ci.org/araile/see.svg?branch=develop
    :target: https://travis-ci.org/araile/see

.. image:: https://coveralls.io/repos/github/araile/see/badge.svg?branch=develop
    :target: https://coveralls.io/github/araile/see?branch=develop

**see** is an alternative to the built-in ``dir`` function in Python. It shows
you what you can do with things.

Supports Python 2.6+ and 3.3+. Also works in iPython and PyPy.

Licensed under the BSD 3-Clause License. See the *LICENSE* file.

Contributions are welcome. See the *CODE_OF_CONDUCT.md*, *CHANGELOG.rst*
and *AUTHORS.rst* files.


Install
-------

To install **see**, run::

    $ pip3 install --upgrade see


Usage
-----

**see** is designed for the interactive Python interpreter. Import the ``see``
function like so::

    >>> from see import see

Call ``see()`` without arguments to see all objects in the global scope. ::

    >>> foo = 'bar'
    >>> see()
        foo      see()

Call ``see(an_object)`` to see what you can do with ``an_object``. ::

    >>> number = 1
    >>> see(number)
        +                -                *                /                //
        %                **               <<               >>               &
        ^                |                +obj             -obj             ~
        <                <=               ==               !=               >
        >=               abs()            bool()           dir()
        divmod()         float()          hash()           help()
        hex()            int()            oct()            repr()
        round()          str()            .bit_length()    .conjugate()
        .denominator     .from_bytes()    .imag            .numerator
        .real            .to_bytes()


Startup
-------

You can use a Python startup file to ensure that ``see`` is available every
time you run Python. The following example uses a startup file named
``.pythonrc.py`` in the user's home directory:

1. Create the Python startup file, if it does not already exist::

       $ touch ~/.pythonrc.py

2. Open this file in your preferred editor. Add the following line::

       from see import see

3. Set the following environment variable (e.g. in ``~/.bashrc`` for Bash)::

       $ export PYTHONSTARTUP="$HOME/.pythonrc.py"

Now you can use ``see`` immediately after running ``python``, without having to
manually import it.
