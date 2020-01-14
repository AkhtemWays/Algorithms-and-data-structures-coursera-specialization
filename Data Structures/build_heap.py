# python3
import math
class HeapBuilder:
    def __init__(self):
        self.swaps = []
        self.data = []

    def ReadData(self):
        n = int(input())
        self.data = [-1] # the following 2 lines are done in order to
        self.data += [int(s) for s in input().split()] # maintain 1-based indexing
        assert n == len(self.data) - 1

    def WriteAnswer(self):
        print(len(self.swaps))
        for swap in self.swaps:
            print(swap[0], swap[1])

    def SiftDown(self, i):
        min_index = i
        leftchild = 2 * i
        rightchild = 2 * i + 1

        if leftchild <= len(self.data) - \
                1 and self.data[leftchild] < self.data[min_index]:
            min_index = leftchild
        if rightchild <= len(self.data) - \
                1 and self.data[rightchild] < self.data[min_index]:
            min_index = rightchild

        if i != min_index:
            self.swaps.append((i - 1, min_index - 1))
            self.data[i], self.data[min_index] = self.data[min_index], self.data[i]
            self.SiftDown(min_index)

    def Build_heap(self):
        for i in range(math.floor((len(self.data)-1)/2), 0, -1):
            self.SiftDown(i)

    def Solve(self):
        self.ReadData()
        self.Build_heap()
        self.WriteAnswer()


if __name__ == '__main__':
    heap_builder = HeapBuilder()
    heap_builder.Solve()