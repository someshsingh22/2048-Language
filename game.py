import random
import re
from copy import deepcopy
import sys
from itertools import product
from errors import (
    WrongIndex,
    IdentifierExists,
    EmptyTileNamingException,
    EmptyTileQueryException,
)


class Tile:
    """
    The tiles used for the 2048 Board, contains the list of assignments mapped and value of the tile

    parameters:
    value: the value present in the tile currently
    variables: list of variables mapped currently
    """

    def __init__(self, index):
        super().__init__()
        self.value = 0
        self.index = index
        self.variables = list()

    def re_index(self, index):
        """
        Update index of tile after move
        """
        self.index = index

    def __repr__(self):
        return "%4d " % self.value if self.value > 0 else " " * 5


class Board:
    """
    The 2048 Game Engine, takes commands from the translator and executes

    Parameters:
    size: 2-tuple of number of rows and columns
    """

    def __init__(self, size=(4, 4)):
        self.rows, self.columns = size
        self.matrix = self.empty_matrix()
        self.add_random_tile()
        self.add_random_tile()

        self.fmap = {
            "NAME": self.name,
            "ASSIGN": self.assign,
            "QUERY": self.query,
            "MOVE": self.move,
            "get_id": self.get_identifiers,
        }

        print(
            "2048 >>> Welcome to the 2048 Gaming Language, Below is the Board. Happy Coding!"
        )
        print(self)

    def empty_matrix(self):
        """
        Creates an empty board
        """
        return [
            [Tile(index=(r, c)) for c in range(self.columns)] for r in range(self.rows)
        ]

    def update_indexes(self):
        """
        Update All indexes after moving
        """
        for row, col in product(range(self.rows), range(self.columns)):
            self.matrix[row][col].re_index((row, col))

    def __repr__(self):
        """
        Printer Function
        """
        return re.sub(
            r"[\,\[\]]", "|", "\n".join([row.__repr__() for row in self.matrix])
        )

    def compress(self):
        """
        Compress Utility Function
        """
        new_mat = self.empty_matrix()
        for i in range(self.rows):
            pos = 0
            for j in range(self.columns):
                if self.matrix[i][j].value != 0:
                    new_mat[i][pos] = deepcopy(self.matrix[i][j])
                    pos += 1
        self.matrix.clear()
        self.matrix = deepcopy(new_mat)

    def merge(self, operation):
        """
        Merge operation for tiles
        """
        for i in range(self.rows):
            for j in range(self.columns - 1):
                if (
                    self.matrix[i][j].value == self.matrix[i][j + 1].value
                    and self.matrix[i][j].value != 0
                ):
                    if operation == "SUBTRACT":
                        self.matrix[i][j].value = 0
                        self.matrix[i][j].variables.clear()

                    else:
                        if operation == "ADD":
                            self.matrix[i][j].value *= 2
                        elif operation == "MULTIPLY":
                            self.matrix[i][j].value *= self.matrix[i][j].value
                        elif operation == "DIVIDE":
                            self.matrix[i][j].value = 1

                        self.matrix[i][j].variables.extend(
                            self.matrix[i][j + 1].variables
                        )

                    self.matrix[i][j + 1].value = 0
                    self.matrix[i][j + 1].variables.clear()

    def reverse_matrix(self):
        """
        Returns the reverse of matrix
        """
        for row in range(self.rows):
            self.matrix[row].reverse()

    def transpose(self):
        """
        Returns the transpose of matrix
        """
        for row in range(self.rows):
            for col in range(row):
                self.matrix[row][col], self.matrix[col][row] = (
                    self.matrix[col][row],
                    self.matrix[row][col],
                )

    def move(self, direction, operation, verbose=True):
        """
        Move Operation, Moves in the given direction and applies the given operation
        """
        if direction == "UP":
            self.transpose()
            self.move("LEFT", operation, verbose=False)
            self.transpose()
        elif direction == "DOWN":
            self.transpose()
            self.move("RIGHT", operation, verbose=False)
            self.transpose()
        elif direction == "LEFT":
            self.compress()
            self.merge(operation)
            self.compress()
        elif direction == "RIGHT":
            self.reverse_matrix()
            self.move("LEFT", operation, verbose=False)
            self.reverse_matrix()
        else:
            print("INVALID DIRECTION")

        if not self.is_game_over() and verbose:
            self.add_random_tile()
            print(self)

        self.update_indexes()

    def assign(self, value, index):
        """
        Assign Operation, Takes index and value and assigns value to that index
        """
        x, y = index
        x, y = x - 1, y - 1

        if not self.is_valid(x, y):
            raise WrongIndex(index, (1, 1), (self.rows, self.columns))

        self.matrix[x][y].value = value
        if value == 0:
            self.matrix[x][y].variables.clear()
        print(self)

    def query(self, index):
        """
        Returns the value on given index
        """
        x, y = index
        x, y = x - 1, y - 1

        if not self.is_valid(x, y):
            raise WrongIndex(index, (1, 1), (self.rows, self.columns))

        elif self.empty_index(x, y):
            raise EmptyTileQueryException(index)

        value = self.matrix[x][y].value
        print(value)
        return value

    def name(self, varName, index):
        """
        Assigns some value to given varnames in memory
        """
        x, y = index
        x, y = x - 1, y - 1
        if self.varExists(varName):
            raise IdentifierExists(varName)

        elif not self.is_valid(x, y):
            raise WrongIndex(index, (1, 1), (self.rows, self.columns))

        elif self.empty_index(x, y):
            raise EmptyTileNamingException(index)

        else:
            self.matrix[x][y].variables.append(varName)

    def add_random_tile(self):
        row, col = random.choice(
            [
                index
                for index in product(range(self.rows), range(self.columns))
                if self.matrix[index[0]][index[1]].value == 0
            ],
        )
        self.matrix[row][col].value = 2 if random.random() <= 0.5 else 4

    def is_game_over(self):
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        for i, j in product(range(self.rows), range(self.columns)):
            if self.matrix[i][j].value == 0:
                return False
            for k in range(4):
                x = i + dx[k]
                y = j + dy[k]
                if (
                    self.is_valid(x, y)
                    and self.matrix[x][y].value == self.matrix[i][j].value
                ):
                    return False
        return True

    def empty_index(self, x, y):
        return self.matrix[x][y].value == 0

    def is_valid(self, x, y):
        return x >= 0 and y >= 0 and x < self.rows and y < self.columns

    def get_identifiers(self):
        var_out = ""
        for row, col in product(range(self.rows), range(self.columns)):
            tile = self.matrix[row][col]
            index = "%d,%d" % (row + 1, col + 1)
            var = ",".join(tile.variables)
            if var:
                var_out += index + var + "\40"
        return var_out

    def varExists(self, varName):
        for row in range(self.rows):
            for col in range(self.columns):
                if varName in self.matrix[row][col].variables:
                    return (row + 1, col + 1)
        return None

    def get_row_major(self):
        row_maj = []
        for row in self.matrix:
            row_maj.extend([str(tile.value) for tile in row])
        return "\40".join(row_maj)

    def eout(self):
        """
        Sends the message to stderr
        """
        print("%s %s" % (self.get_row_major(), self.get_identifiers()), file=sys.stderr)
