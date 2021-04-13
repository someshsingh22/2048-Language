from sly import Lexer
import re
from utils import areBracketsBalanced
from errors import InvalidCharacter, WrongCharacter, FalseTermination, EndNotFound


class Lexer2048(Lexer):
    def err_tokenize(self, text, lineno=1, index=0):
        ltext = areBracketsBalanced(text)
        ltext = text.rstrip()
        _ = self.tokenize(text, lineno=1, index=0)
        Q, D, length = ltext.find("?"), ltext.find("."), len(ltext)
        if Q >= 0:
            if D >= 0:
                if Q < D or (D == length - 1):
                    raise WrongCharacter("?", Q)
                else:
                    raise FalseTermination(D)
            else:
                raise WrongCharacter("?", Q)
        else:
            if D == -1:
                raise EndNotFound
            elif D != length - 1:
                raise FalseTermination(D)
            else:
                pass
        return self.tokenize(ltext[:-1], lineno=1, index=0)

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

    def error(self, t):
        raise InvalidCharacter(self.index, t.value[0])
