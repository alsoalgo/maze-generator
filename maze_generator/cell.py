class Cell:
    _walls = [True, True, True, True]
    _maze_size = (0, 0)
    _position = (0, 0)

    @staticmethod
    def if_exists(arguments, variable):
        if variable in arguments:
            return int(arguments[variable])
        return 0

    def __init__(self, **kwargs):
        arguments = dict(kwargs)
        self._maze_size = (Cell.if_exists(arguments, "n"), 
                            Cell.if_exists(arguments, "m"))
        self._position = (Cell.if_exists(arguments, "i"), 
                            Cell.if_exists(arguments, "j"))
        self._walls = [True, True, True, True] 

    def __int__(self):
        return self._position[0] * self._maze_size[1] + self._position[1]

    def __getitem__(self, index):
        return self._position[index]
    
    def __setitem__(self, index, value):
        self._position[index] = value
    
    def __eq__(self, other_cell):
        return self._maze_size == other_cell._maze_size and \
               self._position == other_cell._position
    
    def __neq__(self, other_cell):
        return not (self == other_cell)

    @property
    def position(self):
        return self._position

    @property
    def maze_size(self):
        return self._maze_size
     
    @property
    def wall_top(self):
        return self._walls[0]

    @property
    def wall_left(self):
        return self._walls[1]

    @property
    def wall_bottom(self):
        return self._walls[2]

    @property
    def wall_right(self):
        return self._walls[3]

    @position.setter
    def position(self, value):
        self._position = value

    @maze_size.setter
    def maze_size(self, value):
        self._maze_size = value

    @wall_top.setter
    def wall_top(self, value):
        self._walls[0] = value

    @wall_left.setter
    def wall_left(self, value):
        self._walls[1] = value

    @wall_bottom.setter
    def wall_bottom(self, value):
        self._walls[2] = value

    @wall_right.setter
    def wall_right(self, value):
        self._walls[3] = value

    def is_top(self, other_cell):
        return self._position[0] - 1 == other_cell.position[0]
    
    def is_left(self, other_cell):
        return self._position[1] - 1 == other_cell.position[1]
    
    def is_bottom(self, other_cell):
        return self._position[0] + 1 == other_cell.position[0]
    
    def is_right(self, other_cell):
        return self._position[1] + 1 == other_cell.position[1]
    
    def neighbour_type(self, other_cell):
        if self.is_top(other_cell):
            return "top"
        if self.is_left(other_cell):
            return "left"
        if self.is_bottom(other_cell):
            return "bottom"
        if self.is_right(other_cell):
            return "right"