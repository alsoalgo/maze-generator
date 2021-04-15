from .cell import Cell
from .maze import Maze
from queue import Queue


class Solver:
    _maze = Maze()
    path = []

    def __init__(self, maze_=Maze()):
        self._maze = maze_
    
    def solve(self) -> list:
        begin = self._maze.begin
        end = self._maze.end
        size = self._maze.size
        #implement of bfs algorithm
        queue = Queue()
        queue.put(begin)
        used_cells = [[False for i in range(size[1])] \
                       for j in range(size[0])]
        came_from = [[[-1, -1] for i in range(size[1])] \
                       for j in range(size[0])]
        used_cells[begin[0]][begin[1]] = True
        while queue:
            current_cell = queue.get()
            neighbours = self._maze.get_neighbours(current_cell)
            walls = ["top", "left", "bottom", "right"]
            for i in range(4):
                if not getattr(current_cell, "wall_" + walls[i]) \
                    and not used_cells[neighbours[i][0]][neighbours[i][1]]:
                        queue.put(neighbour)
                        used_cells[neighbour[0]][neighbour[1]] = True
                        came_from[neighbour[0]][neighbour[1]] = [current_cell[0], current_cell[1]]
                        