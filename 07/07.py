#Advent of Code 2024: Day 7
from itertools import combinations

from icecream import ic

def check_operators_part1(result, operators):
    operators = list(map(int, operators.split(" ")))
    combinations = 2**(len(operators)-1)
    for comb in range(combinations):
        check = operators[0]
        combination = bin(comb)[2:]
        combination = (len(operators) - len(combination)-1) * "0" + combination
        for oper, num in zip(combination, operators[1:]):
            if oper == "0":
                check += num
            else:
                check *= num
        if check == result:
            return True
    return False

with open("data.txt") as file:
    lines = file.read().splitlines()

counter_part1 = 0
for line in lines:
    result, operators = line.split(": ")
    if check_operators_part1(int(result), operators):
        counter_part1 += int(result)
print(counter_part1)