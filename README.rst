see
===

An alternative to Python's ``dir`` function.
Easy to type; easy to read! For humans only.

**Requirements**:
Python 2.4+ or 3.0

**License**:
BSD (see the LICENSE file)

Contributions are welcome. See the CHANGELOG and AUTHORS files.


Install
-------

To install **see**, run:

::

    $ pip install --upgrade see

Alternatively, to install from source:

::

    $ python setup.py install


Usage
-----

**see** is designed for the interactive Python interpreter. Import the ``see``
function like so:

::

    >>> from see import see

Call ``see()`` without arguments to see all objects in the global scope.

::

    >>> foo = 'bar'
    >>> see()
        foo      see()

Call ``see(an_object)`` to see what you can do with ``an_object``.

::

    >>> number = 1
    >>> see(number)
        +             -             *             /             //            %
        **            <<            >>            &             ^             |
        +obj          -obj          ~             <             <=            ==
        !=            >             >=            abs()         bool()
        divmod()      float()       hash()        help()        hex()
        int()         long()        oct()         repr()        str()
        .bit_length()               .conjugate()  .denominator  .imag
        .numerator    .real


Startup
-------

You can use a Python startup file to ensure that ``see`` is available every
time you run Python. The following example uses a startup file named
``.pythonrc.py`` in the user's home directory:

1. Create a startup file, if one does not already exist:

   ::

       touch ~/.pythonrc.py

2. Open the startup file in your preferred Python editor and add the
   following line:

   ::

       from see import see

3. Set the following environment variable (e.g. in ``~/.bashrc`` for Bash):

   ::

       export PYTHONSTARTUP="$HOME/.pythonrc.py"

Now you can use ``see`` immediately after running ``python``, without having to
manually import it.


Startup for iPython
-------------------

For iPython users, importing ``see`` by default requires a little more work.

1. Create a file named ``ipy_profile_see.py`` in your ``~/.ipython`` directory,
   and add the following lines:

   ::

       from IPython import ipapi

       def main():
           ip = ipapi.get()
           ip.ex('from see import see')

       main()

2. From here, you have two options:

   1. Launch iPython with the command: ``ipython -profile see``

   2. Open ``~/.ipython/ipy_user_conf.py`` and add the following line inside
      the ``main()`` function:

      ::

          import ipy_profile_see
