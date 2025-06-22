from pyparsing import (
    Word, alphas, alphanums, nums, Forward, Group, Dict,
    Suppress, QuotedString, delimitedList, oneOf, ZeroOrMore, Optional
)

class TidyMLParser:
    """
    A parser for TidyML syntax using pyparsing.
    Supports nested blocks, key-value pairs, primitive values, and lists.

    Example syntax:
    users = [
      user {
        name = "Gokul"
        age = 40
        admin = true
        skills = ["python", "c++", "leadership"]
      },
      user {
        name = "Kiran"
        age = 35
        admin = false
        skills = ["go", "java"]
      }
    ]
    """

    def __init__(self):
        """
        Initialize and define the grammar rules.
        """
        self._define_grammar()

    def _define_grammar(self):
        """
        Defines the pyparsing grammar for TidyML.
        """
        # Suppressed punctuation used to define structure
        LBRACE, RBRACE, EQ, LBRACK, RBRACK, COMMA = map(Suppress, "{}=[],")

        # Identifiers (keys): must start with a letter, followed by letters, digits, _ or -
        identifier = Word(alphas, alphanums + "_-")

        # Numbers: parsed as int or float based on presence of '.'
        number = Word(nums + ".-").setParseAction(
            lambda t: float(t[0]) if '.' in t[0] else int(t[0])
        )

        # Strings: double-quoted
        string = QuotedString('"')

        # Booleans: true/false mapped to Python bool
        boolean = oneOf("true false").setParseAction(
            lambda t: t[0] == "true"
        )

        # Forward declarations to allow recursive definitions
        value = Forward()
        block = Forward()
        list_item = Forward()

        # Value types:
        # - string, number, boolean
        # - block (e.g., user { ... })
        # - list (e.g., [1, "a", user { ... }])
        value <<= (
            string |
            number |
            boolean |
            Group(block) |
            Group(LBRACK + Optional(delimitedList(list_item)) + RBRACK)
        )

        # List items can be values or blocks
        list_item <<= value | Group(block)

        # A pair is a key = value
        pair = Group(identifier + EQ + value)

        # A block is like: user { name = "..." ... }
        block_body = Dict(ZeroOrMore(pair))
        block <<= Group(identifier + LBRACE + block_body + RBRACE)

        # Top-level assignments: key = value
        top_pair = Group(identifier + EQ + value)

        # A TidyML document consists of multiple top-level assignments
        self.document = Dict(ZeroOrMore(top_pair))

    def parse(self, text: str):
        """
        Parse TidyML text into a nested Python dictionary.

        Args:
            text (str): The input string in TidyML format.

        Returns:
            dict: Parsed output.
        """
        return self.document.parseString(text, parseAll=True).asDict()
