#Uses python3

# Problem Introduction: In this problem, the goal is to build roads between some pairs of the given cities such that there is a path
# between any two cities and the total length of the roads is minimized.
# Problem Description: Task: Given n points on a plane, connect them with segments of minimum total length such that there is a path
# between any two points.
# Input Format: The first line contains the number n of points. Each of the following n lines defines a point (x_i,y_i).
# Constraints: 1 ≤ n ≤ 200; −10**3 ≤ x_i,y_i ≤ 10**3 are integers. All points are pairwise different, no three points lie on the same
# line.
# Output Format: Output the minimum total length of segments. The absolute value of the difference between the answer of your
# program and the optimal value should be at most 10**−6. To ensure this, output your answer with at least seven digits after the
# decimal point (otherwise your answer, while being computed correctly, can turn out to be wrong because of rounding issues).

# The following problem solved using disjoint sets and it's properties
# The program returns the shortest distance to build the roads and the optimal distance edges with 0-based indexing
# Sample 1: Input: 5
#                  0 0
#                  0 2
#                  1 1
#                  3 0
#                  3 2
#           Output: 7.064495102


import sys
import math
class dis_set:
    def __init__(self):
        self.parent = [x for x in range(1, n+1)]
        self.rank = [1 for i in range(n)]
    def make_set(self, i):
        self.parent[i] = i
        self.rank[i] = 0
    def Find(self, i):
        while i != self.parent[i]:
            i = self.parent[i]
        return i
    def Union(self, i, j):
        i_id, j_id = self.Find(i), self.Find(j)
        if i_id == j_id:
            return
        if self.rank[i_id] > self.rank[j_id]:
            self.parent[j_id] = i_id
        else:
            self.parent[i_id] = j_id
            if self.rank[i_id] == self.rank[j_id]:
                self.rank[j_id] += 1

def get_distances(coor1, coor2):
    return float(math.sqrt((coor1[0] - coor2[0])**2 + (coor1[1] - coor2[1])**2))

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    nodes_coordinates = []
    nodes = [i for i in range(1, n+1)]
    for i, j in zip(x, y):
        nodes_coordinates.append([i, j])
    edges_weights = []
    for i in range(n):
        for j in range(i, n):
            if i != j:
                edges_weights.append([i, j, get_distances(nodes_coordinates[i], nodes_coordinates[j])])
    edges_sorted_weights = sorted(edges_weights, key=lambda x: x[2])
    disjoint_set = dis_set()
    for x in range(n):
        disjoint_set.make_set(x)
    X = []
    total_distance = 0
    for u, v, w in edges_sorted_weights:
        if disjoint_set.Find(u) != disjoint_set.Find(v):
            X.append([u, v])
            total_distance += w
            disjoint_set.Union(u, v)
    print(total_distance)
    print(X)

