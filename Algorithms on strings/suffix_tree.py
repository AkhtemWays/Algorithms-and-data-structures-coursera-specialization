import sys


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