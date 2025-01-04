#Advent of Code 2024: Day\21

from collections import defaultdict
import heapq

#Advent of Code 2024: Day 21
def find_path(keyboard, code):
    directions = {">":(0,1), "<":(0,-1), "^":(-1,0), "v":(1,0)}
    start, *keyboard_list = keyboard
    keyboard = dict()
    decode = defaultdict(str)
    for r, line in enumerate(keyboard_list):
        for c, char in enumerate(line):
            if char == None:
                continue
            keyboard[(r,c)] = char
            decode[char] = (r,c)
    path = ""
    for char in code:
        visited = dict({start: 0})
        queue = []
        heapq.heappush(queue, [0, path, start])
        if char == keyboard[start]:
            path += "A"
            continue
        while queue:
            cost, path, coords = heapq.heappop(queue)
            for dir, delta_coords in directions.items():
                dr, dc = delta_coords
                r, c = coords
                r += dr
                c += dc
                if decode[char] == (r,c):
                    queue = []
                    path += dir + "A"
                    break
                elif (r, c) in keyboard.keys():
                    if len(path) > 0:
                        if path[-1] != dir:
                            cost += 100
                    if (r,c) not in visited.keys():
                        visited[(r,c)] = cost
                        heapq.heappush(queue, [cost, path+dir, (r,c)])
                    elif visited[(r,c)] > cost:
                        visited[(r,c)] = cost
                        heapq.heappush(queue, [cost, path+dir, (r,c)])
        print(visited)
        start = decode[char]
    return path

with open("test.txt") as file:
    lines = file.read().splitlines()

print(lines)

#define keyboard: start, list of buttonrows
keyb_nums = [(3,2), ["7", "8", "9"], ["4","5","6"], ["1", "2" ,"3"], [None, "0","A"]]
keyb_arrows = [(0,2), [None, "^", "A"], ["<", "v", ">"]]

result = find_path(keyb_arrows, "v<<A>>^A<A>AvA<^AA>A<vAAA>^A")

print(result)
print("<vA<AA>>^AvAA<^A>A<v<A>>^AvA^A<vA>^A<v<A>^A>AAvA^A<v<A>A>^AAAvA<^A>A")
print(result == "<vA<AA>>^AvAA<^A>A<v<A>>^AvA^A<vA>^A<v<A>^A>AAvA^A<v<A>A>^AAAvA<^A>A")
