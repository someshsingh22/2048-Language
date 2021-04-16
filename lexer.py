from sly import Lexer
import string
import re
from errors import ForeignCharacter, WrongCharacter, FalseTermination, FullStopNotFound


class Lexer2048(Lexer):
    """
    Lexer2048 Class, Subclass of sly.lexer Used to preprocess, tokenize text for pipelining to parser and game

    Parameters:
    tokens: The set of tokens used for grammer
    ignore: spaces and tabs are ignored
    literals: . ? , are given literals
    """

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
    NUMBER = r"-?\d+"
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
        """
        Called When Lexer encounters an Invalid / Foreign Token

        t: Input Token
        """
        raise ForeignCharacter(self.index, t.value[0])

    def preprocess(self, text, lineno=1, index=0):
        """
        Preprocess String for checking Full Stops / Misplaced Characters

        text: Input Command
        """
        vocab = set(string.ascii_letters + string.digits + " .,?-")
        for i, char in enumerate(text):
            if char not in vocab:
                raise ForeignCharacter(i, char)
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
                raise FullStopNotFound
            elif D != length - 1:
                raise FalseTermination(D)
            else:
                return ltext[:-1]
