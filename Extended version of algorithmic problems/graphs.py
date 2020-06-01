
import sys
    

# 4 4
# 1 2
# 3 2
# 4 3
# 1 4
# 1 4

# def find(s, d, visited, adj):
#     if s not in visited:
#         visited.append(s)
#         if d not in adj[s]:
#             for node in adj[s]:
#                 if find(node, d, visited, adj):
#                     return True
                
#         else:
#             return True
    
    

# def checkPath():
#     input = sys.stdin.read()
#     data = list(map(int, input.split()))
#     n, m = data[0:2]
#     data = data[2:]
#     visited = []
#     edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
#     x, y = data[2 * m:]
#     adj = [[] for _ in range(n)]
#     x, y = x - 1, y - 1
#     for (a, b) in edges:
#         adj[a - 1].append(b - 1)
#         adj[b - 1].append(a - 1)
#     if find(x, y, visited, adj):
#         return True
#     else:
#         return False


# print(checkPath())


    


# def find(node, adj, nodes):
#     for vertex in adj[node]:
#         if vertex in nodes:
#             nodes.remove(vertex)
#             find(vertex, adj, nodes)
        

            


# def connected_components():
#     input = sys.stdin.read()
#     data = list(map(int, input.split()))
#     n, m = data[0:2]
#     data = data[2:]
#     edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
#     adj = [[] for _ in range(n)]
#     count = 0
#     nodes = [i for i in range(n-1, -1, -1)]
#     for (a, b) in edges:
#         adj[a - 1].append(b - 1)
#         adj[b - 1].append(a - 1)
#     while nodes:
#         node = nodes.pop()
#         find(node, adj, nodes)
#         count += 1
#     return count
        
    


# print(connected_components())


def path(node, adj, nodes, visited):
    visited.append(node)
    for vertex in adj[node]:
        
        if vertex in visited:
            return True
        
        else:
            if vertex in nodes:
                nodes.remove(vertex)
                return path(vertex, adj, nodes, visited)


def acyclicity():
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)

    nodes = [i for i in range(n-1, -1, -1)]
    while nodes:
        node = nodes.pop()
        visited = []
        if path(node, adj, nodes, visited):
            return True
    return False
    
import math
from queue import Queue
# print(acyclicity())

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
# print(min_num_segments())
    
import queue

def BFS2(adj):
    '''perform breadth first search.initialize to zeros to inidicate undiscovered. At each level, tag each discovered element 
    with alternating tag of one or two to mark the two regions, if It's biparite,  we shouldn't see connected nodes of the 
    same tag as the source'''

    q = queue.Queue()    #to process from one point and outerwards from that point
    #initialize all vertices to zero (undiscovered)
    tag = len(adj) * [0]
    #initialize first vertex with tag 1 and add to Queue
    tag[0] = 1
    q.put(0)
    while not q.empty():
        u = q.get()
        for i in adj[u]:    #process all immediate neighbors
            #check if tag is the same as u, if it is, the graph is not bipartite
            if tag[i] == tag[u]:
                return 0  #tag is not bipartite since tag(u) = tag(i)
            elif tag[i] == 0:
                q.put(i)  #if undiscovered, add to queue for processing and give it a tag of alternating number
                if tag[u] == 1:
                    tag[i] = 2
                else:
                    tag[i] = 1

    return 1



def bipartite():
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    return BFS2(adj)




# print(bipartite())
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

# print(Dijkstra())


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

        




# exchanging_money_optimally()



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
# bidDijksta()

class Node:
    def __init__(self, val, idx):
        self.val = val
        self.edges = []
        self.idx = idx
    
# def construct_trie(patterns):
#     root = Node(0)
#     for pattern in patterns:
#         currentNode = root
#         for i in range(len(pattern)):
#             currentSymbol = pattern[i]
#             for node in currentNode.edges:
#                 if node.val == currentSymbol:

#                     currentNode = node
#                     break
#             if currentNode.val != currentSymbol:
#                 currentNode.edges.append(Node(currentSymbol))
#                 currentNode = currentNode.edges[-1]
            
#     return root

def check_similarity(currentNode, text, i, index):
    
    found = False
    for node in currentNode.edges:
        if node.val[0] == text[i]:
            found = True
            k = 1
            i += 1
            while k < len(node.val) and i < len(text) and node.val[k] == text[i]:
                k += 1
                i += 1
            if k == len(node.val):
                check_similarity(node, text, i, index)
                
            elif k < len(node.val):
                if not node.edges:
                    remainder_of_old_node = node.val[k:]
                    remainder_of_new_node = text[i:]
                    node.val = node.val[:k]
                    node.idx = None
                    node.edges.append(Node(remainder_of_old_node, node.idx))
                    node.edges.append(Node(remainder_of_new_node, index))
            
    if not found:
        currentNode.edges.append(Node(text, index))

         

def make_tree(root, text, index):
    i = 0
    currentNode = root
    if not root.edges:
        root.edges.append(Node(text, index))
    elif currentNode.edges:
        check_similarity(currentNode, text, i, index)
        


        

def suffix_tree():
    text = input()
    root = Node(0, None)
    for i in range(len(text) - 1, -1, -1):
        cur_text = text[i:]
        make_tree(root, cur_text, i)
    return root

# suffix_tree = suffix_tree()
def discover(root):
    for node in root.edges:
        print(node.idx)
        discover(node)
            
# discover(suffix_tree)



def BWT():
    text = input()
    l = len(text)
    M = []
    for i in range(l):
	    M.append(text[i:]+text[:i])
    M.sort()
    
    result = ""
    for row in M:
	    result += row[-1]
    return result


    

def InverseBWT():
	# write your code here
    bwt = input()
    A, C, G , T = 1, 1, 1, 1
    lastColunm = []
    for c in bwt:
    	if c == '$':
    		lastColunm.append(('$', 0))
    	elif c == 'A':
    		lastColunm.append(('A', A))
    		A += 1
    	elif c == 'C':
    		lastColunm.append(('C', C))
    		C += 1
    	elif c == 'G':
    		lastColunm.append(('G', G))
    		G += 1
    	else:
    		lastColunm.append(('T', T))
    		T += 1
    firstColunm = sorted(lastColunm)
    firstToLast = {}
    for i in range(len(firstColunm)):
    	firstToLast[firstColunm[i]] = lastColunm[i]
    result = ""
    nextChar = ('$', 0)
    while len(result) < len(firstColunm):
    	result += nextChar[0]
    	nextChar = firstToLast[nextChar]
    result = result[::-1]
    return result

# print(InverseBWT())




    








