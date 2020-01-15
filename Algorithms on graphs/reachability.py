#Uses python3

# Problem: Finding an Exit from a Maze 
# Problem introduction: A maze is a rectangular grid of cells with walls between some of adjacent cells. You would like to check whether
# there is a path from a given cell to a given exit from a maze where an exit is also a cell that lies on the border of the maze
# (in the example shown to the right there are two exits: one on the left border and one on the right border). For this, you represent
# the maze as an undirected graph: vertices of the graph are cells of the maze, two vertices are connected by an undirected edge if they
# are adjacent and there is no wall between them. Then, to check whether there is a path between two given cells in the maze, it
# suffices to check that there is a path between the corresponding two vertices in the graph.
# Problem Description: Given an undirected graph and two distinct vertices u and v, check if there is a path between u and v.
# Input Format: An undirected graph with n vertices and m edges. The next line contains two vertices u and v of the graph.
# Constraints: 2 ≤ n ≤ 103; 1 ≤ m ≤ 103; 1 ≤ u,v ≤ n; u ̸= v.
# Output Format: Output 1 if there is a path between u and v and 0 otherwise. 
# Memory Limit: 512MB
# Sample 1: Input: 4 4
#                  1 2
#                  3 2
#                  4 3
#                  1 4
#                  1 4 
#          Output: 1
# Explanation: In this graph, there are two paths between vertices 1 and 4: 1-4 and 1-2-3-4.
# Example:        1----2
#                 |    |
#                 |    |
#                 |    |
#                 4----3
# Sample 2: Input: 4 2
#                  1 2
#                  3 2
#                  1 4 
#          Output: 0

import sys

def Explore(node, adjacency_map, y, visited):
    if node not in visited: # if node is visited - not need to do anything again
        visited.append(node)
        if y in adjacency_map[node]:
            return True
        else:
            for node in adjacency_map[node]: # check the same way recursively
                if Explore(node, adjacency_map, y, visited):
                    return True
            return False
    else:
        return False
def reach(adj, x, y):
    if len(adj[x]) == 0: # if there are no hashes of either x or y, return 0
        return 0
    if len(adj[y]) == 0:
        return 0
    if y in adj[x]: # here check whether y in x's hashes, if not then at least know that x has been visited, and check the rest of x's hashes
        return 1
    nodes_to_check_from = [i for i in adj[x]]
    visited = [x]
    for node in nodes_to_check_from: # check each possible edge between x's hashes
        if Explore(node, adj, y, visited): 
            return 1
    return 0

def make_edge(x, y, adjacency_map):
    if y not in adjacency_map[x]:
        adjacency_map[x].append(y)

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    x, y = data[-2], data[-1]
    adjacency_map = {}
    for i in range(n):
        adjacency_map[i+1] = [] # for each node create empty list as a hash to this node
    for a, b in edges: # make edges in both ways
        make_edge(a, b, adjacency_map)
        make_edge(b, a, adjacency_map)
    print(reach(adjacency_map, x, y))


