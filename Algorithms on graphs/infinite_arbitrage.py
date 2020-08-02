import sys
from queue import Queue

def infinite_arbitrage():
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
    dist = [float('inf') for _ in range(n)]
    s = data[0] - 1
    dist[s] = 0
    q = queue.Queue()
    q.put(s)
    arbitrage = []
    for i in range(n):
        u = q.get()
        if i != n - 1:
            for v, w in zip(adj[u], cost[u]):
                if dist[v] > dist[u] + w:
                    dist[v] = dist[u] + w
                    q.put(v)
        elif i == n - 1:
            for v, w in zip(adj[u], cost[u]):
                if dist[v] > dist[u] + w:
                    arbitrage.append(u)
                    arbitrage.append(v)
                    dist[v] = dist[u] + w
                    for k, w2 in zip(adj[v], cost[v]):
                        if dist[k] > dist[v] + w2:
                            arbitrage.append(k)
                            return arbitrage, dist
# print(infinite_arbitrage())                  

def exchanging_money_optimally():
    arbitrage, dist = infinite_arbitrage()

    for l, d in enumerate(dist):
        if d == float('inf'):
            dist[l] = '*'
    for j in arbitrage:
        dist[j] = '-'
    for res in dist:
        print(res)
    return

print(exchanging_money_optimally())
