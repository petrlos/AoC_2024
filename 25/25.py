#Advent of Code 2024: Day 25

def check_pair(key, lock):
    for slot in zip(key, lock):
        if sum(slot) > 5:
            return False
    return 1

#MAIN
with open("data.txt") as file:
    blocks = file.read().split("\n\n")

keys = set()
locks = set()

for block in blocks:
    data = block.splitlines()
    rotated = ["".join(chars) for chars in zip(*data)]
    count = tuple(x.count("#") - 1 for x in rotated)
    if "#" in data[0]:
        locks.add(count)
    else:
        keys.add(count)

counter = 0
for key in keys:
    for lock in locks:
        counter += check_pair(key, lock)

print("Part 1:",counter)