from game import Board, Tile
from lexer import Lexer2048
from parser import Parser2048


lexer, parser = Lexer2048(), Parser2048()
out = 0
while True:
    try:
        command = input("2048>")
        command = lexer.err(command)
        tokens = lexer.tokenize(command)
        for token in tokens:
            print(token)
        out = parser.parse(lexer.tokenize(command))
        print(out)
    except Exception as E:
        print(str(E))
