#!/usr/bin/python3

# Problem Description: Task. You are given a binary tree with integers as its keys. You need to test whether it is a correct
# binary search tree. The definition of the binary search tree is the following: for any node of the tree, if its key is x,
# then for any node in its left subtree its key must be strictly less than x, and for any node in its right subtree its key
# must be strictly greater than x. In other words, smaller elements are to the left, and bigger elements are to the right.
# You need to check whether the given binary tree structure satisfies this condition. You are guaranteed that the input contains
# a valid binary tree. That is, it is a tree, and each node has at most two children.
# Input Format: The first line contains the number of vertices n. The vertices of the tree are numbered from 0 to n−1.
# Vertex 0 is the root. The next n lines contain information about vertices 0, 1, ..., n−1 in order. Each of these lines contains
# three integers keyi, lefti and righti — keyi is the key of the i-th vertex, lefti is the index of the left child of
# the i-th vertex, and righti is the index of the right child of the i-th vertex. If i doesn’t have left or right child (or both),
# the corresponding lefti or righti (or both) will be equal to −1.
# Output Format: If the given binary tree is a correct binary search tree (see the definition in the problem description),
# output one word “CORRECT” (without quotes). Otherwise, output one word “INCORRECT” (without quotes).
# Memory Limit: 512MB.
# Sample 1: Input: 3
#                  2 1 2
#                  1 -1 -1
#                  3 -1 -1
#                  Output: CORRECT
# Explanation:        2
#                    / \
#                   1   3
# Sample 2: Input: 5
#                  1 -1 1
#                  2 -1 2
#                  3 -1 3
#                  4 -1 4
#                  5 -1 -1
#                  Output: CORRECT
# Explanation:          1
#                        \
#                         2
#                          \
#                           3
#                            \
#                             4
#                              \
#                               5


import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size

class binary_search_tree:
  def __init__(self, tree, nodes):
    self.nodes = nodes
    self.keys = [0 for i in range(self.nodes)]
    self.left_indices = [0 for i in range(self.nodes)]
    self.right_indices = [0 for i in range(self.nodes)]
    for i,j in enumerate(tree):
        self.keys[i], self.left_indices[i], self.right_indices[i] = j[0], j[1], j[2]
  def IsBinarySearchTree(self):
    current_index = 0
    while current_index < self.nodes:
      left_index = self.left_indices[current_index]
      right_index = self.right_indices[current_index]
      if right_index != -1:
        if self.keys[current_index] > self.keys[right_index]:
          return False
      if left_index != -1:
        if self.keys[current_index] < self.keys[left_index]:
          return False
      current_index += 1
    return True

def main():
  nodes = int(sys.stdin.readline().strip())
  tree = []
  for i in range(nodes):
    tree.append(list(map(int, sys.stdin.readline().strip().split())))
  BinarySearchTree = binary_search_tree(tree, nodes)
  if nodes == 0:
    print('CORRECT')
  else:

    if BinarySearchTree.IsBinarySearchTree():
      print("CORRECT")
    else:
      print("INCORRECT")


threading.Thread(target=main).start()

