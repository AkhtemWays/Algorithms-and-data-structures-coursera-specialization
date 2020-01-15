#Uses python3

import sys


def Explore(node, adjacency_map, y, visited):
    if node not in visited:
        visited.append(node)
        if y in adjacency_map[node]:
            return True
        else:
            for node in adjacency_map[node]:
                if Explore(node, adjacency_map, y, visited):
                    return True
            return False
    else:
        return False
def reach(adj, x, y):
    if len(adj[x]) == 0:
        return 0
    if len(adj[y]) == 0:
        return 0
    if y in adj[x]:
        return 1
    nodes_to_check_from = [i for i in adj[x]]
    visited = [x]
    for node in nodes_to_check_from:
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
        adjacency_map[i+1] = []
    for a, b in edges:
        make_edge(a, b, adjacency_map)
        make_edge(b, a, adjacency_map)
    print(reach(adjacency_map, x, y))


