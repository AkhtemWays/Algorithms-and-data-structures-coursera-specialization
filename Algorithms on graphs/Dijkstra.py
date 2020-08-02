import sys
from queue import Queue


def Dijkstra2(adj, cost, n, s, t):
    dist = [float('inf') for _ in range(n)]
    dist[s] = 0
    q = queue.Queue()
    q.put(s)
    while not q.empty():
        u = q.get()
        for v, w in zip(adj[u], cost[u]):
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                q.put(v)
    return dist[t]


def Dijkstra():
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    s, t = data
    s, t = s - 1, t - 1
    return Dijkstra2(adj, cost, n, s, t)

print(Dijkstra())