#Advent of Code 2024: Day 24
from icecream import ic
from collections import deque

#MAIN
with open("data.txt") as file:
    inputs, rules = file.read().split("\n\n")

numbers = dict()

for input in inputs.splitlines():
    key, value = input.split(": ")
    numbers[key] = int(value)

rules = deque(rules.splitlines())

while rules:
    current = rules.popleft()
    left, right = current.split(" -> ")
    val1 = left[:3]
    val2 = left[-3:]
    if val1 not in numbers.keys() or val2 not in numbers.keys():
        rules.append(current)
        continue
    if "AND" in left:
        numbers[right] = numbers[val1] & numbers[val2]
    elif " OR" in left:
        numbers[right] = numbers[val1] or numbers[val2]
    elif "XOR" in left:
        numbers[right] = numbers[val1] ^ numbers[val2]

result = ["0"]*50
for key,value in (numbers.items()):
    if "z" in key:
        result[-int(key[1:])-1] = str(value)

result = "".join(result)
print("Part 1:",int(result, 2))