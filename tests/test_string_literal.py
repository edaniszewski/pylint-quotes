"""Tests for the string quote checker for string literals.
"""

from pylint_quotes.checker import StringQuoteChecker
from pylint.testutils import Message, set_config, tokenize_str

from utils import Q_DOUB, Q_SING, TRI_Q_SING, TRI_Q_DOUB, StringQuiteCheckerTestCase


class TestStringLiteralStringQuoteChecker(StringQuiteCheckerTestCase):
    """ Test case for string literals.
    """
    CHECKER_CLASS = StringQuoteChecker

    @set_config(string_quote='double')
    def test_double_quote_string_literal_cfg_double(self):

        test_str = '''x = "test"'''

        with self.assertNoMessages():
            self.checker.process_tokens(tokenize_str(test_str))

    @set_config(string_quote='single')
    def test_double_quote_string_literal_cfg_single(self):

        test_str = '''x = "test"'''

        msg = Message(msg_id='invalid-string-quote', line=1, args=(Q_DOUB, Q_SING))
        with self.assertAddsMessages(msg):
            self.checker.process_tokens(tokenize_str(test_str))

    @set_config(string_quote='double')
    def test_single_quote_string_literal_cfg_double(self):

        test_str = """x = 'test'"""

        msg = Message(msg_id='invalid-string-quote', line=1, args=(Q_SING, Q_DOUB))
        with self.assertAddsMessages(msg):
            self.checker.process_tokens(tokenize_str(test_str))

    @set_config(string_quote='single')
    def test_single_quote_string_literal_cfg_single(self):

        test_str = """x = 'test'"""

        with self.assertNoMessages():
            self.checker.process_tokens(tokenize_str(test_str))

    @set_config(string_quote='double')
    def test_mixed_quote_string_literal_cfg_double(self):

        test_str = '''x = "test" + 'test' + "test"'''

        msg = Message(msg_id='invalid-string-quote', line=1, args=(Q_SING, Q_DOUB))
        with self.assertAddsMessages(msg):
            self.checker.process_tokens(tokenize_str(test_str))

    @set_config(string_quote='single')
    def test_mixed_quote_string_literal_cfg_single(self):

        test_str = '''x = "test" + 'test' + "test"'''

        msg1 = Message(msg_id='invalid-string-quote', line=1, args=(Q_DOUB, Q_SING))
        msg2 = Message(msg_id='invalid-string-quote', line=1, args=(Q_DOUB, Q_SING))
        with self.assertAddsMessages(msg1, msg2):
            self.checker.process_tokens(tokenize_str(test_str))

    @set_config(string_quote='double')
    def test_double_quote_string_literal_cfg_double_with_escaping(self):

        test_str = '''x = "this is a \\"test\\" string"'''

        with self.assertNoMessages():
            self.checker.process_tokens(tokenize_str(test_str))

    @set_config(string_quote='single')
    def test_double_quote_string_literal_cfg_single_with_escaping(self):

        test_str = '''x = "this is a \\"test\\" string"'''

        msg = Message(msg_id='invalid-string-quote', line=1, args=(Q_DOUB, Q_SING))
        with self.assertAddsMessages(msg):
            self.checker.process_tokens(tokenize_str(test_str))

    @set_config(string_quote='double')
    def test_single_quote_string_literal_cfg_double_with_escaping(self):

        test_str = """x = 'this is a \\'test\\' string'"""

        msg = Message(msg_id='invalid-string-quote', line=1, args=(Q_SING, Q_DOUB))
        with self.assertAddsMessages(msg):
            self.checker.process_tokens(tokenize_str(test_str))

    @set_config(string_quote='single')
    def test_single_quote_string_literal_cfg_single_with_escaping(self):

        test_str = """x = 'this is a \\'test\\' string'"""

        with self.assertNoMessages():
            self.checker.process_tokens(tokenize_str(test_str))

    @set_config(triple_quote='double')
    def test_double_tri_quote_string_literal_cfg_double(self):

        test_str = '''x = """test"""'''

        with self.assertNoMessages():
            self.checker.process_tokens(tokenize_str(test_str))
            self.checker.leave_module(None)

    @set_config(triple_quote='single')
    def test_double_tri_quote_string_literal_cfg_single(self):

        test_str = '''x = """test"""'''

        msg = Message(msg_id='invalid-triple-quote', line=1, args=(TRI_Q_DOUB, TRI_Q_SING))
        with self.assertAddsMessages(msg):
            self.checker.process_tokens(tokenize_str(test_str))
            self.checker.leave_module(None)

    @set_config(triple_quote='double')
    def test_single_tri_quote_string_literal_cfg_double(self):

        test_str = """x = '''test'''"""

        msg = Message(msg_id='invalid-triple-quote', line=1, args=(TRI_Q_SING, TRI_Q_DOUB))
        with self.assertAddsMessages(msg):
            self.checker.process_tokens(tokenize_str(test_str))
            self.checker.leave_module(None)

    @set_config(triple_quote='single')
    def test_single_tri_quote_string_literal_cfg_single(self):

        test_str = """x = '''test'''"""

        with self.assertNoMessages():
            self.checker.process_tokens(tokenize_str(test_str))
            self.checker.leave_module(None)

    @set_config(triple_quote='double')
    def test_multi_line_double_tri_quote_string_literal_cfg_double(self):

        test_str = '''x = """
        this is a
        multi-line
        test string
        """'''

        with self.assertNoMessages():
            self.checker.process_tokens(tokenize_str(test_str))
            self.checker.leave_module(None)

    @set_config(triple_quote='single')
    def test_multi_line_double_tri_quote_string_literal_cfg_single(self):

        test_str = '''x = """
        this is a
        multi-line
        test string
        """'''

        msg = Message(msg_id='invalid-triple-quote', line=1, args=(TRI_Q_DOUB, TRI_Q_SING))
        with self.assertAddsMessages(msg):
            self.checker.process_tokens(tokenize_str(test_str))
            self.checker.leave_module(None)
