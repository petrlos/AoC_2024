#Advent of Code 2024: Day 15
from icecream import ic

def create_grid(lines):
    grid = dict()
    lines = lines.splitlines()
    for r, line in enumerate(lines):
        for c, char in enumerate(line):
            if char in ".O@":
                grid[(r,c)] = char
    max_r, max_c = len(lines[0]), len(lines)
    return grid, max_r, max_c

def print_grid(grid, max_r, max_c):
    for r in range(max_r):
        for c in range(max_c):
            if (r,c) in grid.keys():
                print(grid[(r,c)], end="")
            else:
                print("#", end="")
        print("")

def count_gps(grid):
    gps = 0
    for coord, item in grid.items():
        if item == "O":
            gps += coord[0] *100 + coord[1]
    return gps

with open("test_2.txt") as file:
    lines = file.read().split("\n\n")

grid, max_r, max_c = create_grid(lines[0])

print_grid(grid, max_r, max_c)
print(count_gps(grid))