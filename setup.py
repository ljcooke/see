#!/usr/bin/env python

from setuptools import setup

setup(name='see',
      version='1.2.0',
      description='dir for humans',
      author='Liam Cooke',
      author_email='see@araile.com',
      license='BSD License',
      url='http://araile.github.io/see/',
      py_modules=['see'],
      install_requires=[],
      test_suite='tests',
      tests_require=[
          'unittest2>=1.1.0',
      ],
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
          'Programming Language :: Python :: Implementation :: PyPy',
          'Topic :: Software Development',
      ])
