from game import Board, Tile

g = Board(size=(4, 4))
g.matrix[1][1] = Tile(index=(1, 1), value=3)
g.matrix[3][2] = Tile(index=(2, 1), value=1024)
print(g)
