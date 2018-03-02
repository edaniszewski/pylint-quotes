"""Tests for the string quote checker for function-level docstrings.
"""
import sys

import pytest

from pylint_quotes.checker import StringQuoteChecker
from pylint.testutils import Message, set_config

from utils import TRI_Q_DOUB, TRI_Q_SING, StringQuiteCheckerTestCase


@pytest.mark.skipif(sys.version_info < (3, 5), reason='requires python3.5 or python3.6')
class TestAsyncFunctionStringQuoteChecker(StringQuiteCheckerTestCase):
    """ Test case for asynchronous function-level docstrings.
    """
    CHECKER_CLASS = StringQuoteChecker

    @set_config(docstring_quote='double')
    def test_single_line_double_quote_docstring_with_cfg_double(self):

        test_str = '''
async def fn(x):  #@
    """Function level docstring on a single line."""
    pass
'''

        self.check_async_function(test_str)

    @set_config(docstring_quote='single')
    def test_single_line_double_quote_docstring_with_cfg_single(self):

        test_str = '''
async def fn(x):  #@
    """Function level docstring on a single line."""
    pass
'''
        msg = Message(msg_id='invalid-docstring-quote', line=3, args=(TRI_Q_DOUB, TRI_Q_SING))
        self.check_async_function(test_str, msg)

    @set_config(docstring_quote='double')
    def test_single_line_single_quote_docstring_with_cfg_double(self):

        test_str = """
async def fn(x):  #@
    '''Function level docstring on a single line.'''
    pass
"""
        msg = Message(msg_id='invalid-docstring-quote', line=3, args=(TRI_Q_SING, TRI_Q_DOUB))

        self.check_async_function(test_str, msg)

    @set_config(docstring_quote='single')
    def test_single_line_single_quote_docstring_with_cfg_single(self):

        test_str = """
async def fn(x):  #@
    '''Function level docstring on a single line.'''
    pass
"""
        self.check_async_function(test_str)

    @set_config(docstring_quote='double')
    def test_single_line_double_quote_docstring_with_cfg_double_multi_row_def(self):

        test_str = '''
async def fn(  #@
    x
):
    """Function level docstring on a single line."""
    pass
'''

        self.check_async_function(test_str)

    @set_config(docstring_quote='single')
    def test_single_line_double_quote_docstring_with_cfg_single_multi_row_def(self):

        test_str = '''
async def fn(  #@
    x
):
    """Function level docstring on a single line."""
'''
        msg = Message(msg_id='invalid-docstring-quote', line=5, args=(TRI_Q_DOUB, TRI_Q_SING))

        self.check_async_function(test_str, msg)

    @set_config(docstring_quote='double')
    def test_single_line_double_quote_docstring_with_cfg_double_multiple_def(self):

        test_str = '''
async def fn1(x):
    """Function docstring"""

async def fn2(x):  #@
    """Function level docstring on a single line."""

async def fn3(x):
    """Another function level docstring on single line."""
'''

        self.check_async_function(test_str)

    @set_config(docstring_quote='single')
    def test_single_line_double_quote_docstring_with_cfg_single_multiple_def(self):

        test_str = '''
async def fn1(x):
    """Function docstring"""

async def fn2(x):  #@
    """Function level docstring on a single line."""

async def fn3(x):
    """Another function level docstring on single line."""
'''
        msg = Message(msg_id='invalid-docstring-quote', line=6, args=(TRI_Q_DOUB, TRI_Q_SING))

        self.check_async_function(test_str, msg)

    @set_config(docstring_quote='double')
    def test_multi_line_double_quote_docstring_with_cfg_double(self):

        test_str = '''
async def fn(x):  #@
    """Function level docstring
    on multiple lines.
    """
'''

        self.check_async_function(test_str)

    @set_config(docstring_quote='single')
    def test_multi_line_double_quote_docstring_with_cfg_single(self):

        test_str = '''
async def fn(x):  #@
    """Function level docstring
    on multiple lines.
    """
'''
        msg = Message(msg_id='invalid-docstring-quote', line=3, args=(TRI_Q_DOUB, TRI_Q_SING))

        self.check_async_function(test_str, msg)

    @set_config(docstring_quote='double')
    def test_multi_line_single_quote_docstring_with_cfg_double(self):

        test_str = """
async def fn(x):  #@
    '''Function level docstring
    on multiple lines.
    '''
"""
        msg = Message(msg_id='invalid-docstring-quote', line=3, args=(TRI_Q_SING, TRI_Q_DOUB))

        self.check_async_function(test_str, msg)

    @set_config(docstring_quote='single')
    def test_multi_line_single_quote_docstring_with_cfg_single(self):

        test_str = """
async def fn(x):  #@
    '''Function level docstring
    on multiple lines.
    '''
"""

        self.check_async_function(test_str)

    @set_config(docstring_quote='double')
    def test_multi_line_double_quote_docstring_with_cfg_double_multi_row_def(self):

        test_str = '''
async def fn(  #@
    x
):
    """Function level docstring
    on multiple lines.
    """
'''

        self.check_async_function(test_str)

    @set_config(docstring_quote='single')
    def test_multi_line_double_quote_docstring_with_cfg_single_multi_row_def(self):

        test_str = '''
async def fn(  #@
    x
):
    """Function level docstring
    on multiple lines.
    """
'''
        msg = Message(msg_id='invalid-docstring-quote', line=5, args=(TRI_Q_DOUB, TRI_Q_SING))

        self.check_async_function(test_str, msg)

    @set_config(docstring_quote='double')
    def test_multi_line_double_quote_docstring_with_cfg_double_multiple_def(self):

        test_str = '''
async def fn1(x):
    """Function docstring
    on multiple lines.
    """

async def fn2(x):  #@
    """Function level docstring
    on multiple lines.
    """

async def fn3(x):
    """Another function level docstring
    on multiple lines.
    """
'''

        self.check_async_function(test_str)

    @set_config(docstring_quote='single')
    def test_multi_line_double_quote_docstring_with_cfg_single_multiple_def(self):

        test_str = '''
async def fn1(x):
    """Function docstring
    on multiple lines.
    """

async def fn2(x):  #@
    """Function level docstring
    on multiple lines.
    """

async def fn3(x):
    """Another function level docstring
    on multiple lines.
    """
'''
        msg = Message(msg_id='invalid-docstring-quote', line=8, args=(TRI_Q_DOUB, TRI_Q_SING))

        self.check_async_function(test_str, msg)

    @set_config(docstring_quote='double')
    def test_single_line_double_quote_docstring_with_cfg_double_def_contents_01(self):

        test_str = '''
async def fn(x):  #@
    """Function level docstring on a single line."""
    return 33
'''

        self.check_async_function(test_str)

    @set_config(docstring_quote='single')
    def test_single_line_double_quote_docstring_with_cfg_single_def_contents_01(self):

        test_str = '''
async def fn(x):  #@
    """Function level docstring on a single line."""
    return 33
'''
        msg = Message(msg_id='invalid-docstring-quote', line=3, args=(TRI_Q_DOUB, TRI_Q_SING))

        self.check_async_function(test_str, msg)

    @set_config(docstring_quote='double')
    def test_single_line_double_quote_docstring_with_cfg_double_def_contents_02(self):

        test_str = '''
async def fn(x):  #@
    """Function level docstring on a single line."""

    # this is a dictionary
    values = {1:2, 3:4}

    return values.get(x)
'''

        self.check_async_function(test_str)

    @set_config(docstring_quote='single')
    def test_single_line_double_quote_docstring_with_cfg_single_def_contents_02(self):

        test_str = '''
async def fn(x):  #@
    """Function level docstring on a single line."""

    # this is a dictionary
    values = {1:2, 3:4}

    return values.get(x)
'''
        msg = Message(msg_id='invalid-docstring-quote', line=3, args=(TRI_Q_DOUB, TRI_Q_SING))

        self.check_async_function(test_str, msg)

    @set_config(docstring_quote='double')
    def test_single_line_double_quote_docstring_with_cfg_double_def_contents_03(self):

        test_str = '''
async def fn(x):  #@
    """Function level docstring on a single line."""

    # define a function in a function
    def local_fn(z):
        """Function within a function - inception"""
        return z * z

    return local_fn(x)
'''

        self.check_async_function(test_str)

    @set_config(docstring_quote='single')
    def test_single_line_double_quote_docstring_with_cfg_single_def_contents_03(self):

        test_str = '''
async def fn(x):  #@
    """Function level docstring on a single line."""

    # define a function in a function
    def local_fn(z):
        """Function within a function - inception"""
        return z * z

    return local_fn(x)
'''
        msg = Message(msg_id='invalid-docstring-quote', line=3, args=(TRI_Q_DOUB, TRI_Q_SING))

        self.check_async_function(test_str, msg)
