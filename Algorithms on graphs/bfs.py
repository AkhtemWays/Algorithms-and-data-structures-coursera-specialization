#Uses python3
# Problem Description: Task: Given an undirected graph with n vertices and m edges and two vertices u and v, compute the length of
# a shortest path between u and v (that is, the minimum number of edges in a path from u to v).
# Input Format: A graph is given in the standard format. The next line contains two vertices u and v.
# Output Format: Output the minimum number of edges in a path from u to v, or −1 if there is no path.
# Memory Limit: 512MB
# Sample 1: Input: 4 4
#                  1 2
#                  4 1
#                  2 3
#                  3 1
#                  2 4
#           Output: 2
# Explanation: There is a unique shortest path between vertices 2 and 4 in this graph: 2 − 1 − 4.
#                           4   3
#                           |  /|
#                           | / |
#                           |/  |
#                           1---2
# Sample 2: Input: 5 4
#                  5 2
#                  1 3
#                  3 4
#                  1 4
#                  3 5
#           Output: -1
# the following task was solved using queues, thus calculating all the distances from the given node!
import sys
import queue

def distance(adj, node_to_begin, node_to_finish):
    distance = [float('inf')] * len(adj) # set all the distances equal to infinity to begin with
    distance[node_to_begin] = 0 # set distance from node to start with equal to 0, since the distance to itself is zero
    q = queue.Queue()
    q.put(node_to_begin)
    while not q.empty():
        u = q.get()
        for i in adj[u]: # check each node that u's nodes connected to
            if distance[i] == float('inf'): # this statement basically means if the nodes are unvisited still, set the distance
                distance[i] = distance[u] + 1 # from the closest one + 1
                q.put(i)
    if distance[node_to_finish] == float('inf'): # the final statement returns only the distance to the node program cares about
        return -1
    return distance[node_to_finish]

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    s, t = data[2 * m] - 1, data[2 * m + 1] - 1
    print(distance(adj, s, t))
