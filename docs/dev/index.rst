.. API docs, modified from the output of:
   sphinx-apidoc -e -M -f -o docs/api see

Contributing
============

Get the source code
-------------------

The :index:`source code` is maintained
`on GitHub <https://github.com/araile/see>`_.
Contributions are welcome.

* `Change Log <https://github.com/araile/see/blob/develop/CHANGELOG.rst>`_
* `Code of Conduct <https://github.com/araile/see/blob/develop/CODE_OF_CONDUCT.md>`_


Continuous integration
----------------------

The code repository on GitHub is integrated with a few continuous integration
services which come into effect each time code is pushed:

* `Travis CI <https://travis-ci.org/araile/see>`_ runs the unit tests in
  a Linux environment for each supported Python release.
* `AppVeyor <https://ci.appveyor.com/project/araile/see>`_ runs the unit tests
  in a Windows environment.
* `Coveralls <https://coveralls.io/github/araile/see>`_ tracks how much of the
  code is covered by the unit tests. This is updated by Travis when a test
  succeeds.


Module reference
----------------

.. toctree::

   see.exceptions
   see.features
   see.inspector
   see.output
   see.term
   see.tools
