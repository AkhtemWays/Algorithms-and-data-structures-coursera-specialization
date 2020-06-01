from queue import LifoQueue

def check_nodes(node, nodes_to_nodes, data):
    for i, vertex in enumerate(data):
        if node == vertex:
            nodes_to_nodes[node].append(i)
            check_nodes(i, nodes_to_nodes, data)
def get_height(node, nodes_to_nodes, h):
    if len(nodes_to_nodes[node]) != 0:
        
        for vertex in nodes_to_nodes[node]:
            h += 1
            get_height(vertex, nodes_to_nodes, h)

    return h

def height():
    n = int(input())
    data = list(map(int, input().split()))
    nodes_to_nodes = {}
    for i in range(n):
        nodes_to_nodes[i] = []
    
    root = data.index(-1)
    check_nodes(root, nodes_to_nodes, data)
    
    h = 1
    
    print(get_height(root, nodes_to_nodes, h))
    
            
# print(height())


def check_brackets(s):
    stack = LifoQueue()
    left = ['[', '(', '{']
    right = [']', ')', '}']

    for char in s:
        if char in left:
            stack.put(char)
        elif char in right:
            if stack.empty(): return 'nothing found to match for {}'.format(char)
            match = stack.get()
            if (match == '(' and char != ')') or (match == '[' and char != ']') or (match == '{' and char != '}'):
                return 'Unmatched brackets {} and {} check your code again'.format(match, char)
            
    if stack.empty(): return 'Success'
    last = stack.get()
    return 'You did not close the bracket {}'.format(last)
    


# print(check_brackets('[abc]()(()){ab(gg)cd}(a)())'))



 
# python3

# import sys, threading
# from collections import defaultdict
# from queue import Queue


# class TreeHeight:
#         def read(self):
#                 self.n = int(sys.stdin.readline())
#                 self.parent = list(map(int, sys.stdin.readline().split()))

#         def compute_height(self):
#                 height, queue, h = defaultdict(list), list(), 0
#                 for index, value in enumerate(self.parent):
#                     height[value].append(index)

#                 queue += height[-1]
#                 while(True):
#                     nodecount = len(queue)
#                     if nodecount == 0:
#                         return h
#                     h += 1
#                     while nodecount > 0:
#                         node = queue.pop(0)
#                         if node in height:
#                             queue += height[node]
#                         nodecount -= 1



# tree = TreeHeight()
# tree.read()
# print(tree.compute_height())

class MaxHeap:
    def __init__(self):
        self.heap = []
    def parent(self, i):
        return (i - 1)//2
    def leftChild(self, i):
        return 2*i + 1
    def rightChild(self, i):
        return 2*i + 2
    def insert(self, val):
        self.heap.append(val)
        self.siftUp(len(self.heap) - 1)
    
    def siftUp(self, i):
        while i > 0 and self.heap[self.parent(i)] < self.heap[i]:
            self.heap[self.parent(i)], self.heap[i] = self.heap[i], self.heap[self.parent(i)]
            i = self.parent(i)
    def siftDown(self, i):
        max_idx = i
        left = self.leftChild(i)
        if left <= len(self.heap) - 1 and self.heap[left] > self.heap[max_idx]:
            max_idx = left
        right = self.rightChild(i)
        if right <= len(self.heap) - 1 and self.heap[right] > self.heap[max_idx]:
            max_idx = right
        if max_idx != i:
            self.heap[max_idx], self.heap[i] = self.heap[i], self.heap[max_idx]
            self.siftDown(max_idx)
    def ExtractMax(self):
        result = self.heap[0]
        self.heap[0] = self.heap[len(self.heap) - 1]
        self.heap = self.heap[:-1]
        self.siftDown(0)
        
        return result
    def remove(self, i):
        self.heap[i] = float('inf')
        self.siftUp(i)
        self.ExtractMax()
    def changePriority(self, i, val):
        old_val = self.heap[i]
        self.heap[i] = val
        if old_val < val:
            self.siftUp(i)
        else:
            self.siftDown(i)


# arr = [5, 1, 2, 4, 8, 7, 10, 9, 9, 1, 2, 7]
# def heap_sort(arr):
#     result = []
#     heap = MaxHeap()
#     for i in range(len(arr)):
#         heap.insert(arr[i])
#     for i in range(len(arr)):
#         result.append(heap.ExtractMax())
#     return result
# print(heap_sort(arr))

