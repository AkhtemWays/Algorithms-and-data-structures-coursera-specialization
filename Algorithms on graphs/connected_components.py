import sys

def find(node, adj, nodes):
    for vertex in adj[node]:
        if vertex in nodes:
            nodes.remove(vertex)
            find(vertex, adj, nodes)
        

            


def connected_components():
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    count = 0
    nodes = [i for i in range(n-1, -1, -1)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    while nodes:
        node = nodes.pop()
        find(node, adj, nodes)
        count += 1
    return count
        
    


print(connected_components())