#Advent of Code 2024: Day 15
from icecream import ic

def create_grid(lines):
    grid = dict()
    robot = (0,0)
    lines = lines.splitlines()
    for r, line in enumerate(lines):
        for c, char in enumerate(line):
            if char in ".O":
                grid[(r,c)] = char
            if char == "@":
                robot = (r,c)
                grid[(r,c)] = "."
    max_r, max_c = len(lines[0]), len(lines)
    return grid, robot, max_r, max_c

def print_grid(grid, max_r, max_c):
    for r in range(max_r):
        for c in range(max_c):
            if (r,c) in grid.keys():
                print(grid[(r,c)], end="")
            else:
                print("#", end="")
        print("")

def count_gps(grid):
    return sum(coord[0] * 100 + coord[1] for coord, item in grid.items() if item == "O")

#MAIN
with open("data.txt") as file:
    lines = file.read().split("\n\n")

grid, robot, max_r, max_c = create_grid(lines[0])
print_grid(grid, max_r, max_c)
directions = dict(zip("^v<>", [(-1,0), (1,0), (0,-1), (0,1)]))

for step in lines[1]:
    if step not in directions.keys():
        continue
    dr, dc = directions[step]
    move_possible = False
    steps = list()
    current = robot
    while True:
        next = (current[0] + dr, current[1] + dc) #look onto next step
        if next not in grid.keys(): #out of grid - stop
            break
        if grid[next] == ".": # free space
            move_possible = True
            steps.append(next)
            break
        else:
            steps.append(next) #no free space/not out of grid
            current = next #look further
    if move_possible:
        grid[steps[-1]], grid[steps[0]] = grid[steps[0]], grid[steps[-1]] # "@OO." -> ".@00"
        robot = steps[0] #move robot

print("Part 1:", count_gps(grid))