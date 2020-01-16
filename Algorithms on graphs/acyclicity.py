#Uses python3

# Problem Description: Task: Check whether a given directed graph with n vertices and m edges contains a cycle.
# Input Format: A graph is given in the standard format.
# Output Format: Output 1 if the graph contains a cycle and 0 otherwise
# Memory Limit: 512MB
# Sample 1: Input: 4 4
#                  1 2
#                  4 1
#                  2 3
#                  3 1
#           Output: 1
# Explanation: This graph contains a cycle 3 --> 1 --> 2 --> 3
# Sample 2: Input: 5 7
#                  1 2
#                  2 3
#                  1 3
#                  3 4
#                  1 4
#                  2 5
#                  3 5
#            Output: 0


import sys
def Explore(node, adj, key, visited):
    if key in adj[node]:
        return True
    for vertex in adj[node]:
        if vertex not in visited:
            if Explore(vertex, adj, key, visited):
                return True
    return False


def acyclic(adj): # for each node check whether it's visited, if whether the vertices the node has direction to are visited
    visited = [] # if not use Explore on this node
    for key in adj.keys():
        if key not in visited:
            visited.append(key)
            for node in adj[key]:
                if node not in visited:
                    if Explore(node, adj, key, visited):
                        return 1
    return 0

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = {}
    for i in range(n): # for each node make it's list of nodes that this node has edge to
        adj[i+1] = []
    for (a, b) in edges:
        adj[a].append(b)
    print(acyclic(adj))
