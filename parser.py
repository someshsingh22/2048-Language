from sly import Parser
from lexer import Lexer2048


class Parser2048(Parser):
    def __init__(self):
        self.command = []

    tokens = Lexer2048.tokens

    @_("OPERATION DIRECTION")
    def command(self, p):
        self.command = ("move", {"direction": p.DIRECTION, "operation": p.OPERATION})

    @_("ASSIGN NUMBER TO INDEX")
    def command(self, p):
        self.command = ("assign", {"index": p.INDEX, "value": p.NUMBER})

    @_("ASSIGN LPAREN VALUE IN INDEX RPAREN TO INDEX")
    def command(self, p):
        self.command = (
            "assign_query",
            {"index": p.INDEX0, "value": ("query", {"index": p.INDEX1})},
        )

    @_("VALUE IN INDEX")
    def command(self, p):
        self.command = ("query", {"index": p.INDEX})

    @_("VAR INDENTIFIER IS INDEX")
    def command(self, p):
        self.command = ("name", {"varName": p.VAR, "index": p.INDEX})
