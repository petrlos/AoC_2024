#Advent of Code 2024: Day 11
from icecream import ic
from collections import defaultdict
from datetime import datetime
time_start = datetime.now()

def brute_blink(stones):
    new_stones = []
    for stone in stones:
        if stone == "0":
            new_stones.append("1")
        elif len(stone) % 2 == 0:
            l = len(stone)
            left, right = stone[:l //2], stone[l//2:]
            new_stones += [left]+[str(int(right))]
        else:
            new_stones.append(str(int(stone)*2024))
    return new_stones

def blink(repeats, line):
    stones = defaultdict(int)
    for num in line.split(" "):
        stones[num] += 1 #basic setup
    for i in range(repeats):
        new_stones = defaultdict(int)
        for stone, count in stones.items():
            if stone == "0":
                stones["0"] = 0 #all stones with this number are consumed
                new_stones["1"] += count #and create a new stone(stones eventually)
            elif len(stone) % 2 == 0:
                l = len(stone)
                left, right = stone[:l // 2], stone[l // 2:]
                stones[stone] = 0
                new_stones[left] += count
                new_stones[str(int(right))] += count
            else:
                stones[stone] = 0
                new_stones[str(int(stone) * 2024)] += count
        stones.update(new_stones)
    return sum(stones.values())

#MAIN
with open("data.txt") as file:
    line = file.read()

stones = line.split(" ")

for i in range(25):
    stones = brute_blink(stones)
print("Part 1 brute force:", len(stones))
print("Runtime: ", datetime.now() - time_start)
print(" ")

for id, repeat in enumerate([25,75]):
    time_start = datetime.now()
    print(f"Part {id+1}:", blink(repeat, line))
    print("Runtime:", datetime.now() - time_start)