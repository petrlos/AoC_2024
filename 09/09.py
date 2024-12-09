#Advent of Code 2024: Day 9
from icecream import ic

def get_checksum(result):
    return sum(id * int(char) for id, char in enumerate(result))

def compress_single_slots(line):
    file_system = list()
    for id, char in enumerate(line):
        if id % 2 == 0:
            file_system.extend([str(id // 2)] * int(char))
        else:
            file_system += ["."] * int(char)

    compressed_file_system = list()
    id = 0
    while len(compressed_file_system) < len(file_system):
        char = file_system[id]
        if char == ".":
            if file_system[-1] == ".":
                char = "."
            else:
                char = file_system[-1]
            file_system.pop(-1)
        if char != ".":
            compressed_file_system.append(char)
            id += 1
    return get_checksum(compressed_file_system)

#MAIN
with open("data.txt") as file:
    line = file.read()

print("Part 1:", compress_single_slots(line))