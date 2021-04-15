#from maze import Maze
import colorama
from colorama import Fore, Back, Style


class View:
    #_maze = Maze()

    def __init__(self, maze_=""):
        self._maze = maze_

    @property
    def maze(self):
        return self._maze
    
    @maze.setter
    def maze(self, value):
        self._maze = value

    
    def draw(self, type_="console"):
        def cyan(): # border
            return Fore.CYAN + Back.CYAN + "#" + Style.RESET_ALL

        def white(): # empty
            return Fore.WHITE + Back.WHITE + "#" + Style.RESET_ALL

        
        colorama.init()
        size = self._maze.size
        output = [[cyan() for i in range(size[1] * 4 + 2)] for i in range(size[0] * 4 + 2)]

        walls = {"top" : [[-1, 0], [-1, 1]],
                 "left" : [[0, -1], [1, -1]],
                 "bottom" : [[2, 0], [2, 1]],
                 "right" : [[0, 2], [1, 2]],
                }

        map = self._maze.map
        for i in range(size[0]):
            for j in range(size[1]):
                cell = map[i][j]
                out_i = 2 + 4 * i
                out_j = 2 + 4 * j
                for wall in walls:
                    if getattr(cell, "wall_" + wall[0]):
                        output[out_i][out_j] = cyan()
                    else:
                        output[out_i][out_j] = white()
        output_string = ""
        for line in output:
            output_string += "".join(line) + "\n"
        print(output_string)

    def load(self, path):
        pass
    
    def save(self, path):
        pass
