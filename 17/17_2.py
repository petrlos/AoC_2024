#Advent of code 2024: Day 17 Part 2

def program(a):
    output = []
    while a != 0:
        b = a % 8
        b = b ^ 1
        c = a // 2 ** b
        b = b ^ c
        a = a // (2 ** 3)
        b = b ^ 6
        b = b % 8
        output.append(str(b))
    return ",".join(output)

check_program = "2,4,1,1,7,5,4,0,0,3,1,6,5,5,3,0"

a = 247839653009594
for start in range(-1024, 1024):
    result = program(a + start)
    if check_program.endswith(result):
        print(f"{a + start}: {result}")

#for the first number a == 0 at the end -> must be in (0..7)
#next numbers are always previous *8, mostly returns more results -> take the lowest
#by dead-end move back and check the step with more numbers the next one