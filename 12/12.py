#Advent of Code 2024: Day 12
from collections import defaultdict, deque
from icecream import ic

def tuple_sum(a,b):
    return tuple([x + y for x, y in zip(a,b)])

def create_grid(lines):
    grid = defaultdict(list)
    for r, line in enumerate(lines):
        for c, char in enumerate(line):
            grid[char].append((r,c))
    return grid, len(lines), len(lines[0])

def find_region_size_and_perimeter(coords):
    directions = [(-1, 0), (1,0), (0,-1), (0,1)] #UDlR
    queue = deque([coords[0]])
    visited = [coords[0]]
    while queue:
        current = queue.popleft()
        neighbours = [tuple_sum(direction, current) for direction in directions]
        for neighbour in neighbours:
            if neighbour in coords and neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
    perimeter = 0
    for coord in visited:
        counter = 0
        neighbours = [tuple_sum(direction, coord) for direction in directions]
        for neighbour in neighbours:
            if neighbour in visited:
                counter += 1
        perimeter += 4 - counter
    return visited, perimeter

#MAIN
with open("test.txt") as file:
    lines = file.read().splitlines()

grid, max_r, max_c = create_grid(lines)

price = 0
for region in grid.keys():
    while len(grid[region]) > 0:
        visited, perimeter = find_region_size_and_perimeter(grid[region])
        grid[region] = [item for item in grid[region] if item not in visited]
        price += len(visited) * perimeter
print("Part 1:", price)