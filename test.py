from game import Board, Tile
from lexer import Lexer2048
from parser import Parser2048

# from parser import Parser2048

lexer = Lexer2048()
while True:
    command = input("2048> ")

    if command == 0:
        break

    for token in lexer.tokenize(command):
        print(token)
