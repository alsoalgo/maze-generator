from .cell import Cell
from .maze import Maze
from queue import Queue


class Solver:
    _maze = Maze()
    _path = []

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
            for neighbour in neighbours:
                is_used_n = used_cells[neighbours[i][0]][neighbours[i][1]]
                is_wall_exists = getattr(current_cell, "wall_" + current_cell.neighbour_type(neighbour))
                if not is_wall_exists and not is_used_n:
                        queue.put(neighbour)
                        used_cells[neighbour[0]][neighbour[1]] = True
                        came_from[neighbour[0]][neighbour[1]] = [current_cell[0], current_cell[1]]
        path_ = [end]
        cell_ = end
        while came_from[cell_[0]][cell_[1]] != [-1, -1]:
            cell_ = came_from[cell[0]][cell[1]]
            path.append(cell_)
        path_ = path_[::-1]
        self._path = path_
        return self._path
    
    @property
    def path(self):
        return self._path
