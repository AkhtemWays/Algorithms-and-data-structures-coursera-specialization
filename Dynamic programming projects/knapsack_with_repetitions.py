

def knapsack(): # with repetitions
    W, n = list(map(int, input().split()))
    golds = list(map(int, input().split()))
    matrix = np.zeros((n+1, W+1))
    for i in range(1, n+1):
        for w in range(1, W+1):
            matrix[i, w] = matrix[i - 1, w]
            if golds[i-1] <= w:
                val = matrix[i - 1, w - golds[i-1]] + golds[i-1]
                if matrix[i, w] < val:
                    matrix[i, w] = val
    return matrix
# print(knapsack())