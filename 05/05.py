#Advent of Code 2024: Day 5
from icecream import ic
from collections import defaultdict

def parse_data(lines):
    rules = defaultdict(set)
    manuals = []
    lines = lines.split("\n\n")
    for line in lines[0].splitlines():
        rule = tuple(map(int, line.split("|")))
        key, value = rule
        rules[key].add(value)
    for line in lines[1].splitlines():
        manual = list(map(int, line.split(",")))
        manuals.append(manual)
    return rules, manuals

def check_pages_order(manual):
    for position, number in enumerate(manual):
        pages = rules[number]
        for page in pages:
            if page not in manual:
                continue
            else:
                if manual.index(page) < position:
                    return False
    return True

#MAIN
with open("test.txt") as file:
    lines = file.read()

rules, manuals = parse_data(lines)

check_sum = 0


for manual in manuals:
    if check_pages_order(manual):
        check_sum += manual[len(manual) // 2 ]
print(check_sum)