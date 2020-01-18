#Uses python3
# Problem Description: Task: Given an directed graph with positive edge weights and with n vertices and m edges as well as two
# vertices u and v, compute the weight of a shortest path between u and v (that is, the minimum total weight of a path from u to v).
# Input Format: A graph is given in the standard format. The next line contains two vertices u and v.
# Constraints: 1 ≤ n ≤ 10**4, 0 ≤ m ≤ 10**5, u ̸= v, 1 ≤ u,v ≤ n, edge weights are non-negative integers not exceeding 103.
# Output Format: Output the minimum weight of a path from u to v, or −1 if there is no path
# Memory Limit: 512MB
# Sample 1: Input: 4 4
#                  1 2 1
#                  4 1 2
#                  2 3 2
#                  1 3 5
#                  1 3
#            Output: 3
# Sample 2: Input: 5 9
#                  1 2 4
#                  1 3 2
#                  2 3 2
#                  3 2 1
#                  2 4 2
#                  3 5 4
#                  5 4 1
#                  2 5 3
#                  3 4 4
#                  1 5
#            Output: 6
# The following algorithm uses priority queue data structure and supports 1-based indexing for the nodes given


import sys
import queue


def Relaxation(u, v, w, dist, q):
    if dist[v] > dist[u] + w:
        dist[v] = dist[u] + w
        q.put(v)

def Dijkstra(adj, cost, s, t, n):
    q = queue.PriorityQueue()
    dist = [float('inf') for _ in range(n+1)] # basically range is n+1 is in order to secure 1-based indexing ignoring 0 index
    dist[s] = 0 # initialize starting node with 0
    q.put(s)
    while not q.empty():
        u = q.get()
        for v,w in zip(adj[u], cost[u]): # maps the incoming edges from u towards v and the corresponding weights
            Relaxation(u, v, w, dist, q) #
    if dist[t] == float('inf'): # if t's node was not reached
        return -1
    return dist[t]

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj, cost = {}, {}
    for i in range(1, n+1):
        adj[i], cost[i] = [], []
    for ((a, b), w) in edges:
        adj[a].append(b)
        cost[a].append(w)
    s, t = data[0], data[1]
    print(Dijkstra(adj, cost, s, t, n))
