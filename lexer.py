# calclex.py

from sly import Lexer


class Lexer2048(Lexer):

    # Set of token names. This is always required
    tokens = {
        INDENTIFIER,
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
        END,
    }

    ignore = " \t"
    literals = {".", "?", ","}

    # Identifiers and keywords
    INDEX = r"[0-9]+[ ]*,[ ]*[0-9]+"
    NUMBER = r"[0-9]+"
    INDENTIFIER = r"[a-zA-Z]+[a-zA-Z0-9]*"
    INDENTIFIER["ADD"] = OPERATION
    INDENTIFIER["SUBTRACT"] = OPERATION
    INDENTIFIER["MULTIPLY"] = OPERATION
    INDENTIFIER["DIVIDE"] = OPERATION
    INDENTIFIER["LEFT"] = DIRECTION
    INDENTIFIER["RIGHT"] = DIRECTION
    INDENTIFIER["UP"] = DIRECTION
    INDENTIFIER["DOWN"] = DIRECTION
    INDENTIFIER["ASSIGN"] = ASSIGN
    INDENTIFIER["TO"] = TO
    INDENTIFIER["VAR"] = VAR
    INDENTIFIER["IS"] = IS
    INDENTIFIER["VALUE"] = VALUE
    INDENTIFIER["IN"] = IN
    LPAREN = r"\("
    RPAREN = r"\)"
    END = r"\."

    def error(self, t):
        print("Line %d: Bad character %r" % (self.lineno, t.value[0]))
        self.index += 1
