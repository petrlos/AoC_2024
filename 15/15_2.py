#Advent of Code 2024: Day 15
from collections import deque

def parse_grid(lines):
    enlarge_grid = dict({"#":"##", ".":"..", "O":"[]", "@":"@."})
    r, c = 0, 0
    grid = []
    for line in lines.splitlines():
        grid_line = str()
        for char in line:
            grid_line += enlarge_grid[char]
        grid.append(list(grid_line))
    for i, line in enumerate(grid):
        if "@" in line:
            r, c = i, line.index("@")
    grid[r][c] = "."
    return grid, r, c

#MAIN
with open("data.txt") as file:
    lines = file.read().split("\n\n")

grid, r, c = parse_grid(lines[0])

directions = dict(zip("^v<>", [(-1,0), (1,0), (0,-1), (0,1)]))
for move in lines[1]:
    if move not in directions.keys(): #directions contains \n -> must be ignored
        continue
    r_or, c_or = r, c

    to_be_pushed = []
    dr, dc = directions[move]
    if grid[r+dr][c+dc] == "#":
        continue
    r, c = r + dr, c + dc
    if grid[r][c] == ".": #moves on empty place without pushing boxes
        pass
    elif move in "<>": #move left/right -> only one row of boxes would be pushed
        push_r, push_c = r, c
        while grid[push_r][push_c] in "[]":
            to_be_pushed.append((push_r, push_c))
            push_r, push_c = push_r + dr, push_c + dc
            if grid[push_r][push_c] == "#":
                c -= dc
                break
        if grid[push_r][push_c] == ".":
            for push in reversed(to_be_pushed):
                r, c = push
                grid[r+dr][c+dc] = grid[r][c]
            grid[r][c] = "."
    elif move in "v^": #move up/down -> may affect multiple boxes on more lines
        queue = deque([(r,c)])
        must_be_moved = []
        while queue:
            row, col = queue.pop()
            if grid[row][col] == "#": #move not possible - delete everything scanned and put robot back
                move = False
                queue = []
                must_be_moved = []
                r = r - dr
            elif grid[row][col] == "[":
                queue += [(row +dr, col), (row+dr, col+1)] #row in direction up/down, other half of the box left
                must_be_moved += [(row, col), (row, col+1)] #complete box to be moved
            elif grid[row][col] == "]":
                queue += [(row+dr, col), (row+dr, col-1)] #row in direction up/down, other half of the box right
                must_be_moved += [(row, col), (row, col-1)] #complete box to be moved
        if not move:
            continue
        if dr < 0: #move up
            must_be_moved = sorted(list(set(must_be_moved)))
            for row, col in must_be_moved:
                grid[row + dr][col] = grid[row][col]
                grid[row][col] = "."
        if dr > 0:
            must_be_moved = set(must_be_moved)
            sorted_data = sorted(must_be_moved, key=lambda x: (-x[0], -x[1]))
            for row, col in sorted_data:
                grid[row + dr][col] = grid[row][col]
                grid[row][col] = "."

#uncomment to print result grid
"""grid[r][c] = "@"
for line in grid:
    grid[r][c] = "@"
    print("".join(line))
grid[r][c] = "."
"""

gps = 0
for row, line in enumerate(grid):
    for col, char in enumerate(line):
        if char == "[":
            gps += 100* row + col
print("Part 2:",gps)