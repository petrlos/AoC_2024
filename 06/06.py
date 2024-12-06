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
    return grid, guard, len(lines[0]), len(lines) # max row, max col

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

def loop_exists(start, in_directions):
    #put an obstacle on "next point", turn right and check, if comes back to start postion from same direction
    result = set()
    for in_direction in in_directions:
        guard = start
        obstacle = tuple_sum(start, directions[in_direction])
        grid[obstacle] = "#"
        direction = (in_direction + 1) % 4
        visited = defaultdict(set)
        while guard in grid.keys():
            guard, direction = step_or_turn(guard, direction)
            if direction in visited[guard]:
                ic(obstacle, direction, start)
                result.add(obstacle)
                guard = -1
            elif guard != -1:
                visited[guard].add(direction)
        grid[obstacle] = "."
    return result

#MAIN
with open("test.txt") as file:
    lines = file.read().splitlines()

grid, guard, max_row, max_col = create_grid(lines)
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # ULDR
direction = 0
path = defaultdict(set) # key = visited point, value = set of incoming directions
path[guard].add(0) #first point is also visited

while guard in grid.keys():
    guard, direction = step_or_turn(guard, direction)
    if guard != -1:
        path[guard].add(direction)
print("Part 1:", len(path.keys()))

#TODO: part2 not working completely yet - not detecting all possible points
loop_points = set()
counter = 0
for start, in_dirs in path.items():
    counter += 1
    loop_points |= loop_exists(start, in_dirs)
    if counter % 100 == 0:
        print(counter)

print(loop_points)
print(len(loop_points))

print("Runtime:", datetime.now() - time_start)