from maze import *

class Generator:
    def __init__(self):
        pass

    def generate_by_dfs(self, maze):
        size = maze.size


        return maze

    def generate(self, maze_, type_="DFS"):
        if type_ == "DFS":
            return self.generate_by_dfs(maze_)
        elif type_ == "MST":
            return self.generate_by_mst(maze_)