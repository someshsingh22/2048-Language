from sly import Parser
from lexer import Lexer2048
from errors import (
    ParserException,
    InvalidAsssign,
    NamedParserException,
    ReservedIdentifier,
)


class Parser2048(Parser):
    """
    Parser2048 Class, Subclass of sly.parser Used to parse the string and map the grammar to suitable actions acc to the interpretation

    Grammar:
    expr: Expressions that Evaluate to numeric Values
    statement: Command Statements
    nonexpr: non expression keywords / identifiers
    nonindex: COMMA separated tokens which are not expressions
    """

    tokens = Lexer2048.tokens

    def __init__(self, fmap=None):
        self.fmap = fmap

    def error(self, token):
        """
        Error Handling for parse-syntax errors
        """
        if token:
            print(f"Syntax error : unexpected token {token.type} found")
            raise ParserException(token)
        else:
            print("Syntax error: Parse error in Command. Reached EOL")
            raise ParserException(token)

    @_("expr")
    def statement(self, p):
        return p.expr

    @_("NUMBER")
    def expr(self, p):
        return int(p.NUMBER)

    @_("VAR IDENTIFIER IS expr COMMA expr")
    def statement(self, p):
        self.fmap["NAME"](varName=p.IDENTIFIER, index=(p.expr0, p.expr1))

    @_("ASSIGN expr TO expr COMMA expr")
    def statement(self, p):
        if p.expr0 < 0:
            raise InvalidAsssign(p.expr0)
        self.fmap["ASSIGN"](value=p.expr0, index=(p.expr1, p.expr2))

    @_("VALUE IN expr COMMA expr")
    def expr(self, p):
        value = self.fmap["QUERY"](index=(p.expr0, p.expr1))
        return value

    @_("OPERATION DIRECTION")
    def statement(self, p):
        self.fmap["MOVE"](direction=p.DIRECTION, operation=p.OPERATION)

    @_(
        "VAR OPERATION IS expr COMMA expr",
        "VAR DIRECTION IS expr COMMA expr",
        "VAR ASSIGN IS expr COMMA expr",
        "VAR TO IS expr COMMA expr",
        "VAR VAR IS expr COMMA expr",
        "VAR IS IS expr COMMA expr",
        "VAR VALUE IS expr COMMA expr",
        "VAR IN IS expr COMMA expr",
    )
    def statement(self, p):
        raise ReservedIdentifier(p[1])

    @_("VAR expr IS expr COMMA expr")
    def statement(self, p):
        raise NamedParserException(p.VAR, "number", "Identifier")

    @_(
        "OPERATION",
        "DIRECTION",
        "ASSIGN",
        "TO",
        "VAR",
        "IS",
        "VALUE",
        "IN",
        "COMMA",
        "IDENTIFIER",
    )
    def nonexpr(self, p):
        return p[0]

    @_("nonexpr COMMA nonexpr", "nonexpr COMMA expr", "expr COMMA nonexpr")
    def nonindex(self, p):
        return (p[0], p[2])

    @_("VALUE IN nonindex")
    def statement(self, p):
        raise NamedParserException(
            "VALUE IN",
            "non numeric index (%s, %s)" % p.nonindex,
            "comma separated values",
        )

    @_("VAR IDENTIFIER IS nonindex")
    def statement(self, p):
        raise NamedParserException(
            "VAR IDENTIFIER IS",
            "non numeric index (%s, %s)" % p.nonindex,
            "comma separated values",
        )

    @_("ASSIGN nonexpr TO expr COMMA expr", "ASSIGN nonexpr TO nonindex")
    def statement(self, p):
        raise NamedParserException(
            "ASSIGN", "non numeric vale %s" % p[1], "numeric values",
        )

    @_("ASSIGN expr TO nonindex")
    def statement(self, p):
        raise NamedParserException(
            "ASSIGN NUMBER TO",
            "non numeric index (%s, %s)" % p.nonindex,
            "comma separated values",
        )

    @_(
        "ASSIGN expr OPERATION expr COMMA expr",
        "ASSIGN expr DIRECTION expr COMMA expr",
        "ASSIGN expr ASSIGN expr COMMA expr",
        "ASSIGN expr VAR expr COMMA expr",
        "ASSIGN expr IS expr COMMA expr",
        "ASSIGN expr VALUE expr COMMA expr",
        "ASSIGN expr IN expr COMMA expr",
        "ASSIGN expr COMMA expr COMMA expr",
        "ASSIGN expr IDENTIFIER expr COMMA expr",
    )
    def statement(self, p):
        raise NamedParserException(
            "Assign Value", p[2], "TO",
        )

    @_(
        "VAR IDENTIFIER OPERATION expr COMMA expr",
        "VAR IDENTIFIER DIRECTION expr COMMA expr",
        "VAR IDENTIFIER ASSIGN expr COMMA expr",
        "VAR IDENTIFIER TO expr COMMA expr",
        "VAR IDENTIFIER VAR expr COMMA expr",
        "VAR IDENTIFIER VALUE expr COMMA expr",
        "VAR IDENTIFIER IN expr COMMA expr",
        "VAR IDENTIFIER COMMA expr COMMA expr",
        "VAR IDENTIFIER IDENTIFIER expr COMMA expr",
    )
    def statement(self, p):
        raise NamedParserException(
            "VAR IDENTIFIER", p[2], "IS",
        )

    @_(
        "VALUE OPERATION expr COMMA expr",
        "VALUE DIRECTION expr COMMA expr",
        "VALUE ASSIGN expr COMMA expr",
        "VALUE TO expr COMMA expr",
        "VALUE VAR expr COMMA expr",
        "VALUE IS expr COMMA expr",
        "VALUE VALUE expr COMMA expr",
        "VALUE COMMA expr COMMA expr",
        "VALUE IDENTIFIER expr COMMA expr",
    )
    def statement(self, p):
        raise NamedParserException(
            "VAR IDENTIFIER", p[1], "IN",
        )

    @_(
        "OPERATION OPERATION",
        "OPERATION ASSIGN",
        "OPERATION TO",
        "OPERATION VAR",
        "OPERATION IS",
        "OPERATION VALUE",
        "OPERATION IN",
        "OPERATION COMMA",
        "OPERATION IDENTIFIER",
    )
    def statement(self, p):
        raise NamedParserException(
            "OPERATION", p[1], "UP/DOWN/LEFT/RIGHT",
        )

    @_(
        "DIRECTION DIRECTION",
        "ASSIGN DIRECTION",
        "TO DIRECTION",
        "VAR DIRECTION",
        "IS DIRECTION",
        "VALUE DIRECTION",
        "IN DIRECTION",
        "COMMA DIRECTION",
        "IDENTIFIER DIRECTION",
    )
    def statement(self, p):
        raise NamedParserException(
            "DIRECTION", p[1], "ADD/MULTIPLY/SUBTRACT/DIVIDE",
        )
