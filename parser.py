from sly import Parser
from lexer import Lexer2048
from errors import ParserException


class Parser2048(Parser):
    tokens = Lexer2048.tokens

    def error(self, token):
        """
        Error Handling for parse-syntax errors
        """
        if token:
            print(f"sly: Syntax error, token={token.type}")
            raise ParserException(token)
        else:
            print(("sly: Parse error in input. EOF\n"))
            raise ParserException(token)

    def __init__(self, fmap=None):
        self.fmap = fmap

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
        self.fmap["ASSIGN"](value=p.expr0, index=(p.expr1, p.expr2))

    @_("VALUE IN expr COMMA expr")
    def expr(self, p):
        value = self.fmap["QUERY"](index=(p.expr0, p.expr1))
        return value

    @_("OPERATION DIRECTION")
    def statement(self, p):
        self.fmap["MOVE"](direction=p.DIRECTION, operation=p.OPERATION)
