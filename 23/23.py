#Advent of Code 2024: Day 23
from collections import defaultdict
import networkx as nx

def part1_and_part2_using_networkx(lines):
    print("Solutions using NetworkX:")
    G = nx.Graph() #initialize graph
    for line in lines:
        left, right = line.split("-")
        G.add_edge(left, right)

    # clique - a subgraph, where each node is connected to each node

    parties = nx.enumerate_all_cliques(G) #find all cliques in graph
    triplets = list()
    largest_party = list()
    for party in parties:
        if len(party) == 3 and any(node.startswith("t") for node in party):
            triplets.append(sorted(party))
        if len(party) > len(largest_party):
            largest_party = party

    print("Part 1:", len(triplets))
    print("Part 2:", ",".join(sorted(largest_party)))

    #view saved jpg file to visualize graph - captured after opening graph.html
    """# --- Use Pyvis for interactive visualization ---
    net = Network(notebook=True)  # If you're using Jupyter notebook
    net.from_nx(G)  # Convert NetworkX graph to Pyvis format

    # Optional: Set physics to False if you don't want auto-positioning
    net.force_atlas_2based()  # For better layout
    net.show("graph.html")  # Saves and opens an interactive HTML visualization
    """

#MAIN
with open("data.txt") as file:
    lines = file.read().splitlines()

connections = defaultdict(set)
counter = 0
for line in lines:
    counter += 1
    left, right = line.split("-")
    connections[left].add(right)
    connections[right].add(left)

triplets = set()
for first in connections.keys():
    for second in connections[first]:
        for third in connections[second]:
            if first in connections[third]:
                triplet = ",".join(sorted([first, second, third]))
                if first[0] == "t" or second[0] == "t" or third[0] == "t":
                    triplets.add(triplet)
print("Part 1:", len(triplets))

print(" ")
part1_and_part2_using_networkx(lines)