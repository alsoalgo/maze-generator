from .cell import Cell
from .maze import Maze
from .generator import Generator

import colorama
from colorama import Fore, Back, Style

import os


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

    def maze_to_string(self):
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
        return output_string


    def draw_console(self):
        def border(): # border
            prefix = Fore.CYAN + Back.CYAN
            postfix = Style.RESET_ALL
            return prefix + "\u2B1B" + postfix

        def empty(): # empty
            prefix = Fore.WHITE + Back.WHITE 
            postfix = Style.RESET_ALL
            return prefix + "\u2B1B" + postfix

        
        colorama.init()
        maze_string = self.maze_to_string()
        beautiful_maze_string = ""
        for symbol in maze_string:
            if symbol == "#":
                beautiful_maze_string += border()
            elif symbol == ' ':
                beautiful_maze_string += empty()
            else:
                beautiful_maze_string += symbol

        print(beautiful_maze_string)
    
    def draw_graphics(self):
        pass
    
    def draw(self, type_="console"):
        if type_ == "console":
            self.draw_console()
        else:
            self.draw_graphics()

    def load(self, path):
        file_ = None
        try:
            file_ = open(path, "r")
        except FileNotFoundError:
            raise FileNotFoundError("There's no such labyrinth file")
        lines = file_.readlines()
        n = (len(lines) - 2) // 4
        m = (len(lines[0]) - 2) // 4
        self._maze = Maze(n, m)
        walls = {"top" : [-1, 1],
                 "left" : [0, -1],
                 "bottom" : [2, 0],
                 "right" : [1, 2],
                }
        
        for i in range(n):
            for j in range(m):
                current_cell = Cell(n=n, m=m, i=i, j=j)
                c_i = 2 + 4 * i
                c_j = 2 + 4 * j
                for wall in walls:
                    move_i = c_i + walls[wall][0]
                    move_j = c_j + walls[wall][1]
                    setattr(current_cell, "wall_" + wall, "#" == lines[move_i][move_j])
                self._maze[i, j] = current_cell
    
    def save(self, path):
        output_string = self.maze_to_string()
        if "labyrinths" not in os.listdir(path):
            os.mkdir(path + "labyrinths")
        labyrinths = os.listdir(path + "labyrinths")
        count = 1
        for filename in labyrinths:
            if filename.startswith("labyrinth"):
                count += 1
        file_ = open(path + "labyrinths/labyrinth" + str(count) + ".txt", "w")
        file_.write(output_string)
        file_.close()
