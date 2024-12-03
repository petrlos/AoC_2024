#Advent of Code 2024: Day 3
import re
from icecream import ic

def sum_up(where):
    reg = re.compile(r"mul(\(\d+),(\d+)\)")
    numbers = reg.findall(where)
    sum_up = 0
    for numb in numbers:
        first, second = numb
        sum_up += int(first[1:]) * int(second)
    return sum_up

#MAIN
with open("data.txt") as file:
    line = file.read()

#Part1
part1 = sum_up(line)
print("Part 1:", part1)

#Part2
lines = line.split("don't")
result = sum_up(lines[0]) #sum up first line - that is always do
for line in lines[1:]:
    position = line.find("do")
    if position > 0: #ignore everything until first do
        result += sum_up(line[position:])

print("Part 2:", result)