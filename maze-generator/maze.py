from cell import Cell

from functools import singledispatchmethod

class Maze:
    _map = []
    _size = (0, 0)

    def is_possible(self, i, j):
        return (0 <= i) and (i < self._size[0]) \
            and (0 <= j) and (j < self._size[1])

    def get_cell(self, i, j):
        if self.is_possible(i, j):
            return self._map[i][j]
        return None
    
    def __init__(self, n=1, m=1):
        self._size = (n, m)
        self._map.clear()
        for i in range(self._size[0]):
            self._map.append([])
            for j in range(self._size[1]):
                self._map[i].append(Cell(n=self._size[0], m=self._size[1], i=i, j=j))
    
    def __getitem__(self, coordinates):
        if isinstance(coordinates, int):
            coordinates = [coordinates // self._size[0], coordinates % self._size[1]]
        if self.is_possible(coordinates[0], coordinates[1]):
            return self._map[coordinates[0]][coordinates[1]]
        raise IndexError
    
    def __setitem__(self, coordinates, cell):
        if isinstance(coordinates, int):
            coordinates = [coordinates // self._size[0], coordinates % self._size[1]]
        if self.is_possible(coordinates[0], coordinates[1]):
            self._map[coordinates[0]][coordinates[1]] = cell
        raise IndexError
    
    @singledispatchmethod
    def get_neighbours(self, cell):
        raise NotImplementedError
    
    @get_neighbours.register
    def _(self, cell : list) -> list:
        neighbours = []
        i = cell[0]
        j = cell[1]
        moves = [[-1, 0], [0, -1], [1, 0], [0, 1]]
        for (move_i, move_j) in moves:
            neighbour_i = i + move_i
            neighbour_j = j + move_j
            neighbour = self.get_cell(neighbour_i, neighbour_j)
            if neighbour:
                neighbours.append(neighbour)
        return neighbours
    
    @get_neighbours.register
    def _(self, cell : int) -> list:
        i = cell // self._size[0]
        j = cell % self._size[1]
        return self.get_neighbours([i, j])
    
    @get_neighbours.register
    def _(self, cell : Cell) -> list:
        return self.get_neighbours(int(cell))

    @singledispatchmethod
    def remove_wall(self, first_cell, second_cell):
        raise NotImplementedError

    @remove_wall.register
    def _(self, first_cell, second_cell):
        if isinstance(first_cell, int):
            first_cell = self.get_cell(first_cell // self._size[0], first_cell % self._size[1])
        if isinstance(second_cell, int):
            second_cell = self.get_cell(second_cell // self._size[1], second_cell % self._size[1])
        f_i, f_j = first_cell.position[0], first_cell.position[1]
        s_i, s_j = second_cell.position[0], second_cell.position[1]
        neighbourhood_type = ["top", "left", "bottom", "right"]
        opposite = ["bottom", "right", "top", "left"]
        for i in range(4):
            is_ = getattr(first_cell, "is_" + neighbourhood_type[i])
            if is_(second_cell):
                setattr(first_cell, "wall_" + neighbourhood_type[i], False)
                setattr(second_cell, "wall_" + opposite[i], False)
                self[f_i, f_j] = first_cell
                self[s_i, s_j] = second_cell
    
    @remove_wall.register
    def _(self, first_cell : list, second_cell : list):
        f_i, f_j = first_cell[0], first_cell[1]
        s_i, s_j = second_cell[0], second_cell[1]
        self.remove_wall(self[f_i, f_j], self[s_i, s_j])
    
    def 
    
    



    