#!/usr/bin/env python
import sys
from setuptools import setup

tests_require = [
    'mock>=2.0.0' if sys.version_info < (3, 3) else None,
    'unittest2>=1.1.0' if sys.version_info < (2, 7) else None,
]

setup(name='see',
      version='1.3.2',
      description='dir for humans',
      author='Liam Cooke',
      author_email='see@araile.com',
      license='BSD License',
      url='http://araile.github.io/see/',
      py_modules=['see'],
      install_requires=[],
      test_suite='tests',
      tests_require=[lib for lib in tests_require if lib],
      zip_safe=True,
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Environment :: Console',
          'Intended Audience :: Developers',
          'License :: Freely Distributable',
          'License :: OSI Approved :: BSD License',
          'Natural Language :: English',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3.2',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: Implementation :: CPython',
          'Programming Language :: Python :: Implementation :: PyPy',
          'Topic :: Software Development',
      ])
