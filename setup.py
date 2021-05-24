#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Setup for the pylint-quotes package."""

import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

about = {}
with open(os.path.join(here, 'pylint_quotes', '__version__.py'), 'r') as f:
    exec(f.read(), about)


setup(
    name=about['__title__'],
    description=about['__description__'],
    license=about['__license__'],
    version=about['__version__'],
    author=about['__author__'],
    author_email=about['__author_email__'],
    url=about['__url__'],
    install_requires=[
        'pylint>=1.7.6',
    ],
    python_requires=">=3.4",
    packages=['pylint_quotes'],
    zip_safe=False,
    classifiers=(
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development',
        'Topic :: Utilities'
    ),
    keywords='pylint linting string quotes',
)
