from game import Board, Tile
from lexer import Lexer2048
from parser import Parser2048

# from parser import Parser2048

g = Board(size=(4, 4))
g.matrix[1][1] = Tile(index=(1, 1), value=3)
g.matrix[3][2] = Tile(index=(2, 1), value=1024)
print(g)

commands = [
    """ADD LEFT.""",
    """ASSIGN   (VALUE IN  3,8) TO 7,7""",
    """VAR ABC IS 5,8""",
    """VALUE IN 4,9""",
]

lexer, parser = Lexer2048(), Parser2048()
for command in commands:
    toks = lexer.tokenize(command)
    print([tok for tok in toks])
    parser.parse(toks)
    print(parser.command)
