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

def find_cross_MAS(coord):
    ok_counter = 0
    r, c = coord
    corners_top = [(-1 + r,-1 + c), (-1 + r, 1 + c)] #topleft, topright corner
    corners_bot = [( 1 + r, 1 + c), ( 1 + r,-1 + c)] #bottomright,
    for cor_top, cor_bot in zip(corners_top, corners_bot):
        if cor_top not in grid.keys() or cor_bot not in grid.keys():
            #out of grid
            return False
        if grid[cor_top] != grid[cor_bot] and grid[cor_top] not in "XA" and grid[cor_bot] not in  "XA":
            #if they are not the same and not "X" or "A"
            ok_counter += 1
    return ok_counter == 2 #both lines of the cross must be correct

#MAIN
with open("data.txt") as file:
    lines = file.read().splitlines()

grid = dict()
for r, line in enumerate(lines):
    for c, char in enumerate(line):
        grid[r,c] = char

directions = {(dr, dc) for dr in [-1, 0, 1] for dc in [-1, 0, 1] if (dr, dc) != (0, 0)}

#Part1
counter_1 = 0
counter_2 = 0
for coord, char in grid.items():
    if char == "X": #checker for part1
        for direction in directions: #check every direction starting from "X"
            if find_XMAS(coord, direction):
                counter_1 += 1
    if char == "A": #checker for part2
        if find_cross_MAS(coord):
            counter_2 += 1

print("Part 1:", counter_1)
print("Part 2:", counter_2)