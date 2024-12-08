from itertools import permutations
from collections import defaultdict

def create_grid(lines):
    grid = defaultdict(set)
    for r, line in enumerate(lines):
        for c, char in enumerate(line):
            grid[char].add((r,c))
            grid["+"].add((r,c)) #all points
    return grid

def find_antinodes(set_of_points):
    antinodes = set()
    pairs = set(permutations(set_of_points, 2))
    for pair in pairs:
        p1, p2 = pair
        point = (2 * p2[0] - p1[0], 2 * p2[1] - p1[1])
        if point in grid["+"]:
            antinodes.add(point)
    return antinodes

def find_antinodes_repeating(set_of_points):
    antinodes = set()
    pairs = set(permutations(set_of_points, 2))
    for pair in pairs:
        p1, p2 = pair
        while True:
            point = (2 * p2[0] - p1[0], 2 * p2[1] - p1[1])
            if point in grid["+"]:
                antinodes.add(point)
            else:
                break
            p2, p1 = point, p2
    return antinodes

#MAIN
with open("data.txt") as file:
    lines = file.read().splitlines()

grid = create_grid(lines)

result_part1 = set()
result_part2 = set()
for antena, coords in grid.items():
    if antena in ".#+": # "." = empty space, "#" = used for testing, "+" = all points in grid
        continue
    result_part1 |= find_antinodes(coords)
    result_part2 |= find_antinodes_repeating(coords)
    result_part2 |= coords

print("Part 1:", len(result_part1))
print("Part 2:", len(result_part2))