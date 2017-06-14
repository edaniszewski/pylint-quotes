"""Pylint plugin for checking quote type on strings.
"""

from __future__ import absolute_import

import tokenize

from pylint.interfaces import ITokenChecker, IAstroidChecker
from pylint.checkers import BaseTokenChecker


CONFIG_OPTS = ('single', 'double')

QUOTES = ('\'', '"')

SINGLE_QUOTE_OPTS = dict(zip(CONFIG_OPTS, QUOTES))
TRIPLE_QUOTE_OPTS = dict(zip(CONFIG_OPTS, [q * 3 for q in QUOTES]))


class StringQuoteChecker(BaseTokenChecker):
    """Pylint checker for the consistent use of characters in strings.

    This checker will check for quote consistency among string literals,
    triple quoted strings, and docstrings. Each of those three can be
    configured individually to use either single quotes (') or double
    quotes (").
    """

    __implements__ = (ITokenChecker, IAstroidChecker, )

    name = 'string_quotes'

    msgs = {
        'C4001': (
            'Invalid string quote %s, should be %s',
            'invalid-string-quote',
            'Used when the string quote character does not match the '
            'value configured in the `string-quote` option.'
        ),
        'C4002': (
            'Invalid triple quote %s, should be %s',
            'invalid-triple-quote',
            'Used when the triple quote characters do not match the '
            'value configured in the `triple-quote` option.'
        ),
        'C4003': (
            'Invalid docstring quote %s, should be %s',
            'invalid-docstring-quote',
            'Used when the docstring quote characters do not match the '
            'value configured in the `docstring-quote` option.'
        )
    }

    options = (
        (
            'string-quote',
            dict(
                type='choice',
                metavar='<{0} or {1}>'.format(*CONFIG_OPTS),
                default=CONFIG_OPTS[0],
                choices=CONFIG_OPTS,
                help='The quote character for string literals.'
            )
        ),
        (
            'triple-quote',
            dict(
                type='choice',
                metavar='<{0} or {1}>'.format(*CONFIG_OPTS),
                default=CONFIG_OPTS[0],
                choices=CONFIG_OPTS,
                help='The quote character for triple-quoted strings (non-docstring).'
            )
        ),
        (
            'docstring-quote',
            dict(
                type='choice',
                metavar='<{0} or {1}>'.format(*CONFIG_OPTS),
                default=CONFIG_OPTS[1],
                choices=CONFIG_OPTS,
                help='The quote character for triple-quoted docstrings.'
            )
        )
    )

    # we need to check quote usage via tokenization, as the AST walk will
    # only tell us what the doc is, but not how it is quoted. we need to
    # store any triple quotes found during tokenization and check against
    # these when performing the walk. if a triple-quote string matches to
    # a node's docstring, it is checked and removed from this collection.
    # once we leave the module, any remaining triple quotes in this collection
    # are checked as regular triple quote strings.
    _tokenized_triple_quotes = {}

    def visit_module(self, node):
        """Visit module and check for docstring quote consistency.

        Args:
            node: the module node being visited.
        """
        self._process_for_docstring(node, 'module')

    # pylint: disable=unused-argument
    def leave_module(self, node):
        """Leave module and check remaining triple quotes.

        Args:
            node: the module node we are leaving.
        """
        for triple_quote in self._tokenized_triple_quotes.values():
            self._check_triple_quotes(triple_quote)

        # after we are done checking these, clear out the triple-quote
        # tracking collection so nothing is left over for the next module.
        self._tokenized_triple_quotes = {}

    def visit_classdef(self, node):
        """Visit class and check for docstring quote consistency.

        Args:
            node: the class node being visited.
        """
        self._process_for_docstring(node, 'class')

    def visit_functiondef(self, node):
        """Visit function and check for docstring quote consistency.

        Args:
            node: the function node being visited.
        """
        self._process_for_docstring(node, 'function')

    def _process_for_docstring(self, node, node_type):
        """Check for docstring quote consistency.

        Args:
            node: the AST node being visited.
            node_type: the type of node being operated on.
        """
        # if there is no docstring, don't need to do anything.
        if node.doc is not None:

            # the module is everything, so to find the docstring, we
            # iterate line by line from the start until the first element
            # to find the docstring, as it cannot appear after the first
            # element in the body.
            if node_type == 'module':
                for i in range(0, node.body[0].lineno):
                    quote_record = self._tokenized_triple_quotes.get(i)
                    if quote_record:
                        self._check_docstring_quotes(quote_record)
                        del self._tokenized_triple_quotes[i]
                        break

            else:
                # the node has a docstring so we check the tokenized triple
                # quotes to find a matching docstring token that follows the
                # function/class definition.
                doc_row = node.blockstart_tolineno + 1
                quote_record = self._tokenized_triple_quotes[doc_row]
                self._check_docstring_quotes(quote_record)
                del self._tokenized_triple_quotes[doc_row]

    def process_tokens(self, tokens):
        """Process the token stream.

        This is required to override the parent class' implementation.

        Args:
            tokens: the tokens from the token stream to process.
        """
        for tok_type, token, (start_row, _), _, _ in tokens:
            if tok_type == tokenize.STRING:
                # 'token' is the whole un-parsed token; we can look at the start
                # of it to see whether it's a raw or unicode string etc.
                self._process_string_token(token, start_row)

    def _process_string_token(self, token, start_row):
        """Internal method for identifying and checking string tokens
        from the token stream.

        Args:
            token: the token to check.
            start_row: the line on which the token was found.
        """
        for i, char in enumerate(token):
            if char in QUOTES:
                break

        # pylint: disable=undefined-loop-variable
        # ignore prefix markers like u, b, r
        norm_quote = token[i:]

        # triple-quote strings
        if len(norm_quote) >= 3 and norm_quote[:3] in TRIPLE_QUOTE_OPTS.values():
            self._tokenized_triple_quotes[start_row] = (token, norm_quote[:3], start_row)

        # single quote strings
        elif norm_quote[0] != SINGLE_QUOTE_OPTS.get(self.config.string_quote):
            self._invalid_string_quote(norm_quote[0], start_row)

    def _check_triple_quotes(self, quote_record):
        """Check if the triple quote from tokenization is valid.

        Args:
            quote_record: a tuple containing the info about the string
                from tokenization, giving the (token, quote, row number).
        """
        _, triple, row = quote_record
        if triple != TRIPLE_QUOTE_OPTS.get(self.config.triple_quote):
            self._invalid_triple_quote(triple, row)

    def _check_docstring_quotes(self, quote_record):
        """Check if the docstring quote from tokenization is valid.

        Args:
            quote_record: a tuple containing the info about the string
                from tokenization, giving the (token, quote, row number).
        """
        _, triple, row = quote_record
        if triple != TRIPLE_QUOTE_OPTS.get(self.config.docstring_quote):
            self._invalid_docstring_quote(triple, row)

    def _invalid_string_quote(self, quote, row):
        """Add a message for an invalid string literal quote.

        Args:
            quote: The quote characters that were found.
            row: The row number the quote character was found on.
        """
        self.add_message(
            'invalid-string-quote',
            line=row,
            args=(quote, SINGLE_QUOTE_OPTS.get(self.config.string_quote))
        )

    def _invalid_triple_quote(self, quote, row):
        """Add a message for an invalid triple quote.

        Args:
            quote: The quote characters that were found.
            row: The row number the quote characters were found on.
        """
        self.add_message(
            'invalid-triple-quote',
            line=row,
            args=(quote, TRIPLE_QUOTE_OPTS.get(self.config.triple_quote))
        )

    def _invalid_docstring_quote(self, quote, row):
        """Add a message for an invalid docstring quote.

        Args:
            quote: The quote characters that were found.
            row: The row number the quote characters were found on.
        """
        self.add_message(
            'invalid-docstring-quote',
            line=row,
            args=(quote, TRIPLE_QUOTE_OPTS.get(self.config.docstring_quote))
        )
