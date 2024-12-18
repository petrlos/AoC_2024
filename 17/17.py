#Advent of Code 2024: Day 17
import re

def combo(id):
    if id in [0,1,2,3]:
        return id
    elif id == 4:
        return a
    elif id == 5:
        return b
    elif id == 6:
        return c

def parse_data(lines):
    a, b, c, *program = list(map(int, (re.findall(r"\d+", lines))))
    return a, b, c, program

#MAIN
with open("data.txt") as file:
    lines = file.read()

a, b, c, program = parse_data(lines)
output = []

print (a, b, c, program)

pointer = 0
while pointer < len(program):
    operation = program[pointer]
    operand = program[pointer+1]

    if operation == 0: #adv
        a = a // 2 ** combo(operand)
    elif operation == 1: #bxl
        b = b ^ operand
    elif operation == 2: #bst
        b =  combo(operand) % 8
    elif operation == 3: #jnz
        if a != 0:
            pointer = operand
            continue
    elif operation == 4: #bxc
        b = b ^ c
    elif operation == 5: #out
        output.append(str(combo(operand) % 8))
    elif operation == 6: #bdv
        b = a // 2 ** combo(operand)
    elif operation == 7: #cdv
        c = a // 2 ** combo(operand)
    pointer += 2

print(",".join(output))