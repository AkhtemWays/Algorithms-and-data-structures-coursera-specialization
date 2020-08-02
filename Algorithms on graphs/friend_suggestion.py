#!/usr/bin/python3

# Problem Description: Task: Compute the distance between several pairs of nodes in the network.
# Input Format: The first line contains two integers 𝑛 and 𝑚 — the number of nodes and edges in the
# network, respectively. The nodes are numbered from 1 to 𝑛. Each of the following 𝑚 lines contains
# three integers 𝑢, 𝑣 and 𝑙 describing a directed edge (𝑢, 𝑣) of length 𝑙 from the node number 𝑢to the
# node number 𝑣. (Note that some social networks are represented by directed graphs while some other
# correspond naturally to undirected graphs. For example, Twitter is a directed graph (with a directed
# edge (𝑢, 𝑣) meaning that 𝑢 follows 𝑣), while Facebook is an undirected graph (where an undirected
# edge {𝑢, 𝑣} means that 𝑢 and 𝑣 are friends). In this problem, we work with directed graphs only for a
# simple reason. It is easy to turn an undirected graph into a directed one: just replace each undirected
# edge {𝑢, 𝑣} with a pair of directed edges (𝑢, 𝑣) and (𝑣, 𝑢).)
# The next line contains an integer 𝑞 — the number of queries for computing the distance. Each of the
# following 𝑞 lines contains two integers 𝑢 and 𝑣 — the numbers of the two nodes to compute the distance
# from 𝑢 to 𝑣.
# Constraints: 1 ≤ 𝑛 ≤ 1 000 000; 1 ≤ 𝑚 ≤ 6 000 000; 1 ≤ 𝑢, 𝑣 ≤ 𝑛; 1 ≤ 𝑙 ≤ 1 000; 1 ≤ 𝑞 ≤ 1 000.
# Output Format: For each query, output one integer on a separate line. If there is no path from 𝑢 to 𝑣,
# output −1. Otherwise, output the distance from 𝑢 to 𝑣.
# Time Limit: 150 sec for Python3
# Memory Limit: 2048
# This assignment solved using Bidirectional Dijkstra Algorithm


import sys
import queue

class BiDij:
    def __init__(self, n):
        self.n = n                              # Number of nodes
        self.inf = n*10**6                      # All distances in the graph are smaller
        self.d = [[self.inf]*n, [self.inf]*n]   # Initialize distances for forward and backward searches
        self.visited = [False]*n                # visited[v] == True iff v was visited by forward or backward search
        self.workset = []                       # All the nodes visited by forward or backward search

    def clear(self):
        """Reinitialize the data structures for the next query after the previous query."""
        for v in self.workset:
            self.d[0][v] = self.d[1][v] = self.inf
            self.visited[v] = False
        del self.workset[0:len(self.workset)]

    def visit(self, q, side, v, dist, node):
    # """Try to relax the distance to node v from direction side by value dist."""
        self.workset.append(v)
        self.visited[v] = True
        if self.d[side][v] > self.d[side][node] + dist:
            self.d[side][v] = self.d[side][node] + dist
            q[side].put(v)

    def query(self, adj, cost, s, t):
        self.clear()
        q = [queue.PriorityQueue(), queue.PriorityQueue()] # 2 queues for start and end
        self.d[0][s], self.d[1][t] = 0, 0 # initilization of start and end distances
        q[0].put(s)
        q[1].put(t)

        while not q[0].empty() and not q[1].empty():
            node1, node2 = q[0].get(), q[1].get()
            side = 0
            if not self.visited[node1] and not self.visited[node2]:
                for outgoing, leng in zip(adj[side][node1], cost[side][node1]): # checks for outgoing edges
                    if outgoing in self.workset: # in case the node has been processed already - need to compute the distance to it
                        self.visit(q, side, outgoing, leng, node1)
                        return self.d[side][outgoing] + self.d[1-side][outgoing] # and return the result
                    else:
                        self.visit(q, side, outgoing, leng, node1)
                side = 1 - side # same for the other side
                for ingoing, leng2 in zip(adj[side][node2], cost[side][node2]):
                    if ingoing in self.workset:
                        self.visit(q, side, ingoing, leng2, node2)
                        return self.d[side][ingoing] + self.d[1 - side][ingoing]
                    else:
                        self.visit(q, side, ingoing, leng2, node2)
        # algorithm does not return correct values for s == t case and if the optimal edge between two nodes u, v is itself (u, v)
        # thus a slight correction has been made to fix that
        if s == t:
            return 0
        elif t in adj[0][s]:
            return cost[0][s]
        else:
            return -1

def readl():
    return map(int, sys.stdin.readline().split())


if __name__ == '__main__':
    n,m = readl()
    adj = [[[] for _ in range(n)], [[] for _ in range(n)]] # creation of arrays for edges for start node and edges for and end node
    cost = [[[] for _ in range(n)], [[] for _ in range(n)]]
    for e in range(m):
        u,v,c = readl()
        adj[0][u-1].append(v-1)
        cost[0][u-1].append(c)
        adj[1][v-1].append(u-1) # this appends for the reversed graph
        cost[1][v-1].append(c) # same for cost

    t, = readl()
    bidij = BiDij(n)
    for i in range(t):
        s, t = readl()
        print(bidij.query(adj, cost, s-1, t-1))

