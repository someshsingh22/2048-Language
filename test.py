import sys
from game import Board
from lexer import Lexer2048
from parser import Parser2048

board = Board(size=(4, 4))
lexer, parser = Lexer2048(), Parser2048(fmap=board.fmap)

while True:
    try:
        print("\033[32m" + "2048 >>>" + "\033[0m", end=" ")
        inp = input()
        command = lexer.preprocess(inp)
        out = parser.parse(lexer.tokenize(command))
        board.eout()

    except EOFError:
        exit()

    except Exception as E:
        print(str(E))
        print("-1", file=sys.stderr)
