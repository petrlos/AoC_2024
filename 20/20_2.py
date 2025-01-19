#Advent of Code 2024: Day 20
from collections import deque

def check_shortcut(pair):
    c1, c2 = pair
    if c1 not in distances.keys() or c2 not in distances.keys():
        return -1
    return abs(distances[c1] - distances[c2])

#MAIN
with open("data.txt") as file:
    grid = file.read().splitlines()

for r in range(len(grid)):
    for c in range(len(grid[0])):
        if grid[r][c] == "S":
            start = (r, c)

queue = deque([start])
max_r = len(grid)
max_c = len(grid[0])
distances = {start: 0}

while queue:
    r, c = queue.popleft()
    for new_r, new_c in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
        if new_r not in range(max_r) or new_c not in range(max_c): continue
        if grid[new_r][new_c] == "#": continue
        if (new_r, new_c) in distances.keys(): continue
        queue.append((new_r, new_c))
        distances[(new_r, new_c)] = distances[(r, c)] + 1

result = 0
for r in range(max_r):
    for c in range(max_c):
        if grid[r][c] != "#": continue
        oposite_coords = [[(r + 1, c), (r - 1, c)], [(r, c + 1), (r, c - 1)]]
        for pair in oposite_coords:
            shortcut = check_shortcut(pair)
            if shortcut > 100:
                result += 1
print("Part 1:", result)

result = 0
for r in range(max_r):
    for c in range(max_c):
        if grid[r][c] == "#": continue
        for d_r in range(-20, 20 + 1):
            for d_c in range(-20 + abs(d_r), 20 - abs(d_r) + 1): #get all points in manhattan distance of max 20
                new_r = r + d_r
                new_c = c + d_c
                if (new_r, new_c) not in distances.keys(): continue
                #saved distance minus length of shortcut must be >= 100
                if distances[(new_r, new_c)] - distances[(r, c)] - (abs(d_c) + abs(d_r)) >= 100 :
                    result += 1
print("Part 2:", result)