#Advent of code 2024: Day 2
from icecream import ic
import re

def parse_input(lines):
    numbers = []
    for line in lines:
        numbers.append((list(map(int, (re.findall(r"\d+", line))))))
    return numbers

def safe_part1(numbers):
    if numbers == sorted(numbers, reverse=True) or numbers == sorted(numbers):
        for i in range(len(numbers)-1):
            if abs(numbers[i] - numbers[i+1]) > 3 or numbers[i] == numbers[i+1]:
                return False
        return True

#MAIN
with open("data.txt") as file:
    lines = file.read().splitlines()

numbs = parse_input(lines)

counter = 0
for num in numbs:
    if safe_part1(num):
        counter += 1
print("Part 1:", counter)
