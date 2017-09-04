"""Tests for the string quote checker for module-level docstrings.
"""

from pylint_quotes.checker import StringQuoteChecker
from pylint.testutils import Message, set_config

from utils import TRI_Q_DOUB, TRI_Q_SING, StringQuiteCheckerTestCase


class TestModuleStringQuoteChecker(StringQuiteCheckerTestCase):
    """ Test case for module-level docstrings.
    """
    CHECKER_CLASS = StringQuoteChecker

    @set_config(docstring_quote='double')
    def test_single_line_double_quote_docstring_with_cfg_double(self):

        test_str = '''"""This is a top level docstring"""'''

        self.check_module(test_str)

    @set_config(docstring_quote='single')
    def test_single_line_double_quote_docstring_with_cfg_single(self):

        test_str = '''"""This is a top level docstring"""'''
        msg = Message(msg_id='invalid-docstring-quote', line=1, args=(TRI_Q_DOUB, TRI_Q_SING))

        self.check_module(test_str, msg)

    @set_config(docstring_quote='double')
    def test_single_line_single_quote_docstring_with_cfg_double(self):

        test_str = """'''This is a top level docstring'''"""
        msg = Message(msg_id='invalid-docstring-quote', line=1, args=(TRI_Q_SING, TRI_Q_DOUB))

        self.check_module(test_str, msg)

    @set_config(docstring_quote='single')
    def test_single_line_single_quote_docstring_with_cfg_single(self):

        test_str = """'''This is a top level docstring'''"""

        self.check_module(test_str)

    @set_config(docstring_quote='double')
    def test_multi_line_double_quote_docstring_with_cfg_double(self):

        test_str = '''"""Top level docstring

        With an additional line.
        And another additional line.
        """'''

        self.check_module(test_str)

    @set_config(docstring_quote='single')
    def test_multi_line_double_quote_docstring_with_cfg_single(self):

        test_str = '''"""Top level docstring

        With an additional line.
        And another additional line.
        """'''
        msg = Message(msg_id='invalid-docstring-quote', line=1, args=(TRI_Q_DOUB, TRI_Q_SING))

        self.check_module(test_str, msg)

    @set_config(docstring_quote='double')
    def test_multi_line_single_quote_docstring_with_cfg_double(self):

        test_str = """'''Top level docstring

        With an additional line.
        And another additional line.
        '''"""
        msg = Message(msg_id='invalid-docstring-quote', line=1, args=(TRI_Q_SING, TRI_Q_DOUB))

        self.check_module(test_str, msg)

    @set_config(docstring_quote='single')
    def test_multi_line_single_quote_docstring_with_cfg_single(self):

        test_str = """'''Top level docstring

        With an additional line.
        And another additional line.
        '''"""

        self.check_module(test_str)

    @set_config(docstring_quote='double')
    def test_docstring_with_shebang_cfg_double(self):

        test_str = '''#!/usr/bin/env python
""" This is a top level docstring.

It describes the module.
"""
        '''

        self.check_module(test_str)

    @set_config(docstring_quote='single')
    def test_docstring_with_shebang_cfg_single(self):

        test_str = '''#!/usr/bin/env python
""" This is a top level docstring.

It describes the module.
"""
        '''
        msg = Message(msg_id='invalid-docstring-quote', line=2, args=(TRI_Q_DOUB, TRI_Q_SING))

        self.check_module(test_str, msg)

    @set_config(docstring_quote='double')
    def test_docstring_with_file_contents_01_cfg_double(self):

        test_str = '''#!/usr/bin/env python
""" This is a top level docstring.

It describes the module.
"""

import os

x = 2 * 2
        '''

        self.check_module(test_str)

    @set_config(docstring_quote='single')
    def test_docstring_with_file_contents_01_cfg_single(self):

        test_str = '''#!/usr/bin/env python
""" This is a top level docstring.

It describes the module.
"""

import os

x = 2 * 2
        '''
        msg = Message(msg_id='invalid-docstring-quote', line=2, args=(TRI_Q_DOUB, TRI_Q_SING))

        self.check_module(test_str, msg)

    @set_config(docstring_quote='double')
    def test_docstring_with_file_contents_02_cfg_double(self):

        test_str = '''#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" This is a top level docstring.

It describes the module.
"""

def x():
    print(2 * 2)

x()
        '''

        self.check_module(test_str)

    @set_config(docstring_quote='single')
    def test_docstring_with_file_contents_02_cfg_single(self):

        test_str = '''#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" This is a top level docstring.

It describes the module.
"""

def x():
    print(2 * 2)

x()
        '''
        msg = Message(msg_id='invalid-docstring-quote', line=3, args=(TRI_Q_DOUB, TRI_Q_SING))

        self.check_module(test_str, msg)
