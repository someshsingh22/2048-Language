class SyntaxException(Exception):
    """
    Parent Exception for Syntax Errors
    """

    def __init__(self, error):

        self.message = "\033[31m" + "Syntax Error: " + "\033[0m"
        super().__init__(self.message + error)


class RuntimeException(Exception):
    """
    Parent Exception for Runtime Errors
    """

    def __init__(self, error):
        self.message = "\033[31m" + "Runtime Error: " + "\033[0m"
        super().__init__(self.message + error)


class ForeignCharacter(SyntaxException):
    """
    Raised when a foreign character is passed to the lexer
    parameter:

    index: index at which invalid character was found
    character: the invalid character that was found
    """

    def __init__(self, index, character):

        self.message = (
            "Foreign Character \033[33m %c \033[0m found at index \033[33m %d \033[0m"
            % (character, index)
        )
        super().__init__(self.message)


class WrongCharacter(SyntaxException):
    """
    Raised when a , or ? character is passed to the lexer in a wrong place
    parameter:

    index: index at which invalid character was found
    character: the invalid character that was found
    """

    def __init__(self, character, index):

        self.message = (
            "\033[33m %c \033[0m wrongly referenced at index \033[33m %d \033[0m"
            % (character, index)
        )
        super().__init__(self.message)


class FullStopNotFound(SyntaxException):
    """
    Raised when a full stop is not present.
    parameter:
    """

    def __init__(self):

        self.message = "All commands must terminate with full stops '.'"
        super().__init__(self.message)


class FalseTermination(SyntaxException):
    """
    Raised when a full stop is present in between
    parameter:
    """

    def __init__(self, index):

        self.message = (
            "Non terminating Full Stop present at index \033[33m %d \033[0m" % index
        )
        super().__init__(self.message)


class ReservedIdentifier(SyntaxException):
    """
    Raised when an reserved identifier is passed to the lexer
    parameter:

    index: index at which reserved character was found
    identifier: the reserved identifier that was found
    """

    def __init__(self, identifier):

        self.message = (
            "\033[33m %s \033[0m cannot be used for naming, it is a reserved keyword"
            % identifier
        )
        super().__init__(self.message)


class IdentifierExists(RuntimeException):
    """
    Raised when assigning a name which already exists

    varName: name of the variable
    """

    def __init__(self, varName):
        self.message = (
            "A variable with name \033[33m %s \033[0m already exists" % varName
        )
        super().__init__(self.message)


class InvalidAsssign(SyntaxException):
    """
    Raised when a Invalid assignment value is passed to the parser
    parameter:

    index: index at which Invalid value was found
    value: the Invalid value that was found
    """

    def __init__(self, value):

        self.message = (
            "Invalid value \033[33m %d \033[0m negative values cannot be assigned"
            % value
        )
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

        self.message = (
            "Wrong index \033[33m %s \033[0m found, index can vary from \033[33m %s \033[0m to \033[33m %s \033[0m"
            % (str(index), str(lindex), str(uindex),)
        )
        super().__init__(self.message)


class ParserException(SyntaxException):
    """
    Raised when an error is raised during parsing:

    token: token at which the parser found the error
    """

    def __init__(self, token):

        self.message = "Invalid token \033[33m %s \033[0m found" % token.type
        super().__init__(self.message)


class EmptyTileNamingException(RuntimeException):
    """
    Raised when assigning a name to an empty tile
    """

    def __init__(self, index):
        self.message = (
            "Empty Tile at \033[33m %d \033[0m,\033[33m %d \033[0m cannot be named"
            % index
        )
        super().__init__(self.message)


class EmptyTileQueryException(RuntimeException):
    """
    Raised when assigning a name to an empty tile
    """

    def __init__(self, index):
        self.message = (
            "Empty Tile at \033[33m %d \033[0m,\033[33m %d \033[0m cannot be queried"
            % index
        )
        super().__init__(self.message)


class NamedParserException(SyntaxException):
    """
    Raised when an error is raised during parsing:

    token: token at which the parser found the error
    """

    def __init__(self, pre, post, correct):

        self.message = (
            "\033[33m %s \033[0m cannot be followed by \033[33m %s \033[0m, try \033[33m %s \033[0m"
            % (pre, post, correct)
        )
        super().__init__(self.message)
