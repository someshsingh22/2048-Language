from sly import Parser
from lexer import Lexer2048


class Parser2048(Parser):
    tokens = Lexer2048.tokens

    def __init__(self):
        self.names = {}

    @_("expr")
    def statement(self, p):
        return p.expr

    @_("NUMBER")
    def statement(self, p):
        return int(p.NUMBER)

    @_("VAR IDENTIFIER IS expr COMMA expr")
    def expr(self, p):
        return (p.IDENTIFIER, p.expr0, p.expr1)

    @_("ASSIGN expr TO expr COMMA expr")
    def expr(self, p):
        return (p.expr0, p.expr1, p.expr2)

    @_("VALUE IN NUMBER COMMA NUMBER")
    def expr(self, p):
        return (p.NUMBER0, p.NUMBER1)

    @_("OPERATION DIRECTION")
    def statement(self, p):
        return (p.OPERATION, p.DIRECTION)

    @_("IDENTIFIER")
    def statement(self, p):
        try:
            return self.names[p.IDENTIFIER]
        except LookupError:
            print(f"Undefined name {p.IDENTIFIER!r}")
            return 0
