#Advent of Code 2024: Day 18
from collections import deque

def tuple_sum(a,b):
    return tuple([x + y for x, y in zip(a,b)])

def find_path(lines, bytes, size):
    walls = {tuple(map(int, line.split(","))) for line in lines[:bytes]}
    target = (size, size)
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    visited = {(0, 0): 0}
    queue = deque([(0, 0)])
    while queue:
        current = queue.popleft()
        neighbours = [tuple_sum(direction, current) for direction in directions]
        for neighbour in neighbours:
            r, c = neighbour
            if 0 <= r <= size and 0 <= c <= size:
                if neighbour not in visited.keys() and neighbour not in walls :
                    visited[neighbour] = visited[current] + 1
                    queue.append(neighbour)
    if target in visited.keys():
        return visited[target]
    else:
        return -1

#MAIN
with open("data.txt") as file:
    lines = file.read().splitlines()

part1 = find_path(lines, 1024, 70)
print("Part 1:", part1)

for bytes in range(len(lines), 0, -1):
    if find_path(lines, bytes, 70) > 0:
        print(bytes, lines[bytes])
        break