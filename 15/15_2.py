#Advent of Code 2024: Day 15
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
with open("test_3.txt") as file:
    lines = file.read().split("\n\n")

grid, r, c = parse_grid(lines[0])

directions = dict(zip("^v<>", [(-1,0), (1,0), (0,-1), (0,1)]))
for move in lines[1]:
    to_be_pushed = []
    dr, dc = directions[move]
    r, c = r + dr, c + dc
    if grid[r][c] == ".": #moves on empty place withnout pushing boxes
        continue
    elif move in "<>": #move left/right -> only one row of boxes would be pushed
        push_r, push_c = r, c
        while grid[push_r][push_c] in "[]":
            to_be_pushed.append((push_r, push_c))
            push_r, push_c = push_r + dr, push_c + dc
            if grid[push_r][push_c] == "#":
                break
        if grid[push_r][push_c] == ".":
            for push in reversed(to_be_pushed):
                r, c = push
                grid[r+dr][c+dc] = grid[r][c]
            grid[r][c] = "."
    elif move in "v^": #move up/down -> may affect multiple boxes on more lines
        ...