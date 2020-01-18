#Uses python3
# Problem Description: Task: Given an directed graph with possibly negative edge weights and with n vertices and m edges,
# check whether it contains a cycle of negative weight.
# Input Format: A graph is given in the standard format.
# Constraints: 1 ≤ n ≤ 10**3, 0 ≤ m ≤ 10**4, edge weights are integers of absolute value at most 103.
# Output Format: Output 1 if the graph contains a cycle of negative weight and 0 otherwise.
# Memory Limit: 512MB
# Sample 1: Input: 4 4
#                  1 2 -5
#                  4 1 2
#                  2 3 2
#                  3 1 1
#           Output: 1
# Explanation: The weight of the cycle 1 → 2 → 3 is equal to −2, that is, negative.

import sys

def Relaxation(u, v, w, dist):
    if dist[v] > dist[u] + w:
        dist[v] = dist[u] + w

def final_relaxation(u, v, w, dist, af):
    if dist[v] > dist[u] + w:
        dist[v] = dist[u] + w
        af.append(v)

def negative_cycle(adj, cost, n, nodes):
    dist = [10**10 for _ in range(n+1)]
    dist[1] = 0
    for _ in range(n-1):
        for node in nodes:
            for v, w in zip(adj[node], cost[node]):
                Relaxation(node, v, w, dist)
    affected_nodes = []
    for node in nodes:
        for v, w in zip(adj[node], cost[node]):
            final_relaxation(node, v, w, dist, affected_nodes)
    if affected_nodes:
        return 1
    return 0

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
    nodes_to_process = [node for node in range(1, n+1)]
    for ((a, b), w) in edges:
        adj[a].append(b)
        cost[a].append(w)
    print(negative_cycle(adj, cost, n, nodes_to_process))
