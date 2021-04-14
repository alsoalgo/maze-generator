class Cell:
    walls = [True, True, True, True]

    def __if_exists(arguments, variable):
        if variable in arguments.keys():
            return int(arguments[variable])
        return 0

    def __init__(self, **kwargs):
        arguments = kwargs.items()
        self.maze_size = (__if_exists(arguments, "n"), __if_exists(arguments, "m"))
        self.position = (__if_exists(arguments, "i"), __if_exists(arguments, "j"))
        self.walls = [True, True, True, True] 

    @property
    def position(self):
        return self.position

    @property
    def maze_size(self):
        return self.maze_size 

    @property
    def wall_top(self):
        return self.walls[0]

    @property
    def wall_left(self):
        return self.walls[1]

    @property
    def wall_bottom(self):
        return self.walls[2]

    @property
    def wall_right(self):
        return self.walls[3] 
    
