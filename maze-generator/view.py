from maze import Maze
from generator import Generator
import colorama
from colorama import Fore, Back, Style


class View:
    _maze = Maze()

    def __init__(self, maze_=Maze()):
        self._maze = maze_

    @property
    def maze(self):
        return self._maze
    
    @maze.setter
    def maze(self, value):
        self._maze = value

    
    def draw(self, type_="console"):
        def border(): # border
            prefix = Fore.BLACK + Back.BLACK
            postfix = Style.RESET_ALL
            return prefix + "\u2B1B" + postfix

        def empty(): # empty
            prefix = Fore.WHITE + Back.WHITE 
            postfix = Style.RESET_ALL
            return prefix + "\u2B1B" + postfix

        
        colorama.init()
        size = self._maze.size
        output = [[border() for i in range(size[1] * 4 + 2)] for i in range(size[0] * 4 + 2)]

        walls = {"top" : [[-1, 0], [-1, 1]],
                 "left" : [[0, -1], [1, -1]],
                 "bottom" : [[2, 0], [2, 1]],
                 "right" : [[0, 2], [1, 2]],
                }
        cell_inner = [[0, 0], [0, 1],
                      [1, 0], [1, 1],
                      ]

        map = self._maze.map
        for i in range(size[0]):
            for j in range(size[1]):
                cell = map[i][j]
                out_i = 2 + 4 * i
                out_j = 2 + 4 * j
                for move in cell_inner:
                    output[out_i + move[0]][out_j + move[1]] = empty()
                for wall in walls:
                    if not getattr(cell, "wall_" + wall):
                        for move in walls[wall]:
                            output[out_i + move[0]][out_j + move[1]] = empty()
        output_string = ""
        for line in output:
            output_string += "".join(line) + "\n"
        print(output_string)

    def load(self, path):
        pass
    
    def save(self, path):
        pass
        size = self._maze.size
        output = [["#" for i in range(size[1] * 4 + 2)] for i in range(size[0] * 4 + 2)]

        walls = {"top" : [[-1, 0], [-1, 1]],
                 "left" : [[0, -1], [1, -1]],
                 "bottom" : [[2, 0], [2, 1]],
                 "right" : [[0, 2], [1, 2]],
                }
        cell_inner = [[0, 0], [0, 1],
                      [1, 0], [1, 1],
                      ]

        map = self._maze.map
        for i in range(size[0]):
            for j in range(size[1]):
                cell = map[i][j]
                out_i = 2 + 4 * i
                out_j = 2 + 4 * j
                for move in cell_inner:
                    output[out_i + move[0]][out_j + move[1]] = " "
                for wall in walls:
                    if not getattr(cell, "wall_" + wall):
                        for move in walls[wall]:
                            output[out_i + move[0]][out_j + move[1]] = " "
        output_string = ""
        for line in output:
            output_string += "".join(line) + "\n"
        
        file_ = open(path + ".txt", "r")
        file_.write(output_string)
        file_.close()
