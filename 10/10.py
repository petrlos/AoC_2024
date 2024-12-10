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

def count_paths_part1(start, grid):
    #bfs - search all 9s that may be found from 0 with succesive steps by 1
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

def count_paths_part2(start, grid):
    directions = [(-1, 0), (1,0), (0,-1), (0,1)] #UDlR
    paths = list() #saves final path
    queue = deque([[start]]) #queue of not yet completed paths
    while queue:
        current = queue.popleft()
        new_points = [tuple_sum(direction, current[-1]) for direction in directions] #find all neighbours from last point
        for new_point in new_points:
            if new_point in grid.keys():
                if (grid[new_point] == grid[current[-1]] + 1): #new point is by 1 larger
                    if grid[new_point] == 9:
                        paths.append(current + [new_point]) #path completed - save it, dont look further
                    else:
                        queue.append(current + [new_point]) #path not yet completed, save to queue
    return len(paths)

#MAIN
with open("data.txt") as file:
    lines = file.read().splitlines()

grid, starts = create_grid(lines)

result_1 = 0
result_2 = 0
for start in starts:
    result_1 += count_paths_part1(start, grid)
    result_2 += count_paths_part2(start, grid)
print("Part 1:", result_1)
print("Part 2:", result_2)