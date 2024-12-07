#Advent of Code 2024: Day 7
from itertools import product
from datetime import datetime
time_start = datetime.now()

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

def check_operators_part2(result, operators):
    operators = operators.split(" ")
    combinations = list(product(range(3), repeat=(len(operators)-1)))
    for combination in combinations:
        check = operators[0]
        for oper, num in zip(combination, operators[1:]):
            if oper == 0:
                check = str(int(check) + int(num))
            elif oper == 1:
                check = str(int(check) * int(num))
            elif oper == 2:
                check += num #ads string
        if check == result:
            return True
    return False

#MAIN
with open("data.txt") as file:
    lines = file.read().splitlines()

counter_part1 = 0
counter_part2 = 0
for line in lines:
    result, operators = line.split(": ")
    if check_operators_part1(int(result), operators):
        counter_part1 += int(result)
    else:
        if check_operators_part2(result, operators):
            counter_part2 += int(result)

print("Part 1:", counter_part1)
print("Part 2:", counter_part1+counter_part2)
print("Runtime: ", datetime.now() - time_start)