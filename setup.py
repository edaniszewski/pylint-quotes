"""Setup for the pylint-quotes package.
"""

import os
import re
from setuptools import setup, find_packages


def find_version(*file_paths):
    """Return version defined in __init__.py without import pylint"""
    with open(os.path.join(*file_paths)) as fhandler:
        version_file = fhandler.read()
        version_match = re.search(r'^__version__ = [\'"]([^\'"]*)[\'"]',
                                  version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError('Unable to find version string.')


setup(
    name='pylint-quotes',
    description='Quote consistency checker for Pylint',
    license='MIT',
    version=find_version("pylint_quotes", "__init__.py"),
    author='Erick Daniszewski',
    author_email='edaniszewski@gmail.com',
    url='https://github.com/edaniszewski/pylint-quotes',
    install_requires=[
        'pylint',
    ],
    packages=find_packages(),
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Topic :: Software Development',
        'Topic :: Utilities'
    ],
    keywords='pylint linting string quotes'
)
