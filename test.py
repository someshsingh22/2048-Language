from game import Board
from lexer import Lexer2048
from parser import Parser2048

board = Board(size=(4, 4))
lexer, parser = Lexer2048(), Parser2048(fmap=board.fmap)
print("Welcome to the 2048 Gaming Language, Below is the Board. Happy Coding!")
print(board)
while True:
    try:
        command = lexer.err(input("2048>"))
        out = parser.parse(lexer.tokenize(command))

    except NotImplementedError:
        print("Board Function Not Implemented Yet")

    except Exception as E:
        print(str(E))
