from game import Board, Tile
from lexer import Lexer2048
from parser import Parser2048

# from parser import Parser2048

lexer = Lexer2048()
parser = Parser2048()
while True:
    command = input("2048> ")

    try:
        tokens = lexer.tokenize(command)
        for token in tokens:
            print(token)
        parsed = parser.parse(tokens)

    except Exception as E:
        print(str(E))
