#Advent of Code 2024: Day 20
from collections import deque
from datetime import datetime
from collections import Counter
from icecream import ic
time_start = datetime.now()

def parse_grid(lines):
    path = set()
    walls = set()
    start = ex = (0,0)
    for r, line in enumerate(lines[1:-1]):
        for c, char in enumerate(line[1:-1]):
            if char == ".": path.add((r,c))
            elif char == "#": walls.add((r,c))
            elif char == "S":
                start = (r,c)
            elif char == "E":
                path.add((r,c))
                ex = (r,c)
            else: raise ValueError("Unknow character")
    return start, ex, path, walls

def find_path(path, added):
    visited = {start: 0}
    queue = deque([start])
    path.add(added)
    while queue:
        r, c = queue.popleft()
        for nr, nc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
            if (nr, nc) in path:
                if (nr, nc) not in visited.keys():
                    queue.append((nr, nc))
                    visited[(nr, nc)] = visited[r, c] + 1
    path.remove(added)
    return visited[ex]

#MAIN
with open("data.txt") as file:
    lines = file.read().splitlines()

start, ex, path, walls = parse_grid(lines)

queue = deque([start])

saved = []
full_path = find_path(path, (-1, -1))

print(len(walls))

for id, added in enumerate(walls):
    saved.append(full_path - find_path(path, added))
    if id % 200 == 0:
        print(id)

#extreme slow, dont use it :)
result = list(filter(lambda x:  x>=100, saved))
print("Path 1:", len(result))