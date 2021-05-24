"""Tests for the string quote checker for "smart quotes" which operate
differently than normal mode by permitting quote types which might
otherwise fail if they are wrapping around other quotes, thus preventing
the need to string escape.
"""

from pylint_quotes.checker import StringQuoteChecker
from pylint.testutils import Message, set_config

from pylint.testutils import _tokenize_str as tokenize_str

from utils import Q_DOUB, Q_SING, TRI_Q_SING, TRI_Q_DOUB, StringQuoteCheckerTestCase


class TestSmartStringQuoteChecker(StringQuoteCheckerTestCase):
    """ Test case for smart escaping string literals.
    """
    CHECKER_CLASS = StringQuoteChecker

    @set_config(string_quote='double-avoid-escape')
    def test_double_quote_string_literal_cfg_double_escaped(self):

        test_str = '''x = "this is a \\"test\\" string"'''

        msg = Message(msg_id='invalid-string-quote', line=1, args=(Q_DOUB, Q_SING))
        with self.assertAddsMessages(msg):
            self.checker.process_tokens(tokenize_str(test_str))

    @set_config(string_quote='single-avoid-escape')
    def test_double_quote_string_literal_cfg_single_escaped(self):

        test_str = '''x = "this is a \\"test\\" string"'''

        msg = Message(msg_id='invalid-string-quote', line=1, args=(Q_DOUB, Q_SING))
        with self.assertAddsMessages(msg):
            self.checker.process_tokens(tokenize_str(test_str))

    @set_config(string_quote='double-avoid-escape')
    def test_single_quote_string_literal_cfg_double_escaped(self):

        test_str = """x = 'this is a \\'test\\' string'"""

        msg = Message(msg_id='invalid-string-quote', line=1, args=(Q_SING, Q_DOUB))
        with self.assertAddsMessages(msg):
            self.checker.process_tokens(tokenize_str(test_str))

    @set_config(string_quote='single-avoid-escape')
    def test_single_quote_string_literal_cfg_single_escaped(self):

        test_str = """x = 'this is a \\'test\\' string'"""

        msg = Message(msg_id='invalid-string-quote', line=1, args=(Q_SING, Q_DOUB))
        with self.assertAddsMessages(msg):
            self.checker.process_tokens(tokenize_str(test_str))

    @set_config(string_quote='double-avoid-escape')
    def test_double_quote_string_literal_cfg_double_non_escaped(self):

        test_str = '''x = "this is a 'test' string"'''

        with self.assertNoMessages():
            self.checker.process_tokens(tokenize_str(test_str))

    @set_config(string_quote='single-avoid-escape')
    def test_double_quote_string_literal_cfg_single_non_escaped(self):

        test_str = '''x = "this is a 'test' string"'''

        with self.assertNoMessages():
            self.checker.process_tokens(tokenize_str(test_str))

    @set_config(string_quote='double-avoid-escape')
    def test_single_quote_string_literal_cfg_double_non_escaped(self):

        test_str = """x = 'this is a "test" string'"""

        with self.assertNoMessages():
            self.checker.process_tokens(tokenize_str(test_str))

    @set_config(string_quote='single-avoid-escape')
    def test_single_quote_string_literal_cfg_single_non_escaped(self):

        test_str = """x = 'this is a "test" string'"""

        with self.assertNoMessages():
            self.checker.process_tokens(tokenize_str(test_str))
