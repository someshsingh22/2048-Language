import random


class Tile:
    """
    The tiles used for the 2048 Board, contains the list of assignments mapped and value of the tile

    parameters:
    value: the value present in the tile currently
    variables: list of variables mapped currently
    """

    def __init__(self, index, value=0, variables=[]):
        self.value = value
        self.variables = variables
        self.index = index

    def __repr__(self):
        return "%4d " % self.value if self.value > 0 else " " * 5

    def __add__(self, tile):
        """
        The add operation on a tile, updating the values and histories
        paramaters:
        tile: tile object for operation
        """
        raise NotImplementedError

    def __sub__(self, tile):
        """
        The sub operation on a tile, updating the values and histories
        paramaters:
        tile: tile object for operation
        """
        raise NotImplementedError

    def __mul__(self, tile):
        """
        The mul operation on a tile, updating the values and histories
        paramaters:
        tile: tile object for operation
        """
        raise NotImplementedError

    def __truediv__(self, tile):
        """
        The divide operation on a tile, updating the values and histories
        paramaters:
        tile: tile object for operation
        """
        raise NotImplementedError

    def assign(self, value):
        """
        Assign the value for the given tile
        parameters:
        value: the value to be updated
        """
        raise NotImplementedError

    def merge(self, variables):
        """
        merges variables of tile
        parameters:
        variables: the list of variables to be merged
        """
        raise NotImplementedError


class Board:
    """
    The 2048 Game Engine, takes commands from the translator and executes

    Parameters:
    size: 2-tuple of number of rows and columns
    """

    def __init__(self, size=(4, 4), target=2048):
        self.rows, self.columns = size
        self.matrix = [
            [Tile(index=(r, c)) for c in range(self.columns)] for r in range(self.rows)
        ]
        self.target = target

    def __repr__(self):
        return "\n".join([row.__repr__() for row in self.matrix]).replace(",", "|")

    def assign(self, index, value):
        """
        Assign Operation, Takes index and value and assigns value to that index
        """
        raise NotImplementedError

    def move(self, direction, operation):
        """
        Move Operation, Moves in the given direction and applies the given operation
        """
        raise NotImplementedError

    def name(self, varName, value):
        """
        Assigns some value to given varnames in memory
        """

    def query(self, index):
        """
        Returns the value on given index
        """
        raise NotImplementedError

    def get_identifiers(self):
        """
        Retrieves the list of identifiers in the memory
        """
        raise NotImplementedError
