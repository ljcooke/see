#!/usr/bin/env python

from setuptools import setup

setup(name='see',
      version='1.2.0',
      description='A human-readable alternative to dir',
      author='Liam Cooke',
      author_email='see@araile.com',
      url='http://araile.github.io/see/',
      py_modules=['see'],
      test_suite='tests',
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Environment :: Console',
          'Intended Audience :: Developers',
          'License :: Freely Distributable',
          'License :: OSI Approved :: BSD License',
          'Natural Language :: English',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Topic :: Software Development',
      ])
