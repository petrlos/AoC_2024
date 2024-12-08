from itertools import permutations
from icecream import ic
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
    #p2, p1 = point, p2
    return antinodes

#MAIN
with open("data.txt") as file:
    lines = file.read().splitlines()

max_r = len(lines[0])
max_c = len(lines)
grid = create_grid(lines)

result_part1 = set()
result_part2 = set()
for antena, coords in grid.items():
    if antena in ".#+":
        continue
    result_part1 |= find_antinodes(coords)
    result_part2 |= find_antinodes(coords)
    result_part2 |= coords

ic(len(result_part1))