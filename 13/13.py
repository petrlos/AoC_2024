#Advent of Code 2024: Day 13
import re
from sympy import symbols, Eq, solve

def check_block(block, part):
    a, d, b, e, c, f = list(map(int, re.findall(r"\d+", block)))
    x, y = symbols('x y')
    c += part
    f += part
    eq1 = Eq(a * x + b * y, c)
    eq2 = Eq(d * x + e * y, f)
    solution = solve((eq1, eq2), (x, y))
    results = [solution[x], solution[y]]
    result_ok = True
    for result in results:
        if int(result) != result:
            result_ok = False
        if part == 0 and result > 100:
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
for id, i in enumerate([0, 10000000000000]):
    tokens_needed = 0
    for block in blocks:
        tokens_needed += check_block(block, i)
    print(f"Part {id+1}: {tokens_needed}")