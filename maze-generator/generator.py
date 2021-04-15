from maze import *
from random import randrange


class Generator:
    def __init__(self):
        pass

    def generate_by_dfs(self, maze):
        size = maze.size
        used_cells = [[False for i in range(size[1])] \
                        for i in range(size[0])]
        stack = []
        cell = [0, 0]
        stack.append(cell)
        used_cells[cell[0]][cell[1]] = True
        while stack:
            current_cell = stack.pop()
            unvisited = False
            neighbours = maze.get_neighbours(current_cell)
            unvisited_neighbours = []
            for neighbour in neighbours:
                n_i, n_j = neighbour[0], neighbour[1]
                if not used_cells[n_i][n_j]:
                    unvisited = True
                    unvisited_neighbours.append(neighbour)
            if unvisited:
                stack.append(current_cell)
                choose = randrange(0, len(unvisited_neighbours))
                maze.remove_wall(current_cell, unvisited_neighbours[choose])
                un_i = unvisited_neighbours[choose][0]
                un_j = unvisited_neighbours[choose][1]
                used_cells[un_i][un_j] = True
                stack.append(unvisited_neighbours[choose])
        return maze

    def generate(self, maze_, type_="DFS"):
        if type_ == "DFS":
            return self.generate_by_dfs(maze_)
        elif type_ == "MST":
            return self.generate_by_mst(maze_)