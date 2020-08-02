import sys

def path(node, adj, nodes, visited):
    visited.append(node)
    for vertex in adj[node]:
        
        if vertex in visited:
            return True
        
        else:
            if vertex in nodes:
                nodes.remove(vertex)
                return path(vertex, adj, nodes, visited)


def acyclicity():
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)

    nodes = [i for i in range(n-1, -1, -1)]
    while nodes:
        node = nodes.pop()
        visited = []
        if path(node, adj, nodes, visited):
            return True
    return False
print(acyclicity())