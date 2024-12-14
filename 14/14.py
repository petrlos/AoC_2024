#Advent of Code 2024: Day 14
import re
from icecream import ic
from math import prod
from collections import Counter, defaultdict
from dataclasses import dataclass

def print_grid(robots):
    c_robots = Counter(robots)
    for row in range(r_max):
        for col in range(c_max):
            if (row, col) in robots:
                print(c_robots[(r,c)], end="")
            else:
                print(".", end="")
        print(" ")
    print(" ")

def move_part1(lines, r_max, c_max):
    sectors = defaultdict(int)
    for line in lines:
        c, r, dc, dr = list(map(int, (re.findall(r"-?\d+", line))))
        for i in range(100):
            r = (r + dr) % r_max
            c = (c + dc) % c_max
        r = r - r_max // 2 #correct row by 1/2 size of a grid upwards
        c = c - c_max // 2 #correct col by 1/2 size of a grid left
        if c == 0 or r == 0: #lies in the middle
            continue
        c = c // abs(c) #leave only sign: +1 or -1
        r = r // abs(r)
        sectors[(r,c)] += 1
    return prod(sectors.values())

#MAiN

with open("test.txt")as file:
    lines = file.read().splitlines()
print(move_part1(lines, 7,11))

with open("data.txt")as file:
    lines = file.read().splitlines()
print(move_part1(lines, 103,101))
