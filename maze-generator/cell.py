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
        return self._position[0] * self._maze_size[0] + self._position[1]

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, value):
        self._position = value

    @property
    def maze_size(self):
        return self._maze_size
     
    @maze_size.setter
    def maze_size(self, value):
        self._maze_size = value

    @property
    def wall_top(self):
        return self._walls[0]

    @wall_top.setter
    def wall_top(self, value):
        self._walls[0] = value

    @property
    def wall_left(self):
        return self._walls[1]

    @wall_left.setter
    def wall_left(self, value):
        self._walls[1] = value

    @property
    def wall_bottom(self):
        return self._walls[2]
    
    @wall_bottom.setter
    def wall_bottom(self, value):
        self._walls[2] = value

    @property
    def wall_right(self):
        return self._walls[3] 
    
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
