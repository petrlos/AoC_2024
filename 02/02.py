#Advent of code 2024: Day 2
from icecream import ic
import re

def parse_input(lines):
    numbers = []
    for line in lines:
        numbers.append((list(map(int, (re.findall(r"\d+", line))))))
    return numbers

def safe_part1(numbers):
    #all numbers must be in order + max difference of 3
    if numbers == sorted(numbers, reverse=True) or numbers == sorted(numbers):
        for i in range(len(numbers)-1):
            if abs(numbers[i] - numbers[i+1]) > 3 or numbers[i] == numbers[i+1]:
                return False
        return True

def safe_part2(numbers):
    #leave out one number from list and check with part1 function
    for i in range(len(numbers)):
        one_out = numbers[:i] + numbers[i+1:]
        if safe_part1(one_out):
            return True
    return False

#MAIN
with open("data.txt") as file:
    lines = file.read().splitlines()

data = parse_input(lines)

counter_part1 = 0
counter_part2 = 0
for nums in data:
    if safe_part1(nums):
        counter_part1 += 1
    else:
        #not safe for part1? check part2
        if safe_part2(nums):
            counter_part2 += 1

print("Part 1:", counter_part1)
print("Part 2:", counter_part1+counter_part2)