#Advent of Code 2024: Day 16
import heapq
from collections import defaultdict
from icecream import ic

def create_grid(lines):
    grid = set()
    start, end = tuple(), tuple()
    for r, line in enumerate(lines):
        for c, char in enumerate(line):
            if char == "S":
                start = (r,c)
            if char == "E":
                end = (r,c)
            if char != "#":
                grid.add((r,c))
    return grid, start, end

def tuple_sum(a,b):
    return tuple([x + y for x, y in zip(a,b)])

def find_shortest_path(grid, start, end):
    directions = ((0, 1), (-1, 0), (0, -1), (1, 0))

    queue = []
    heapq.heappush(queue, [0, 0, start, []])
    visited = {}

    while queue:
        score, dir, coords, path = heapq.heappop(queue)
        if coords in visited and score >= visited[coords]: #dont test any visits, that have larger score
            continue
        visited[coords] = score #update socre of current visit
        if coords == end: #reached end
           return score
        if coords not in grid: #out of grid
            continue
        for new_score, new_dir, new_coords, in [[score + 1, dir, tuple_sum(coords, directions[dir])], #forward
                                                [score + 1001, (dir + 1) % 4, #turn left + move forward
                                                 tuple_sum(coords, directions[(dir + 1) % 4])],
                                                [score + 1001, (dir - 1) % 4, #turn right + move forward
                                                 tuple_sum(coords, directions[(dir - 1) % 4])]]:
            heapq.heappush(queue, [new_score, new_dir, new_coords, path + [coords]]) #add to heap

#MAIN
with open("data.txt") as file:
    lines = file.read().splitlines()i ne

grid, start, end = create_grid(lines)

print(f"Part 1: {find_shortest_path(grid, start, end)}")