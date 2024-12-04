#Advent of Code 2024: Day 4
from icecream import ic

def find_XMAS(coord, direction):
    r,c = coord
    dr, dc = direction
    for char in "MAS":
        r += dr
        c += dc
        if (r,c) not in grid.keys():
            return False
        if grid[(r,c)] != char:
            return False
    return True

#MAIN
with open("data.txt") as file:
    lines = file.read().splitlines()

grid = dict()
for r, line in enumerate(lines):
    for c, char in enumerate(line):
        grid[r,c] = char

directions = {(dr, dc) for dr in [-1, 0, 1] for dc in [-1, 0, 1] if (dr, dc) != (0, 0)}

counter = 0
for coord, char in grid.items():
    if char == "X":
        for direction in directions:
            if find_XMAS(coord, direction):
                counter += 1

print(counter)
