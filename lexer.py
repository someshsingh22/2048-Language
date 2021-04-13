# calclex.py

from sly import Lexer


class Lexer2048(Lexer):

    # Set of token names. This is always required
    tokens = {
        IDENTIFIERS,
        NUMBER,
        INDEX,
        OPERATION,
        DIRECTION,
        ASSIGN,
        TO,
        VAR,
        IS,
        VALUE,
        IN,
        LPAREN,
        RPAREN,
    }

    ignore = " \t"
    literals = {".", "?", ","}

    # Identifiers and keywords
    INDEX = r"[0-9]+,[0-9]+"
    NUMBER = r"[0-9]+"
    IDENTIFIERS = r"[A-Z_][A-Z0-9_]*"
    IDENTIFIERS["ADD"] = OPERATION
    IDENTIFIERS["SUBTRACT"] = OPERATION
    IDENTIFIERS["MULTIPLY"] = OPERATION
    IDENTIFIERS["DIVIDE"] = OPERATION
    IDENTIFIERS["LEFT"] = DIRECTION
    IDENTIFIERS["RIGHT"] = DIRECTION
    IDENTIFIERS["UP"] = DIRECTION
    IDENTIFIERS["DOWN"] = DIRECTION
    IDENTIFIERS["ASSIGN"] = ASSIGN
    IDENTIFIERS["TO"] = TO
    IDENTIFIERS["VAR"] = VAR
    IDENTIFIERS["IS"] = IS
    IDENTIFIERS["VALUE"] = VALUE
    IDENTIFIERS["IN"] = IN
    LPAREN = r"\("
    RPAREN = r"\)"

    def error(self, t):
        print("Line %d: Bad character %r" % (self.lineno, t.value[0]))
        self.index += 1
