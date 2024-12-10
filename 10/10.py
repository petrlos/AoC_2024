#Advent of Code 2024: Day 10
from icecream import ic
from collections import deque

def tuple_sum(a,b):
    return tuple([x + y for x, y in zip(a,b)])

def create_grid(lines):
    starts = set()
    grid = dict()
    for r, line in enumerate(lines):
        for c, char in enumerate(line):
            if char == ".":
                continue
            grid[(r,c)] = int(char)
            if char == "0":
                starts.add((r,c))
    return grid, starts

def count_paths(start, grid):
    directions = [(-1, 0), (1,0), (0,-1), (0,1)] #UDlR
    queue = deque([start])
    peaks = set()
    while queue: 
        current = queue.popleft()
        for direction in directions:
            new_point = tuple_sum(direction, current)
            if new_point in grid.keys():
                if (grid[new_point] == grid[current] + 1):
                    queue.append(new_point)
                    if grid[new_point] == 9:
                        peaks.add(new_point)
    return len(peaks)

#MAIN
with open("data.txt") as file:
    lines = file.read().splitlines()

grid, starts = create_grid(lines)

result = 0
for start in starts:
    result += count_paths(start, grid)
print("Part 1:", result)