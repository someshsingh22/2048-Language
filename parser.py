from sly import Parser
from lexer import Lexer2048


class Parser2048(Parser):
    tokens = Lexer2048.tokens

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
        return (p.IDENTIFIER, p.expr0, p.expr1)

    @_("ASSIGN expr TO expr COMMA expr")
    def statement(self, p):
        return (p.expr0, p.expr1, p.expr2)

    @_("VALUE IN expr COMMA expr")
    def expr(self, p):
        return (p.expr0, p.expr1)

    @_("OPERATION DIRECTION")
    def statement(self, p):
        return (p.OPERATION, p.DIRECTION)

    @_("IDENTIFIER")
    def expr(self, p):
        return p.IDENTIFIER