# import heapq
# arr = [5, 1, 2, 4, 8, 7, 10, 9, 9, 1, 2, 7]
# heapq.heapify(arr)
# one = heapq.heappop(arr)
# print(one)
# print(arr)
# heapq.heappush(arr, 5)
# print(arr)




# heap = MaxHeap()
# heap.insert(5)
# heap.insert(8)
# heap.insert(7)
# heap.insert(10)
# heap.insert(12)
# heap.insert(6)
# heap.insert(13)
# heap.insert(1)
# heap.insert(0)
# heap.insert(9)
# heap.remove(2)
# heap.changePriority(0, 15)
# print(heap.heap)
# print(heap.ExtractMax())
# print(heap.heap)



# helper function
# def siftDown(arr, i, count):
#     min_idx = i
#     left = (2*i) + 1
#     right = (2*i) + 2
#     if left < len(arr) and arr[left] < arr[min_idx]:
        
#         min_idx = left
    
#     if right < len(arr) and arr[right] < arr[min_idx]:
        
#         min_idx = right
#     if min_idx != i:
#         arr[min_idx], arr[i] = arr[i], arr[min_idx]
#         count.append((i, min_idx))
#         siftDown(arr, min_idx, count)
# count number of swaps
# def count_swaps():
#     count = []
#     n = int(input())
#     arr = list(map(int, input().split()))
#     for i in range(len(arr)-1, -1, -1):
#         siftDown(arr, i, count)
#     # return arr, count  to check the heap structure
#     print(len(count))
#     for i, j in count:
#         print(i, j)
#     return
# count_swaps()

# import heapq
# # processing simulation task using priority queue
# def threads():
#     n, m = list(map(int, input().split()))
#     jobs = list(map(int, input().split()))
#     times_threads = [[0, i] for i in range(n)]
#     heapq.heapify(times_threads)
#     for job in jobs:
#         result = heapq.heappop(times_threads)
#         print(result[1], result[0])
#         result[0] += job
#         heapq.heappush(times_threads, result)
#     return
        
# threads()


# simulation of merging multiple tables
# class Storage:
    
#     def __init__(self, tables):
#         self.tables = tables
#         self.maximum = 0
        
#     def merge(self, source, destination):
#         destination_table = self.tables[destination]
#         source_table = self.tables[source]
#         while destination_table.link != destination_table.id:
#             destination_table = self.tables[destination_table.link]
#         while source_table.link != source_table.id:
#             source_table = self.tables[source_table.link]
#         if source_table == destination_table:
#             self.get_max()
#         else:
#             destination_table.size += source_table.size
#             source_table.size = 0
#             source_table.link = destination_table.link
#             self.get_max()
#     def get_max(self):
        
#         for i in range(1, len(self.tables)):
#             cur_table = self.tables[i]
#             if cur_table.size > self.maximum:
#                 self.maximum = cur_table.size
#         print(self.maximum)

# class Table:
#     def __init__(self, size, id):
#         self.id = id
#         self.size = size
#         self.link = id

# def Merging_tables():
#     n, m = list(map(int, input().split()))
#     table_sizes = list(map(int, input().split()))
#     tables = [0]
#     for id, size in enumerate(table_sizes):
#         tables.append(Table(size, id+1))
#     storage = Storage(tables)
#     queries = []
#     for _ in range(m):
#         destination, source = list(map(int, input().split()))
#         queries.append((destination, source))
#     for destination, source in queries:
#         storage.merge(source, destination)
   
#     return
# Merging_tables()

# simple phonebook using hash tables with chaining
# class PhoneBook:
#     def __init__(self, n):
#         self.book = [[] for i in range(int(n**0.1))]
#         self.prime = None
#         self.n = n
#         self.cardinality_fix = len(self.book)
#     def is_prime(self, n):
#         for i in range(2, int(n**0.5)+1):
#             if n // i == 0:
#                 return False
#         return True
#     def get_prime(self):
#         n = self.n
#         while not self.is_prime(n):
#             n = n + 1
#         self.prime = n
#     def Add(self, number, name):
#         number = int(number)
#         chain_to_add = (number % self.prime) % self.cardinality_fix
#         for note in self.book[chain_to_add]:
#             if number in note.keys():
#                 note[number] = name
#                 return
#         self.book[chain_to_add].append({number: name})
#     def Find(self, number):
#         number = int(number)
#         chain_to_search = (number % self.prime) % self.cardinality_fix
#         for note in self.book[chain_to_search]:
#             if number in note.keys():
#                 print(note[number])
#                 return
#         print('not found')
#         return
#     def Del(self, number):
#         number = int(number)
#         chain_to_search = (number % self.prime) % self.cardinality_fix
#         for i, note in enumerate(self.book[chain_to_search]):
#             if number in note.keys():
#                 del self.book[chain_to_search][i]
#                 return


