#Uses python3

# Problem Description: Task: Compute a topological ordering of a given directed acyclic graph (DAG) with n vertices and m edges.
# Input Format: A graph is given in the standard format. The given graph is guaranteed to be acyclic.
# Output Format: Output reversed topological ordering of it's vertices.
# Memory Limit: 512MB
# Sample 1: Input: 4 3
#                  1 2
#                  4 1
#                  3 1
#           Output: 4 3 1 2
# Sample 2: Input: 4 1
#                  3 1
#           Output: 4 3 1 2

import sys
def Explore(adj, visited, sink, order):
    if len(adj[sink]) == 0: # 1 possible case: if the node does not have any nodes pointing at it
        if sink not in visited:
            if sink not in order:
                order.append(sink)
                visited.append(sink)
    for node in adj[sink]: # otherwise just check whether it's visited or not
        if node not in visited and node not in order:
            visited.append(node)
            order.append(node)
    if sink not in order: # finally if the key wasn't in the order at the beginning append it
        order.append(sink)

def toposort(adj):
    visited = []
    order = []
    for sink in adj.keys():
        Explore(adj, visited, sink, order)
    return order

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = {}
    for i in range(n, 0, -1): # need to output in reversed order. Create empty lists for each node
        adj[i] = []
    for (a, b) in edges: # Keys are the nodes that other vertices have direction to
        adj[b].append(a)
    order = toposort(adj)
    order = map(str, order)
    print(" ".join(order))




