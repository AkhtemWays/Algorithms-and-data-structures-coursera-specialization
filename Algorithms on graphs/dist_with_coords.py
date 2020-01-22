#!/usr/bin/python3

import sys
import queue
import math

class AStar:
    def __init__(self, n, adj, cost, x, y):
        # See the explanations of these fields in the starter for friend_suggestion
        self.n = n
        self.adj = adj
        self.cost = cost
        self.inf = n*10**6
        self.d = [self.inf]*n
        self.visited = [False]*n
        # Coordinates of the nodes
        self.x = x
        self.y = y


    # See the explanation of this method in the starter for friend_suggestion
    def clear(self):
        for v in range(self.n):
            self.d[v] = self.inf
            self.visited[v] = False



    # See the explanation of this method in the starter for friend_suggestion
    def visit(self, q, v, u, dist, t):
        self.visited[v] = True
        if self.d[v] > self.d[u] + dist:
            self.d[v] = self.d[u] + dist
            q.put(v, self.compute_distance(v, t))

    def compute_distance(self, v, t):
        return math.sqrt((self.x[t] - self.x[v])**2 + (self.y[t] - self.y[v])**2)
    def extract_min(self, q):
        v = q.get()
        return int(v)
    # Returns the distance from s to t in the graph
    def query(self, s, t):
        self.clear()
        q = queue.PriorityQueue()
        self.d[s] = 0
        q.put(self.compute_distance(s, t), s)
        u = self.extract_min(q)
        while not q.empty():
            u = self.extract_min(q)
            if u == t:
                return self.d[u]
            for v, w in zip(adj[u], cost[u]):
                if not self.visited[v]:
                    self.visit(q, v, u, w, t)
                elif v == t:
                    return self.d[v]
                else:
                    return -1
        return -1

def readl():
    return map(int, sys.stdin.readline().split())

if __name__ == '__main__':
    n,m = readl()
    x = [0 for _ in range(n)]
    y = [0 for _ in range(n)]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for i in range(n):
        a, b = readl()
        x[i] = a
        y[i] = b
    for e in range(m):
        u,v,c = readl()
        adj[u-1].append(v-1)
        cost[u-1].append(c)
    t, = readl()
    astar = AStar(n, adj, cost, x, y)
    for i in range(t):
        s, t = readl()
        print(astar.query(s-1, t-1))

