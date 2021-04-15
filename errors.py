class SyntaxException(Exception):
    """
    Parent Exception for Syntax Errors
    """

    def __init__(self, error):
        self.message = "Syntax Error: "
        super().__init__(self.message + error)


class RuntimeException(Exception):
    """
    Parent Exception for Runtime Errors
    """

    def __init__(self, error):
        self.message = "Runtime Error: "
        super().__init__(self.message + error)


class ForeignCharacter(SyntaxException):
    """
    Raised when a foreign character is passed to the lexer
    parameter:

    index: index at which invalid character was found
    character: the invalid character that was found
    """

    def __init__(self, index, character):

        self.message = "Foreign Character %c found at index %d" % (character, index)
        super().__init__(self.message)


class WrongCharacter(SyntaxException):
    """
    Raised when a , or ? character is passed to the lexer in a wrong place
    parameter:

    index: index at which invalid character was found
    character: the invalid character that was found
    """

    def __init__(self, character, index):

        self.message = "%c wrongly referenced at index %d" % (character, index)
        super().__init__(self.message)


class FullStopNotFound(SyntaxException):
    """
    Raised when a full stop is not present.
    parameter:
    """

    def __init__(self):

        self.message = "Full Stop required to terminate the command"
        super().__init__(self.message)


class FalseTermination(SyntaxException):
    """
    Raised when a full stop is present in between
    parameter:
    """

    def __init__(self, index):

        self.message = "Non terminating Full Stop present at index %d" % index
        super().__init__(self.message)


class InvalidIdentifier(SyntaxException):
    """
    Raised when an invalid identifier is passed to the lexer
    parameter:

    index: index at which invalid character was found
    identifier: the invalid identifier that was found
    """

    def __init__(self, index, identifier):

        self.message = "Invalid identifier %s found at index %d" % (identifier, index)
        super().__init__(self.message)


class ReservedIdentifier(SyntaxException):
    """
    Raised when an reserved identifier is passed to the lexer
    parameter:

    index: index at which reserved character was found
    identifier: the reserved identifier that was found
    """

    def __init__(self, index, identifier):

        self.message = "Reserved identifier %s found at index %d" % (identifier, index)
        super().__init__(self.message)


class InvalidAsssign(SyntaxException):
    """
    Raised when a Invalid assignment value is passed to the parser
    parameter:

    index: index at which Invalid value was found
    value: the Invalid value that was found
    """

    def __init__(self, index, value):

        self.message = "Invalid value %s found at index %d" % (value, index)
        super().__init__(self.message)


class InvalidIndex(SyntaxException):
    """
    Raised when a Invalid index is passed to the parser
    parameter:

    index: index at which Invalid index was found
    value: the Invalid index that was found
    """

    def __init__(self, index, index_value):

        self.message = "Invalid index %s found at index %d" % (index_value, index)
        super().__init__(self.message)


class WrongIndex(RuntimeException):
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
