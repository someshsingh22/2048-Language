class InvalidCharacter(Exception):
    """
    Raised when a foreign character is passed to the lexer
    parameter:

    index: index at which invalid character was found
    character: the invalid character that was found
    """

    def __init__(self, index, character):
        self.message = "Invalid Character %c found at index %d" % (character, index)
        super().__init__(self.message)


class WrongCharacter(Exception):
    """
    Raised when a ? character is passed to the lexer in a wrong place
    parameter:

    index: index at which invalid character was found
    character: the invalid character that was found
    """

    def __init__(self, index):
        self.message = "? referenced at index %d" % (index)
        super().__init__(self.message)


class EndNotFound(Exception):
    """
    Raised when a full stop is not present.
    parameter:
    """

    def __init__(self):
        self.message = "Full Stop required to terminate the command"
        super().__init__(self.message)


class FalseTermination(Exception):
    """
    Raised when a full stop is present in between
    parameter:
    """

    def __init__(self, index):
        self.message = "Non terminating Full Stop present at index %d" % index
        super().__init__(self.message)


class InvalidIdentifier(Exception):
    """
    Raised when an invalid identifier is passed to the lexer
    parameter:

    index: index at which invalid character was found
    identifier: the invalid identifier that was found
    """

    def __init__(self, index, identifier):
        self.message = "Invalid identifier %s found at index %d" % (identifier, index)
        super().__init__(self.message)


class ReservedIdentifier(Exception):
    """
    Raised when an reserved identifier is passed to the lexer
    parameter:

    index: index at which reserved character was found
    identifier: the reserved identifier that was found
    """

    def __init__(self, index, identifier):
        self.message = "Reserved identifier %s found at index %d" % (identifier, index)
        super().__init__(self.message)


class InvalidAsssign(Exception):
    """
    Raised when a Invalid assignment value is passed to the parser
    parameter:

    index: index at which Invalid value was found
    value: the Invalid value that was found
    """

    def __init__(self, index, value):
        self.message = "Invalid value %s found at index %d" % (value, index)
        super().__init__(self.message)


class InvalidIndex(Exception):
    """
    Raised when a Invalid index is passed to the parser
    parameter:

    index: index at which Invalid index was found
    value: the Invalid index that was found
    """

    def __init__(self, index, index_value):
        self.message = "Invalid index %s found at index %d" % (index_value, index)
        super().__init__(self.message)


class WrongIndex(Exception):
    """
    Raised when an out of bound index is passed on runtime
    parameter:

    index: index at which wrong index was found
    value: the Invalid index that was found
    range: permissible range
    """

    def __init__(self, index, index_value, irange):
        self.message = "Invalid index %s found at index %d, index can vary from %s" % (
            index_value,
            index,
            irange,
        )
        super().__init__(self.message)


class ImbalancedParanthesis(Exception):
    """
    Raised when a imbalanced paranthesis is passed to the parser
    parameter:

    index: index at which imbalanced paranthesis was found
    value: the imbalanced paranthesis that was found
    """

    def __init__(self, index, imbalance):
        self.message = "imbalanced paranthesis %s found starting at index %d" % (imbalance, index)
        super().__init__(self.message)
