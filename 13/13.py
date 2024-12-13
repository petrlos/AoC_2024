#Advent of Code 2024: Day 13
import re
from icecream import ic
from sympy import symbols, Eq, solve

def check_block(block):
    a, d, b, e, c, f = list(map(int, re.findall(r"\d+", block)))
    x, y = symbols('x y')
    eq1 = Eq(a * x + b * y, c)
    eq2 = Eq(d * x + e * y, f)
    solution = solve((eq1, eq2), (x, y))
    results = [solution[x], solution[y]]
    result_ok = True
    for result in results:
        if result > 100 or int(result) != result:
            result_ok = False
    if result_ok:
        tokens = int(results[0]*3 + results[1])
    else:
        tokens = 0
    return tokens

#MAIN
with open("data.txt") as file:
    blocks = file.read().split("\n\n")

tokens_needed = 0
for block in blocks:
    tokens_needed += check_block(block)

print("Part 1:", tokens_needed)


