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

    def __init__(self, value):

        self.message = "Invalid value %d found at index" % value
        super().__init__(self.message)


class WrongIndex(RuntimeException):
    """
    Raised when an out of bound index is passed on runtime
    parameter:

    index: index at which wrong index was found
    value: the Invalid index that was found
    range: permissible range
    """

    def __init__(self, index, lindex, uindex):

        self.message = "Wrong index %s found, index can vary from %s to %s" % (
            str(index),
            str(lindex),
            str(uindex),
        )
        super().__init__(self.message)


class ParserException(SyntaxException):
    """
    Raised when an error is raised during parsing:

    token: token at which the parser found the error
    """

    def __init__(self, token):

        self.message = "Invalid token %s found" % token.type
        super().__init__(self.message)


class IdentifierExists(RuntimeException):
    """
    Raised when assigning a name which already exists

    varName: name of the variable
    """

    def __init__(self, varName):
        self.message = "A variable with name %s already exists" % varName
        super().__init__(self.message)


class EmptyTileNamingException(RuntimeException):
    """
    Raised when assigning a name to an empty tile
    """

    def __init__(self, index):
        self.message = "Empty Tile at %d,%d cannot be named" % index
        super().__init__(self.message)


class EmptyTileQueryException(RuntimeException):
    """
    Raised when assigning a name to an empty tile
    """

    def __init__(self, index):
        self.message = "Empty Tile at %d,%d cannot be queried" % index
        super().__init__(self.message)