# def ActivatePhoneBook():
#     n = int(input())
#     book = PhoneBook(10**5)
#     book.get_prime()
#     for _ in range(n):
#         request = input().split()
#         if request[0] == 'find':
#             number = request[1]
#             book.Find(number)
#         elif request[0] == 'add':
#             number, name = request[1], request[2]
#             book.Add(number, name)
#         elif request[0] == 'del':
#             book.Del(request[1])
#         else:
#             print('request {} has not been identified'.format(request[0]))
#     return

# ActivatePhoneBook()


# simple storage storing arbitrary info using hash tables with polynomial hash functions
# class Storage:
#     def __init__(self, cardinality_fix):
#         self.cardinality_fix = cardinality_fix
#         self.data = [[] for i in range(cardinality_fix)]
#         self.prime = 1000000007 # was stated to use that prime
#         self.x = 263 # and that x
#     def hash_string(self, string):
#         hash = 0
#         for i in range(len(string)):
#             hash += (ord(string[i]) * self.x**i)
#         hash = hash % self.prime
#         return hash % self.cardinality_fix
    
#     def Add(self, string):
#         hash = self.hash_string(string)
        
#         self.data[hash].append(string)
#     def Find(self, string):
#         hash = self.hash_string(string)
#         if string in self.data[hash]:
#             print('yes')
#         else:
#             print('no')
#     def Del(self, string):
#         hash = self.hash_string(string)
#         for i, s in enumerate(self.data[hash]):
#             if s == string:
#                 del self.data[hash][i]

#     def Check(self, hash):
#         if self.data[hash]:
#             print(" ".join(self.data[hash][::-1]))
                
#         else:
#             print(" ")
        

# def ActivateStorage():
#     cardinality_fix = int(input())
#     n_queries = int(input())
#     storage = Storage(cardinality_fix)
#     for _ in range(n_queries):
#         query = input().split()
#         if query[0] == 'add':
#             storage.Add(query[1])
#         elif query[0] == 'find':
            
#             storage.Find(query[1])
#         elif query[0] == 'check':
#             storage.Check(int(query[1]))
#         elif query[0] == 'del':
#             storage.Del(query[1])
#         else:
#             print('query {} has not been identified'.format(query[0]))
#     return 'I am done sir'

# ActivateStorage()

# class Node:
#     def __init__(self, key, left, right):
#         self.key = key
#         self.left = left
#         self.right = right
#         self.parent = 0

# class BST:
#     def __init__(self):
#         self.tree = []
#         self.inOrder = []
#         self.preOrder = []
#         self.postOrder = []
    
    
#     def validate_parents(self, node):
#         while node.parent != 0:
                    
#             for vertex in self.tree:
#                 if vertex.key == node.parent:
#                     if self.tree[vertex.left] == node:
                       
#                         if node.key >= vertex.key:
                            
#                             return False
#                         else:
#                             node = vertex
#                     elif self.tree[vertex.right] == node:
                        
#                         if node.key < vertex.key:
                            
#                             return False
#                         else:
#                             node = vertex



#     def validate_tree(self, node):

#         if node.left != -1 and node.right != -1:
#             if self.tree[node.left].key < node.key and self.tree[node.right].key >= node.key:
#                 self.validate_tree(self.tree[node.left])
#                 self.validate_tree(self.tree[node.right])
#                 if not self.validate_parents(node):
#                     print('a')
#                     return 'INCORRECT'
#             else:
#                 print('b')
#                 return 'INCORRECT'
        
