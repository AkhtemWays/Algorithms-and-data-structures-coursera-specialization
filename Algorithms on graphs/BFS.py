import sys


def BFS(adj, s, d, n):
    dist = [float('inf') for _ in range(n)]
    dist[s] = 0
    
    q = Queue()
    q.put(s)
    while not q.empty():
        u = q.get()
        for v in adj[u]:
            if dist[v] == float('inf'):
                q.put(v)
                dist[v] = dist[u] + 1
    return dist[d]

def min_num_segments():
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    s, d = data[2 * m:]
    s, d = s - 1, d - 1
    
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    return BFS(adj, s, d, n)
print(min_num_segments())