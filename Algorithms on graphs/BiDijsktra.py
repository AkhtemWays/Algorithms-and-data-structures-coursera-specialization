import sys
from queue import Queue

def ReverseGraphAndCost(adj, cost):
    reversed_adj = [[] for _ in range(len(adj))]
    reversed_cost = [[] for _ in range(len(adj))]
    for node, (node_neighbors, c) in enumerate(zip((adj), cost)):
        for neighbor, w in zip(node_neighbors, c):
            reversed_adj[neighbor].append(node)
            reversed_cost[neighbor].append(w)
    return reversed_adj, reversed_cost
def Relax(u, v, dist, prev, w):
    if dist[v] > dist[u] + w:
        dist[v] = dist[u] + w
        prev[v] = u

def Process(u, adj, dist, prev, proc, cost):
    for v, w in zip(adj[u], cost[u]):
        Relax(u, v, dist, prev, w)
    proc.append(u)

def ShortestPath(s, dist_F, prev_F, processed_F, t, dist_R, prev_R, processed_R):
    distance = float('inf')
    u_best = None
    processedJoined = processed_F
    for node in processed_R:
        processedJoined.append(node)
    for u in processedJoined:
        if dist_F[u] + dist_R[u] < distance:
            u_best = u
            distance = dist_F[u] + dist_R[u]
    path = []
    last = u_best
    while last != s:
        path.append(last)
        last = prev_F[last]
    path = path[::-1]
    last = u_best
    while last != t:
        last = prev_R[last]
        path.append(last)
    return distance, path

def BidirectionalDijkstra(adj_F, s, t, cost_F):
    adj_R, cost_R = ReverseGraphAndCost(adj_F, cost_F)
    dist_F, dist_R = [float('inf') for _ in range(len(adj_F))], [float('inf') for _ in range(len(adj_F))]
    dist_F[s], dist_R[t] = 0, 0
    prev_F, prev_R = [None for _ in range(len(adj_F))], [None for _ in range(len(adj_F))]
    processed_F, processed_R = [], []
    q_F, q_R = queue.Queue(), queue.Queue()
    q_F.put(s)
    q_R.put(t)
    while not q_F.empty() or not q_R.empty():
        v_F = q_F.get()
        Process(v_F, adj_F, dist_F, prev_F, processed_F, cost_F)
        if v_F in processed_R:
            print('b')
            return ShortestPath(s, dist_F, prev_F, processed_F, t, dist_R, prev_R, processed_R)
        v_R = q_R.get()
        Process(v_R, adj_R, dist_R, prev_R, processed_R, cost_R)
        if v_R in processed_F:
            print('a')
            return ShortestPath(s, dist_F, prev_F, processed_F, t, dist_R, prev_R, processed_R)

def bidDijksta():
    n, m = list(map(int, input().split()))
    

    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for _ in range(m):
        node1, node2, w = list(map(int, input().split()))
        adj[node1 - 1].append(node2 - 1)
        cost[node1 - 1].append(w)
    quer = int(input())
    for _ in range(quer):
        s, t = list(map(int, input().split()))
        s, t = s - 1, t - 1
        print(BidirectionalDijkstra(adj, s, t, cost))
    return
bidDijksta()