#         elif node.left == -1 and node.right != -1:
#             if self.tree[node.right].key >= node.key:
#                 self.validate_tree(self.tree[node.right])
#                 if not self.validate_parents(node):
#                     print('c')
#                     return 'INCORRECT'
#             else:
#                 print('d')
#                 return 'INCORRECT'
#         elif node.left != -1 and node.right == -1:
#             if self.tree[node.left].key < node.key:
#                 self.validate_tree(self.tree[node.left])
#                 if not self.validate_parents(node):
#                     print('e')
#                     return 'INCORRECT'
#             else:
#                 print('f')
#                 return 'INCORRECT'
#         elif node.left == -1 and node.right == -1:
#             if not self.validate_parents(node):
#                 print('here')
#                 return 'INCORRECT'
        
#         return 'CORRECT'
        
#     def find_parent(self, node):
#         if node.left != -1 and node.right != -1:
#             self.tree[node.left].parent = node.key
#             self.tree[node.right].parent = node.key
#             self.find_parent(self.tree[node.right])
#             self.find_parent(self.tree[node.left])
#         if node.left == -1 and node.right != -1:
#             self.tree[node.right].parent = node.key
#             self.find_parent(self.tree[node.right])
#         if node.left != -1 and node.right == -1:
#             self.tree[node.left].parent = node.key
#             self.find_parent(self.tree[node.left])
#     def read_data(self, data):
#         for key, left, right in data:
#             if left != -1 and right != -1:

#                 self.tree.append(Node(key, left, right))
#             elif left == -1 and right != -1:
#                 self.tree.append(Node(key, -1, right))
#             elif left != -1 and right == -1:
#                 self.tree.append(Node(key, left, -1))
#             elif left == -1 and right == -1:
#                 self.tree.append(Node(key, -1, -1))
#         self.find_parent(self.tree[0])
        

    
            
#     def InOrderTraversal(self, node):
#         if node.left == None and node.right == None:
#             self.inOrder.append(node.key)
#             return
#         self.InOrderTraversal(self.tree[node.left])
#         self.inOrder.append(node.key)
#         self.InOrderTraversal(self.tree[node.right])
#     def PostOrderTraversal(self, node):
#         if node.left == None and node.right == None:
#             self.postOrder.append(node.key)
#             return
#         self.PostOrderTraversal(self.tree[node.left])
#         self.PostOrderTraversal(self.tree[node.right])
#         self.postOrder.append(node.key)
#     def PreOrderTraversal(self, node):
#         if node.left == None and node.right == None:
#             self.preOrder.append(node.key)
#             return
#         self.preOrder.append(node.key)
#         self.PreOrderTraversal(self.tree[node.left])
#         self.PreOrderTraversal(self.tree[node.right])
        
    


# def treeTraversals():
#     n = int(input())
#     tree = BST(n)
#     data = []
#     for _ in range(n):
#         to_add = list(map(int, input().split()))
#         data.append(to_add)
#     tree.read_data(data)
#     tree.InOrderTraversal(tree.tree[0])
#     print(" ".join(list(map(str, tree.inOrder))))
#     tree.PreOrderTraversal(tree.tree[0])
#     print(" ".join(list(map(str, tree.preOrder))))
#     tree.PostOrderTraversal(tree.tree[0])
#     print(" ".join(list(map(str, tree.postOrder))))
    
    

# treeTraversals()

# def is_BST():
#     n = int(input())
#     if n == 0:
#         print('CORRECT')
#         return
#     data = []
#     tree = BST()
#     for _ in range(n):
#         to_add = list(map(int, input().split()))
#         data.append(to_add)
#     tree.read_data(data)
#     print(tree.validate_tree(tree.tree[0]))

# is_BST()


