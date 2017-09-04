"""Test the plugin registration method.
"""

from pylint.lint import PyLinter

from pylint_quotes.plugin import register


def test_register():
    linter = PyLinter()

    assert 'string_quotes' not in linter._checkers

    register(linter)

    assert 'string_quotes' in linter._checkers
