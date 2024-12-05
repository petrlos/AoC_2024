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

def bubble_sort(manual):
    #kind of bubble sort, probably not working generally, for this AoC is ok
    i = 0
    while i < len(manual)-1:
        first, second = manual[i], manual[i+1]
        if first in rules[second]:
            manual[i], manual [i+1] = manual[i+1], manual[i]
            i = 0
        else:
            i += 1
    return manual[len(manual) //2]

#MAIN
with open("data.txt") as file:
    lines = file.read()

rules, manuals = parse_data(lines)

check_sum = 0
wrong_manuals = list()

for manual in manuals:
    if check_pages_order(manual):
        check_sum += manual[len(manual) // 2 ]
    else:
        wrong_manuals.append(manual) #save for part 2
print("Part 1:", check_sum)

check_sum = 0
for manual in wrong_manuals:
     check_sum += bubble_sort(manual) #function returns middle position of sorted list
print("Part 2:",check_sum)