class Node:
	def __init__(self, val):
		self.value = val
		self.leftChild = None
		self.rightChild = None
		
	def insert(self, data):
		if self.value == data:
			return False
			
		elif self.value > data:
			if self.leftChild:
				return self.leftChild.insert(data)
			else:
				self.leftChild = Node(data)
				return True

		else:
			if self.rightChild:
				return self.rightChild.insert(data)
			else:
				self.rightChild = Node(data)
				return True
				
	def find(self, data):
		if(self.value == data):
			return True
		elif self.value > data:
			if self.leftChild:
				return self.leftChild.find(data)
			else:
				return False
		else:
			if self.rightChild:
				return self.rightChild.find(data)
			else:
				return False
				
	def getHeight(self):
		if self.leftChild and self.rightChild:
			return 1 + max(self.leftChild.getHeight(), self.rightChild.getHeight())
		elif self.leftChild:
			return 1 + self.leftChild.getHeight()
		elif self.rightChild:
			return 1 + self.rightChild.getHeight()
		else:
			return 1

	def preorder(self):
		if self:
			print (str(self.value))
			if self.leftChild:
				self.leftChild.preorder()
			if self.rightChild:
				self.rightChild.preorder()

	def postorder(self):
		if self:
			if self.leftChild:
				self.leftChild.postorder()
			if self.rightChild:
				self.rightChild.postorder()
			print (str(self.value))

	def inorder(self):
		if self:
			if self.leftChild:
				self.leftChild.inorder()
			print (str(self.value))
			if self.rightChild:
				self.rightChild.inorder()

class Tree:
	def __init__(self):
		self.root = None

	def insert(self, data):
		if self.root:
			return self.root.insert(data)
		else:
			self.root = Node(data)
			return True

	def find(self, data):
		if self.root:
			return self.root.find(data)
		else:
			return False
			
	def getHeight(self):
		if self.root:
			return self.root.getHeight()
		else:
			return -1
	
	def remove(self, data):
		# empty tree
		if self.root is None:
			return False
			
		# data is in root node	
		elif self.root.value == data:
			if self.root.leftChild is None and self.root.rightChild is None:
				self.root = None
			elif self.root.leftChild and self.root.rightChild is None:
				self.root = self.root.leftChild
			elif self.root.leftChild is None and self.root.rightChild:
				self.root = self.root.rightChild
			elif self.root.leftChild and self.root.rightChild:
				delNodeParent = self.root
				delNode = self.root.rightChild
				while delNode.leftChild:
					delNodeParent = delNode
					delNode = delNode.leftChild
					
				self.root.value = delNode.value
				if delNode.rightChild:
					if delNodeParent.value > delNode.value:
						delNodeParent.leftChild = delNode.rightChild
					elif delNodeParent.value < delNode.value:
						delNodeParent.rightChild = delNode.rightChild
				else:
					if delNode.value < delNodeParent.value:
						delNodeParent.leftChild = None
					else:
						delNodeParent.rightChild = None
						
			return True
		
		parent = None
		node = self.root
		
		# find node to remove
		while node and node.value != data:
			parent = node
			if data < node.value:
				node = node.leftChild
			elif data > node.value:
				node = node.rightChild
		
		# case 1: data not found
		if node is None or node.value != data:
			return False
			
		# case 2: remove-node has no children
		elif node.leftChild is None and node.rightChild is None:
			if data < parent.value:
				parent.leftChild = None
			else:
				parent.rightChild = None
			return True
			
		# case 3: remove-node has left child only
		elif node.leftChild and node.rightChild is None:
			if data < parent.value:
				parent.leftChild = node.leftChild
			else:
				parent.rightChild = node.leftChild
			return True
			
		# case 4: remove-node has right child only
		elif node.leftChild is None and node.rightChild:
			if data < parent.value:
				parent.leftChild = node.rightChild
			else:
				parent.rightChild = node.rightChild
			return True
			
		# case 5: remove-node has left and right children
		else:
			delNodeParent = node
			delNode = node.rightChild
			while delNode.leftChild:
				delNodeParent = delNode
				delNode = delNode.leftChild
				
			node.value = delNode.value
			if delNode.rightChild:
				if delNodeParent.value > delNode.value:
					delNodeParent.leftChild = delNode.rightChild
				elif delNodeParent.value < delNode.value:
					delNodeParent.rightChild = delNode.rightChild
			else:
				if delNode.value < delNodeParent.value:
					delNodeParent.leftChild = None
				else:
					delNodeParent.rightChild = None

	def preorder(self):
		if self.root is not None:
			print("PreOrder")
			self.root.preorder()
		
	def postorder(self):
		if self.root is not None:
			print("PostOrder")
			self.root.postorder()
			
	def inorder(self):
		if self.root is not None:
			print("InOrder")
			self.root.inorder()

bst = Tree()
print(bst.insert(10))
#print(bst.insert(5))
bst.preorder()
print(bst.getHeight())
#bst.postorder()
#bst.inorder()
print(bst.remove(10))
bst.preorder()


