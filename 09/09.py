#Advent of Code 2024: Day 9
from icecream import ic

def get_checksum(result):
    return sum(id * int(char) for id, char in enumerate(result))

def control_sum(file_system):
    file_system = file_system.replace(".", "")
    return sum(int(char) for char in file_system)

#MAIN
with open("data.txt") as file:
    line = file.read()


file_system = list()
for id, char in enumerate(line):
    if id % 2 == 0:
        file_system.extend([str(id // 2)]*int(char))
    else:
        file_system += ["."]*int(char)


compressed_file_system = list()
id = 0
while len(compressed_file_system) < len(file_system):
    char = file_system[id]
    if char == ".":
        if file_system[-1] == ".":
            char = "."
        else:
            char = file_system[-1]
        file_system = file_system[:-1]
    if char != ".":
        compressed_file_system.append(char)
        id += 1

ic(get_checksum(compressed_file_system))