#Advent of Code 2024: Day 1
from icecream import ic
from collections import Counter

def parse_data(lines):
    left, right = [], []
    for line in lines:
        l, r = line.split()
        left.append(int(l))
        right.append(int(r))
    return left, right

def part1_compare(left, right):
    result = 0
    for l, r in zip(sorted(left), sorted(right)):
        result += abs(l-r)
    return result

def part2_multiply(left, right):
    result = 0
    count_right = Counter(right)
    for num in left:
        if num in count_right:
            result += count_right[num]*num
    return result

#MAIN
with open("data.txt") as file:
    lines = file.read().splitlines()

left, right = parse_data(lines)

print(f"Part 1:{part1_compare(left, right)}")
print(f"Part 2:{part2_multiply(left, right)}")