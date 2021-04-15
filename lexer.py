from sly import Lexer
import re
from errors import InvalidCharacter, WrongCharacter, FalseTermination, EndNotFound


class Lexer2048(Lexer):
    def err(self, text, lineno=1, index=0):
        ltext = text.rstrip()
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
                return ltext[:-1]

    # Set of token names. This is always required
    tokens = {
        IDENTIFIER,
        NUMBER,
        COMMA,
        OPERATION,
        DIRECTION,
        ASSIGN,
        TO,
        VAR,
        IS,
        VALUE,
        IN,
    }

    ignore = " \t"
    literals = {".", "?", ","}

    # Identifiers and keywords
    COMMA = r"\,"
    NUMBER = r"\d+"
    IDENTIFIER = r"[a-zA-Z]+[a-zA-Z0-9]*"
    IDENTIFIER["ADD"] = OPERATION
    IDENTIFIER["SUBTRACT"] = OPERATION
    IDENTIFIER["MULTIPLY"] = OPERATION
    IDENTIFIER["DIVIDE"] = OPERATION
    IDENTIFIER["LEFT"] = DIRECTION
    IDENTIFIER["RIGHT"] = DIRECTION
    IDENTIFIER["UP"] = DIRECTION
    IDENTIFIER["DOWN"] = DIRECTION
    IDENTIFIER["ASSIGN"] = ASSIGN
    IDENTIFIER["TO"] = TO
    IDENTIFIER["VAR"] = VAR
    IDENTIFIER["IS"] = IS
    IDENTIFIER["VALUE"] = VALUE
    IDENTIFIER["IN"] = IN

    def error(self, t):
        raise InvalidCharacter(self.index, t.value[0])
