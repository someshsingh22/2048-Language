from game import Board, Tile
from lexer import Lexer2048
from parser import Parser2048


lexer, parser = Lexer2048(), Parser2048()
out = 0
while True:
    try:
        command = lexer.err(input("2048>"))
        out = parser.parse(lexer.tokenize(command))
    except Exception as E:
        print(str(E))
