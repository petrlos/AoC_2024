#Advent of Code 2024: Day 19
import heapq

def check_design(design):
    queue = []
    heapq.heappush(queue, [len(design), design])
    while queue:
        current = heapq.heappop(queue)[1]
        for pattern in patterns:
            if current.startswith(pattern):
                new = current[len(pattern):]
                if len(new) == 0:
                    return True
                else:
                    heapq.heappush(queue, [len(new), new])
    return False

#MAIN
with open("data.txt") as file:
    patterns, designs= file.read().split("\n\n")

patterns = set(patterns.split(", "))
designs = set(designs.split("\n"))

counter = 0
for design in designs:
    counter += check_design(design)
print("Part 1:",counter)