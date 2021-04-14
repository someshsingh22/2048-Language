from game import Board
from lexer import Lexer2048
from parser import Parser2048

board = Board(size=(4, 4), target=69)
lexer, parser = Lexer2048(), Parser2048(fmap=board.fmap)

while True:
    try:
        command = lexer.err(input("2048>"))
        out = parser.parse(lexer.tokenize(command))

    except NotImplementedError:
        print("Board Function Not Implemented Yet")

    except Exception as E:
        print(str(E))
