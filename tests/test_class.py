"""Tests for the string quote checker for class-level docstrings.
"""

from pylint_quotes.checker import StringQuoteChecker
from pylint.testutils import Message, set_config

from utils import TRI_Q_DOUB, TRI_Q_SING, StringQuiteCheckerTestCase


class TestClassStringQuoteChecker(StringQuiteCheckerTestCase):
    """ Test case for class-level docstrings.
    """
    CHECKER_CLASS = StringQuoteChecker

    @set_config(docstring_quote='double')
    def test_single_line_double_quote_docstring_with_cfg_double(self):

        test_str = '''
class TestClass(object):  #@
    """Class level docstring on a single line."""
'''

        self.check_class(test_str)

    @set_config(docstring_quote='single')
    def test_single_line_double_quote_docstring_with_cfg_single(self):

        test_str = '''
class TestClass(object):  #@
    """Class level docstring on a single line."""
'''
        msg = Message(msg_id='invalid-docstring-quote', line=3, args=(TRI_Q_DOUB, TRI_Q_SING))

        self.check_class(test_str, msg)

    @set_config(docstring_quote='double')
    def test_single_line_single_quote_docstring_with_cfg_double(self):

        test_str = """
class TestClass(object):  #@
    '''Class level docstring on a single line.'''
"""
        msg = Message(msg_id='invalid-docstring-quote', line=3, args=(TRI_Q_SING, TRI_Q_DOUB))

        self.check_class(test_str, msg)

    @set_config(docstring_quote='single')
    def test_single_line_single_quote_docstring_with_cfg_single(self):

        test_str = """
class TestClass(object):  #@
    '''Class level docstring on a single line.'''
"""

        self.check_class(test_str)

    @set_config(docstring_quote='double')
    def test_single_line_double_quote_docstring_with_cfg_double_multi_row_cls(self):

        test_str = '''
class TestClass(  #@
    object
):
    """Class level docstring on a single line."""
'''

        self.check_class(test_str)

    @set_config(docstring_quote='single')
    def test_single_line_double_quote_docstring_with_cfg_single_multi_row_cls(self):

        test_str = '''
class TestClass(  #@
    object
):
    """Class level docstring on a single line."""
'''
        msg = Message(msg_id='invalid-docstring-quote', line=5, args=(TRI_Q_DOUB, TRI_Q_SING))

        self.check_class(test_str, msg)

    @set_config(docstring_quote='double')
    def test_single_line_double_quote_docstring_with_cfg_double_multiple_cls(self):

        test_str = '''
class TestClass1(object):
    """Class docstring"""

class TestClass2(object):  #@
    """Class level docstring on a single line."""

class TestClass3(object):
    """Another class level docstring on single line."""
'''

        self.check_class(test_str)

    @set_config(docstring_quote='single')
    def test_single_line_double_quote_docstring_with_cfg_single_multiple_cls(self):

        test_str = '''
class TestClass1(object):
    """Class docstring"""

class TestClass2(object):  #@
    """Class level docstring on a single line."""

class TestClass3(object):
    """Another class level docstring on single line."""
'''
        msg = Message(msg_id='invalid-docstring-quote', line=6, args=(TRI_Q_DOUB, TRI_Q_SING))

        self.check_class(test_str, msg)

    @set_config(docstring_quote='double')
    def test_multi_line_double_quote_docstring_with_cfg_double(self):

        test_str = '''
class TestClass(object):  #@
    """Class level docstring
    on multiple lines.
    """
'''

        self.check_class(test_str)

    @set_config(docstring_quote='single')
    def test_multi_line_double_quote_docstring_with_cfg_single(self):

        test_str = '''
class TestClass(object):  #@
    """Class level docstring
    on multiple lines.
    """
'''
        msg = Message(msg_id='invalid-docstring-quote', line=3, args=(TRI_Q_DOUB, TRI_Q_SING))

        self.check_class(test_str, msg)

    @set_config(docstring_quote='double')
    def test_multi_line_single_quote_docstring_with_cfg_double(self):

        test_str = """
class TestClass(object):  #@
    '''Class level docstring
    on multiple lines.
    '''
"""
        msg = Message(msg_id='invalid-docstring-quote', line=3, args=(TRI_Q_SING, TRI_Q_DOUB))

        self.check_class(test_str, msg)

    @set_config(docstring_quote='single')
    def test_multi_line_single_quote_docstring_with_cfg_single(self):

        test_str = """
class TestClass(object):  #@
    '''Class level docstring
    on multiple lines.
    '''
"""

        self.check_class(test_str)

    @set_config(docstring_quote='double')
    def test_multi_line_double_quote_docstring_with_cfg_double_multi_row_cls(self):

        test_str = '''
class TestClass(  #@
    object
):
    """Class level docstring
    on multiple lines.
    """
'''

        self.check_class(test_str)

    @set_config(docstring_quote='single')
    def test_multi_line_double_quote_docstring_with_cfg_single_multi_row_cls(self):

        test_str = '''
class TestClass(  #@
    object
):
    """Class level docstring
    on multiple lines.
    """
'''
        msg = Message(msg_id='invalid-docstring-quote', line=5, args=(TRI_Q_DOUB, TRI_Q_SING))

        self.check_class(test_str, msg)

    @set_config(docstring_quote='double')
    def test_multi_line_double_quote_docstring_with_cfg_double_multiple_cls(self):

        test_str = '''
class TestClass1(object):
    """Class docstring
    on multiple lines.
    """

class TestClass2(object):  #@
    """Class level docstring
    on multiple lines.
    """

class TestClass3(object):
    """Another class level docstring
    on multiple lines.
    """
'''

        self.check_class(test_str)

    @set_config(docstring_quote='single')
    def test_multi_line_double_quote_docstring_with_cfg_single_multiple_cls(self):

        test_str = '''
class TestClass1(object):
    """Class docstring
    on multiple lines.
    """

class TestClass2(object):  #@
    """Class level docstring
    on multiple lines.
    """

class TestClass3(object):
    """Another class level docstring
    on multiple lines.
    """
'''
        msg = Message(msg_id='invalid-docstring-quote', line=8, args=(TRI_Q_DOUB, TRI_Q_SING))

        self.check_class(test_str, msg)

    @set_config(docstring_quote='double')
    def test_single_line_double_quote_docstring_with_cfg_double_cls_contents_01(self):

        test_str = '''
class TestClass(object):  #@
    """Class level docstring on a single line."""

    member = 44

    def __init__(self):
        pass
'''

        self.check_class(test_str)

    @set_config(docstring_quote='single')
    def test_single_line_double_quote_docstring_with_cfg_single_cls_contents_01(self):

        test_str = '''
class TestClass(object):  #@
    """Class level docstring on a single line."""

    member = 44

    def __init__(self):
        pass
'''
        msg = Message(msg_id='invalid-docstring-quote', line=3, args=(TRI_Q_DOUB, TRI_Q_SING))

        self.check_class(test_str, msg)

    @set_config(docstring_quote='double')
    def test_single_line_double_quote_docstring_with_cfg_double_cls_contents_02(self):

        test_str = '''
class TestClass(object):  #@
    """Class level docstring on a single line."""

    # this is a class member
    member = {1:2, 3:4}

    def __init__(self, x):
        """Constructor
        """
        self.x = x

    def get_x():
        """Gets the x member"""
        return self.x
'''

        self.check_class(test_str)

    @set_config(docstring_quote='single')
    def test_single_line_double_quote_docstring_with_cfg_single_cls_contents_02(self):

        test_str = '''
class TestClass(object):  #@
    """Class level docstring on a single line."""

    # this is a class member
    member = {1:2, 3:4}

    def __init__(self, x):
        """Constructor
        """
        self.x = x

    def get_x():
        """Gets the x member"""
        return self.x
'''
        msg = Message(msg_id='invalid-docstring-quote', line=3, args=(TRI_Q_DOUB, TRI_Q_SING))

        self.check_class(test_str, msg)
