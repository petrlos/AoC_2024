#Advent of Code 2024: Day 14
import re
from math import prod
from collections import Counter, defaultdict

def print_grid(robots, r_max, c_max):
    for row in range(44, r_max-24): #constraints tested manually, so that output looks nice for my data
        for col in range(30, c_max-10):
            if (row, col) in robots:
                print("*", end="")
            else:
                print(".", end="")
        print(" ")
    print(" ")

def move_part1(lines, r_max, c_max, repeats):
    sectors = defaultdict(int)
    robots = set()
    for line in lines:
        c, r, dc, dr = list(map(int, (re.findall(r"-?\d+", line))))
        for i in range(1,repeats):
            r = (r + dr) % r_max
            c = (c + dc) % c_max
        robots.add((r,c))
        r = r - r_max // 2 #correct row by 1/2 size of a grid upwards
        c = c - c_max // 2 #correct col by 1/2 size of a grid left
        if c == 0 or r == 0: #lies in the middle
            continue
        c = c // abs(c) #leave only sign: +1 or -1
        r = r // abs(r)
        sectors[(r,c)] += 1
    if repeats == 7372:
        print("Part 2 ", i)
        print_grid(robots, r_max, c_max)
    return prod(sectors.values())

#MAiN
with open("data.txt")as file:
    lines = file.read().splitlines()
print("Part 1:",move_part1(lines, 103,101, repeats=101)) #101 because cycle starts at 1

#after 58 iterations appears a horizontal stripe every 103 more steps
#tested manually from 5000 iterations to find a tree
#7371 is a correct answer for my data
move_part1(lines, 103,101, repeats=7372)
