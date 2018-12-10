# Pylint Quote Checker
[![Build Status](https://travis-ci.org/edaniszewski/pylint-quotes.svg?branch=master)](https://travis-ci.org/edaniszewski/pylint-quotes)
[![Coverage Status](https://coveralls.io/repos/github/edaniszewski/pylint-quotes/badge.svg?branch=master)](https://coveralls.io/github/edaniszewski/pylint-quotes?branch=master)
[![Latest Version](https://img.shields.io/pypi/v/pylint-quotes.svg)](https://pypi.python.org/pypi/pylint-quotes)
[![License](https://img.shields.io/github/license/edaniszewski/pylint-quotes.svg)](LICENSE)

A Pylint plugin for checking the consistency of string quotes.

## Example

### before
Below is an example python file that uses inconsistent string quotes.

`example.py`
```python
"""Example python file."""


def main(output="default"):
    '''Entrypoint to the example script which prints out the
    value in the 'output' variable.
    '''
    print(output)


if __name__ == "__main__":
    main('testing')
```
which would yield
```
➜ pylint --load-plugins pylint_quotes example.py 

No config file found, using default configuration
************* Module example
C:  4, 0: Invalid string quote ", should be ' (invalid-string-quote)
C: 11, 0: Invalid string quote ", should be ' (invalid-string-quote)
C:  5, 0: Invalid docstring quote ''', should be """ (invalid-docstring-quote)

-----------------------------------
Your code has been rated at 2.50/10
```

### after
Fixing up the example above based on linting recommendations,

`example.py`
```python
"""Example python file."""


def main(output='default'):
    """Entrypoint to the example script which prints out the
    value in the 'output' variable.
    """
    print(output)


if __name__ == '__main__':
    main('testing')
```
which yields
```
➜ pylint --load-plugins pylint_quotes example.py 

No config file found, using default configuration

-------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 2.50/10, +7.50)
```

### Example Package
An example package is found in the [`example/`](example) directory.

```
➜ pylint --load-plugins pylint_quotes example

************* Module foo.__init__
example/foo/__init__.py:3:0: C4001: Invalid string quote ", should be ' (invalid-string-quote)
************* Module foo
example/foo/__init__.py:1:0: C0102: Black listed name "foo" (blacklisted-name)
************* Module foo.other
example/foo/other.py:1:0: C4003: Invalid docstring quote ''', should be """ (invalid-docstring-quote)
example/foo/other.py:4:0: R0903: Too few public methods (1/2) (too-few-public-methods)
example/foo/other.py:10:0: C4002: Invalid triple quote """, should be ''' (invalid-triple-quote)
************* Module foo.utils
example/foo/utils.py:15:0: C4001: Invalid string quote ", should be ' (invalid-string-quote)
example/foo/utils.py:5:0: C4003: Invalid docstring quote ''', should be """ (invalid-docstring-quote)
example/foo/utils.py:10:0: C4003: Invalid docstring quote ''', should be """ (invalid-docstring-quote)

------------------------------------------------------------------
Your code has been rated at 1.11/10 (previous run: 1.11/10, +0.00)
```


## Installation

Installing with `pip`:
```
pip install pylint-quotes
```

Installing with `pipenev`:
```
pipenv install pylint-quotes
```

## Usage
To use pylint-quotes, it must loaded in as a plugin when running pylint
```
pylint --load-plugins pylint_quotes <module-or-package>
```

## Checks
pylint-quotes provides a single `StringQuoteChecker` that checks for consistency
between
 - single quote string literals
   ```python
   x = 'example'
   y = "example"
   ```
 - triple quote strings
   ```python
   """ single line block comments """
   '''
      multi-line block comments too
   '''
   
   x = '''example'''
   y = """
   example
   """
   ```
 - docstrings (module, class, function, async function)
   ```python
   def x():
       '''Example'''
       pass
       
   def y():
       """
           Multi-line example.
       """
       pass
  
   async def z():
       """Async example.
       """
       pass
   ```

## Configuration
The string quote type can be configured as either 'single' or 'double' in the configuration
file. For example, to check for single quote string literals, double quote triple quoted 
string, and double quoted docstrings,
```ini
string-quote=single
triple-quote=double
docstring-quote=double
```

the default configuration is
```ini
string-quote=single
triple-quote=single
docstring-quote=double
```

Additionally the `string-quote` can be configured to avoid escaping: by default
it enforces one type but if using the other type would avoid some escaping then
it enforces the other one. To use those smart types the config is
'single-avoid-escape', and 'double-avoid-escape'.


## Developing
If you wish to develop the pylint-quotes project to fix a bug, add a feature, or
extend it for your own uses, the [Makefile](Makefile) provides a bunch of helpful
development targets. For a full list of the targets, see the Makefile, or you can
use `make help`.

For convenience, `pipenv` is used to manage development dependencies. Before starting
development, you should `make init` to install `pipenv` if you don't already have it and
create a virtualenv with the project development dependencies. From there, you can use:
- `make test` to run the unit tests
- `make coverage` to run unit tests and get a coverage report
- `make lint` to perform source code linting

## License
Pylint-quotes is licensed under an MIT license -- see [LICENSE](LICENSE) for more info.