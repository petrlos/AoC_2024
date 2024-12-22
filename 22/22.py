#Advent of Code 2024: Day 22
from collections import defaultdict

def step(number):
    number = ((number * 64) ^ number ) % 16777216
    number = ((number // 32) ^ number ) % 16777216
    number = ((number * 2048) ^ number ) % 16777216
    return number

#MAIN
with open("data.txt") as file:
    lines = file.read().splitlines()

part1 = 0
sequences = defaultdict(int)
for line in lines:
    number = int(line)
    prices = [number % 10] #last cipher from first price
    for i in range(2000): #generate 2000 numbers
        number = step(number)
        prices.append(number % 10) #store last cipher only
    part1 += number #check sum for part 1
    seq_buyer = set()
    for i in range(len(prices)-4): #find groups of five numbers
        a, b, c, d, e = prices[i: i+5]
        sequence = (b-a, c-b, d-c, e-d)
        if sequence not in seq_buyer: #when sequence not yet seen by buyer
            seq_buyer.add(sequence) #add to buyer
            sequences[sequence] += e #add to output

print("Part 1:", part1)
print("Part 2:", max(sequences.values())) #max value from all byuer from first occurence of sequence
