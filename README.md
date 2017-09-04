# Pylint Quote Checker
A Pylint plugin for checking the consistency of string quotes.

## Example

### before
Below is an example python file that uses inconsistent string quotes.

`example.py`
```python
"""Example python file.
"""


def main(output="default"):
    '''Entrypoint to the example script which prints out the
    value in the 'output' variable.
    '''
    print output


if __name__ == "__main__":
    main('testing')
```
which would yield
```
No config file found, using default configuration
************* Module example
C:  5, 0: Invalid string quote ", should be ' (invalid-string-quote)
C: 12, 0: Invalid string quote ", should be ' (invalid-string-quote)
C:  6, 0: Invalid docstring quote ''', should be """ (invalid-docstring-quote)

------------------------------------------------------------------
Your code has been rated at 2.50/10 (previous run: 2.50/10, +0.00)
```

### after
Fixing up the example above based on linting recommendations,

`example.py`
```python
"""Example python file.
"""


def main(output='default'):
    """Entrypoint to the example script which prints out the
    value in the 'output' variable.
    """
    print output


if __name__ == '__main__':
    main('testing')
```
which yields
```
No config file found, using default configuration

-------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 2.50/10, +7.50)
```

## Installation

```
pip install pylint-quotes
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
 - docstrings (module, class, function)
   ```python
   def x():
       '''Example'''
       pass
       
   def y():
       """
           Multi-line example.
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
