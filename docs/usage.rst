Usage
=====

.. module:: see


``see()`` function
------------------

The ``see`` function is designed for the interactive Python interpreter.
Import it by running::

    >>> from see import see

.. autofunction:: see
   :noindex:


Startup file
------------

You can use a Python startup file to ensure that the ``see`` function is
available every time you run Python. The following example uses a file named
``.pythonrc.py`` in the user's home directory:

1. Create the Python startup file, if it does not already exist:

   .. code-block:: shell

      $ touch ~/.pythonrc.py

2. Open this file in your preferred editor. Add the following line::

      from see import see

3. Set the following environment variable:

   .. code-block:: shell

      $ export PYTHONSTARTUP="$HOME/.pythonrc.py"

   For example, with the Bash shell, you can add this to the ``~/.bashrc``
   file.

Now you can use ``see`` immediately after running the Python interpreter,
without having to manually import it.
