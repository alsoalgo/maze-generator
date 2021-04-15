import argparse
from maze_generator import *

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("generation_type", help="Select DFS or MST algorithm generation type")
    parser.add_argument("graphics", help="Select console or gui display type")
    args = parser.parse_args()
    print(args.generation_type, args.graphics)


if __name__ == "__main__":
    main()