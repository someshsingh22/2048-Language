from game import Board, Tile
from lexer import Lexer2048
from parser import Parser2048

out = []
lexer, parser = Lexer2048(), Parser2048()
while True:
    command = input("2048>")
    command = lexer.err(command)
    out = parser.parse(lexer.tokenize(command))
    print(out)
