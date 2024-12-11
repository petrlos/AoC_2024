#Advent of Code 2024: Day 11
from icecream import ic
from collections import defaultdict

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

def blink(stones):
    new_stones = defaultdict(int)
    for stone, count in stones.items():
        news = solve_single_stone(stone)
        for new in news:
            new_stones[new] += count
    return new_stones

def solve_single_stone(stone):
    result = []
    if stone == "0":
        result.append("1")
    elif len(stone) % 2 == 0:
        l = len(stone)
        left, right = stone[:l // 2], stone[l // 2:]
        result += [left] + [str(int(right))]
    else:
        result.append(str(int(stone) * 2024))
    return result


with open("data.txt") as file:
    line = file.read()

stones = line.split(" ")

for i in range(25):
    stones = brute_blink(stones)
print(len(stones))

stones = defaultdict(int)
for num in line.split(" "):
    stones[num] += 1

for i in range(75):
    ic(i, len(stones))
    for number, count in stones.items():
        new_stones = blink(stones)
    stones = new_stones

ic(sum(stones.values()))
