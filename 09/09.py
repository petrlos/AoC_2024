#Advent of Code 2024: Day 9
from icecream import ic
from dataclasses import dataclass
from datetime import datetime
time_start = datetime.now()

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

#Part1
print("Part 1:", compress_single_slots(line))
print("Runtime part 1:", datetime.now() - time_start)

#Part2
@dataclass
class f_g: #file and gap - easier to work with + mutable
    id: int
    size: int
    start: int

files = dict() #key = file id, value = size, start
gaps = list() #list is sorted from left to right, gaps may get size=0, will not be deleted, just skipped

locator = 0
for id, char in enumerate(line):
    if id % 2 == 0:
        files[id // 2] = f_g(start = locator, size = int(char), id = id//2)
    else:
        # id of gap not needed - 1 dataclass for both may be used
        gaps.append(f_g(start = locator, size=int(char), id=0))
    locator += int(char)

max_id = max(files.keys())

for id in range(max_id, -1, -1): #look through all files from right to left
    for gap in gaps: #look through all gaps from left to right
        if gap.size >= files[id].size: #if find a gap large enough
            gap.size -= files[id].size #make it smaller by file size
            files[id].start = gap.start #replace start of a file
            gap.start += files[id].size  #reindex start of a gap
            break #every file may be copied maximally once - dont look further
        if gap.start > files[id].start: #files cannot be moved to right
            break

result = 0
for id, file in files.items():
    result += id * sum(file.start + i for i in range(file.size))
print("Part 2:",result)

print("Total runtime:", datetime.now() - time_start)