# python3


# Problem Description: Task. You are given a rooted binary tree. Build and output its in-order, pre-order and post-order traversals.
# Input Format. The first line contains the number of vertices n. The vertices of the tree are numbered from 0 to n−1.
# Vertex 0 is the root. The next n lines contain information about vertices 0, 1, ..., n−1 in order.
# Each of these lines contains three integers keyi, lefti and righti — keyi is the key of the i-th vertex,
# lefti is the index of the left child of the i-th vertex, and righti is the index of the right child of the i-th vertex.
# If i doesn’t have left or right child (or both), the corresponding lefti or righti (or both) will be equal to −1.
# Output Format: Print three lines: The first line should contain the keys of the vertices in the in-order traversal of the tree.
# The second line should contain the keys of the vertices in the pre-order traversal of the tree.
# The third line should contain the keys of the vertices in the post-order traversal of the tree.
# Memory Limit. 512MB.
# Sample 1: Input: 5
#                  4 1 2
#                  2 3 4
#                  5 -1 -1
#                  1 -1 -1
#                  3 -1 -1
#                  Output:
#                  1 2 3 4 5
#                  4 2 1 3 5
#                  1 3 2 5 4
# Explanation:
   #        root
   #          4
   #         / \
   #        2   5
   #       / \
   #      1   3





import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeOrders:
    def read(self):
        self.n = int(sys.stdin.readline())
        self.keys = [0 for _ in range(self.n)]
        self.left_indices = [0 for _ in range(self.n)]
        self.right_indices = [0 for _ in range(self.n)]
        for i in range(self.n):
            self.keys[i], self.left_indices[i], self.right_indices[i] = map(
                int, sys.stdin.readline().split())

    def in_Order(self):
        self.result = []
        stack = []
        current_index = 0
        while True:
            if current_index != -1:
                stack.append(current_index)
                current_index = self.left_indices[current_index]
            elif len(stack) != 0:
                current_index = stack.pop()
                self.result.append(self.keys[current_index])
                current_index = self.right_indices[current_index]
            else:
                return self.result

    def pre_order(self):
        self.result = []
        current_index = 0
        stack = []
        while True:
            if current_index != -1:
                stack.append(current_index)
                self.result.append(self.keys[current_index])
                current_index = self.left_indices[current_index]
            elif stack:
                current_index = stack.pop()
                current_index = self.right_indices[current_index]
            else:
                return self.result

    def post_order(self):
        """Post-order tree traversal."""
        # Create two stacks and push root's index to the first one.
        stack1 = [0]
        result_stack_reversed = []
        while stack1:
            current_index = stack1.pop()
            result_stack_reversed.append(self.keys[current_index])

            left_index = self.left_indices[current_index]
            right_index = self.right_indices[current_index]
            if left_index != -1:
                stack1.append(left_index)
            if right_index != -1:
                stack1.append(right_index)

        return result_stack_reversed[::-1]

def main():
    tree = TreeOrders()
    tree.read()
    print(" ".join(str(x) for x in tree.in_Order()))
    print(" ".join(str(x) for x in tree.pre_order()))
    print(" ".join(str(x) for x in tree.post_order()))
if __name__ == '__main__':
    main()




threading.Thread(target=main).start()
