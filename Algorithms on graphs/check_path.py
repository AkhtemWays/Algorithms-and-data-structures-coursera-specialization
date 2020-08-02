import sys
    

# 4 4
# 1 2
# 3 2
# 4 3
# 1 4
# 1 4

def find(s, d, visited, adj):
    if s not in visited:
        visited.append(s)
        if d not in adj[s]:
            for node in adj[s]:
                if find(node, d, visited, adj):
                    return True
                
        else:
            return True
    
    

def checkPath():
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    visited = []
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    x, y = data[2 * m:]
    adj = [[] for _ in range(n)]
    x, y = x - 1, y - 1
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    if find(x, y, visited, adj):
        return True
    else:
        return False


print(checkPath())