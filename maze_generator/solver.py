from .cell import Cell
from .maze import Maze


class Solver:
    _maze = Maze()

    def __init__(self, maze_=Maze()):
        self._maze = maze_
    
    def solve(self):
        pass