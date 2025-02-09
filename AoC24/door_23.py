import networkx as nx
from itertools import combinations


with open("../inputs.txt") as f:
    puzzle = f.read().splitlines()
    puzzle = [(line.split("-")[0], line.split("-")[1]) for line in puzzle]

def part1(puzzle):
    count = 0
    G = nx.DiGraph()
    G.add_edges_from(puzzle)
    #print("Number of nodes: ", G.number_of_nodes())
    # print all nodes
    #print("Nodes: ", G.nodes)
    # print all nodes with exactly two adjacent nodes
    #print(G.nodes)
    # filter all nodes which are starting with charachter 't'
    #print("FILTERED")
    nodes_t = [node for node in G.nodes if node.startswith('t')]
    #print(G.neighbors('ta'))
    #print(list(nx.all_neighbors(G, 'ta')))
    #neighbours = list(nx.all_neighbors(G, 'ta'))
    # check if these nodes are connected ['de', 'kh', 'co', 'ka']
    all_inter_graphs = []
    for n_t in nodes_t:
        neighbours = list(nx.all_neighbors(G, n_t))
        interconnected_graphs = []
        #print("T Node", n_t)
        for n in neighbours:
            neighbours_sub = list(nx.all_neighbors(G, n))
            for n2 in neighbours:
                if n2 in neighbours_sub:
                    interconnected_graphs.append(n)
                    interconnected_graphs.append(n2)
        interconnected = list(set(interconnected_graphs))
        print("Interconnected graphs: ", interconnected)
        for j, i in enumerate(range(len(interconnected)), 1):
            if j == len(interconnected):
                break
            if (n_t, interconnected[i], interconnected[j]) not in all_inter_graphs:
                all_inter_graphs.append((n_t, interconnected[i], interconnected[j]))

    count += len(all_inter_graphs)
    return count



def part2(puzzle):
    pass

print(puzzle)

print("Part 1: ", part1(puzzle))
# 239 too low