.. index::
   single: Installation

Installation
============

**see** supports Python 2.7 and 3.4+.

The latest release can be found on the
`Python Package Index <https://pypi.org/project/see/>`_.


Install with Pip
----------------

Run the following command in your terminal to install the latest release:

.. code-block:: shell

   $ pip3 install --upgrade see

For Python 2, change ``pip3`` to ``pip2``.


After installing
----------------

Once **see** is installed, launch an interactive Python interpreter and try
importing the ``see`` function:

.. code-block:: shell

   $ python3  # or python2

.. code-block:: python

   >>> from see import see
   >>> see('hello')

.. see/docs <use-startup>

You can use a :doc:`startup file <startup>` to ensure that ``see`` is always
imported when you start Python.

.. see/docs </use-startup>
