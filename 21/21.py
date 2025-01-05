#Advent of Code 2024: Day 21
from datetime import datetime
from collections import deque
from itertools import product
timestart = datetime.now()

def bfs(first, second, keyboard):
    result = []
    queue = deque([[keyboard[first], "", set()]])
    min_length = 100

    while queue:
        (r, c), path, seen = queue.popleft()
        if first == second: return ["A"]
        seen.add((r,c))
        for r, c, p in [(r-1, c, "^"), (r, c-1, "<"), (r+1, c, "v"), (r, c+1, ">")]:
            if (r, c) not in keyboard.values(): continue
            if (r, c) in seen: continue
            if keyboard[second] == (r,c):
                if min_length >= len(path + p):
                    min_length = len(path + p + "A")
                    result.append(path + p + "A")
            else:
                queue.append([(r, c), path + p, seen])
    return result

def generate_paths(keyb):
    #generate all possible paths between all buttons on a keyboard
    keyboard = {}
    paths = dict()
    for r, line in enumerate(keyb):
        for c, char in enumerate(line):
            if char == None: continue
            keyboard[char] = (r,c)
    for first in keyboard.keys():
        for second in keyboard.keys():
            paths[(first, second)] = bfs(first, second, keyboard)
    return paths

def solve_path(path, path_keyboard):
    #generate all paths for input number/arrows
    result = []
    for first, second in zip("A" + path, path):
        result.append(path_keyboard[(first, second)])
    return ["".join(x) for x in list(product(*result))]

#MAIN
with open("data.txt") as file:
    lines = file.read().splitlines()

#keyboards
num_keyboard = [["7", "8", "9"], ["4","5","6"], ["1", "2" ,"3"], [None, "0","A"]] #(3,2)
directional_keyboard = [[None, "^", "A"], ["<", "v", ">"]] #(0,2)

#generate all possible paths between all buttons on both keyboards
paths_nums = generate_paths(num_keyboard)
paths_arrows = generate_paths(directional_keyboard)

check_sum = 0
for num in lines:
    paths = solve_path(num, paths_nums) #decode number to directional keyboard
    second = []
    for path in paths: #decode first keyoboard to directional keyboard
        second += solve_path(path, paths_arrows)
    minlen = min(map(len, second))
    second = [path for path in second if len(path) == minlen] #only shortest paths are valid
    third = []
    for path in second: #repeat
        third += solve_path(path, paths_arrows)
    minlen = min(map(len, third))
    second = [path for path in third if len(path) == minlen]
    print(f"For {num} is minimal length: {minlen}.")
    check_sum += minlen * int(num[:-1])

print(" ")
print("Part 1:", check_sum)
print("Total runtime:", datetime.now() - timestart)