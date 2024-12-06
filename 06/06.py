#Advent of Code 2024: Day 6
from icecream import ic
from collections import defaultdict
from datetime import datetime
time_start = datetime.now()

def tuple_sum(a,b):
    return tuple([x + y for x, y in zip(a,b)])

def create_grid(lines):
    grid = dict()
    guard = (0,0)
    for r, line in enumerate(lines):
        for c, char in enumerate(line):
            if char == "^":
                guard = (r,c)
                grid[(r,c)] = "."
            else:
                grid[(r,c)] = char
    return grid, guard

def step_or_turn(guard, direction):
    dr, dc = directions[direction]
    r, c = guard
    new_position = ((r + dr, c + dc))
    if new_position in grid.keys():
        if grid[new_position] != "#":
            guard = new_position
        else:
            direction = (direction + 1) % 4
    else:
        guard = -1
    return guard, direction

def loop_exists(start):
    #check whole path - if detected point from same direction -> loop
    guard = start
    direction = 0
    visited = defaultdict(set)
    while guard in grid.keys():
        guard, direction = step_or_turn(guard, direction)
        if direction in visited[guard]:
            return True
        elif guard != -1:
            visited[guard].add(direction)
    return False

#MAIN
with open("data.txt") as file:
    lines = file.read().splitlines()

grid, guard_start = create_grid(lines)
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # ULDR
direction = 0
path = defaultdict(set) # key = visited point, value = set of incoming directions
path[guard_start].add(0) #first point is also visited

#Part 1
guard = guard_start
while guard in grid.keys():
    guard, direction = step_or_turn(guard, direction)
    if guard != -1:
        path[guard].add(direction)
print("Part 1:", len(path.keys()))

#Part 2
result = 0
for counter, point in enumerate(path.keys()):
    if point == guard_start:
        continue
    grid[point] = "#"
    if loop_exists(guard_start):
        result += 1
    grid[point] = "."
print("Part 2:", result)

print("Runtime:", datetime.now() - time_start)