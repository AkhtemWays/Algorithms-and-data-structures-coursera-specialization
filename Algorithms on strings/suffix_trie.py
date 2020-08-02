class Node:
    def __init__(self, val, idx):
        self.val = val
        self.edges = []
        self.idx = idx
    
def construct_trie(patterns):
    root = Node(0)
    for pattern in patterns:
        currentNode = root
        for i in range(len(pattern)):
            currentSymbol = pattern[i]
            for node in currentNode.edges:
                if node.val == currentSymbol:

                    currentNode = node
                    break
            if currentNode.val != currentSymbol:
                currentNode.edges.append(Node(currentSymbol))
                currentNode = currentNode.edges[-1]
            
    return root