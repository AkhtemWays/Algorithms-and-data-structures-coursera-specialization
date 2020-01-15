# python3

# Problem Description: Task. You are given a string S and you have to process n queries. Each query is described by three
# integers i,j,k and means to cut substring S[i..j] (i and j are 0-based) from the string and then insert it after the k-th symbol
# of the remaining string (if the symbols are numbered from 1). If k = 0, S[i..j] is inserted in the beginning. See the examples
# for further clarification.
# Input Format: The first line contains the initial string S. The second line contains the number of queries q.
# Next q lines contain triples of integers i,j,k.
# Constraints. S contains only lowercase english letters. 1 ≤ |S| ≤ 300000; 1 ≤ q ≤ 100000; 0 ≤ i ≤ j ≤ n−1; 0 ≤ k ≤ n−(j −i + 1).
# Output Format: Output the string after all q queries.
# Sample 1: Input: hlelowrold
#                  2
#                  1 1 2
#                  6 6 7
#                  Output: helloworld
# Explanation: hlelowrold → hellowrold → helloworld When i = j = 1, S[i..j] = l, and it is inserted after the 2-nd symbol of the
# remaining string helowrold, which gives hellowrold. Then i = j = 6, so S[i..j] = r, and it is inserted after the 7-th symbol of
# the remaining string hellowold, which gives helloworld.
# Sample 2: Input: abcdef
#                  2
#                  0 1 1
#                  4 5 0
#                  Output: efcabd

import sys

class Rope:
	def __init__(self, string):
		self.string = string
	def make_list(self):
		li = []
		for i in self.string:
			li.append(i)
		return li
	def partition(self, i, j, array): # partitions the string on the temporarily deleted part and two substrings
		string_to_insert = array[i:j+1]
		left = array[:i]
		right = array[j+1:]
		return string_to_insert, left, right
	def solve(self, string, left, right):
		for i in right:
			left.append(i)
		l = left
		left = l[:k]
		right = l[k:]
		for i in string:
			left.append(i)
		for i in right:
			left.append(i)
		self.string = "".join(left)
		return self.string
	def process(self, i, j, k):
		array = self.make_list()
		string_to_insert, left, right = self.partition(i, j, array)
		return self.solve(string_to_insert, left, right)

rope = input()
q = int(sys.stdin.readline())
for _ in range(q):
	i, j, k = map(int, sys.stdin.readline().strip().split())
	object = Rope(rope)
	rope = object.process(i, j, k)
print(rope)

