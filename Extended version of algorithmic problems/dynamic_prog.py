def money_change(money, coins=[1, 3, 7, 8]):
    min_coins = [0]
    coins_to_change = [[] for i in range(money+1)]
    

    for m in range(1, money+1):
        min_coins.append(float('inf'))
        for coin in coins:
            if m >= coin:
                num_coins = min_coins[m - coin] + 1
                if num_coins <= min_coins[m]:
                    min_coins[m] = num_coins
                    new_coins = coins_to_change[m - coin].copy()
                    new_coins.append(coin)
                    coins_to_change[m] = new_coins



                    
    return min_coins[-1], coins_to_change[-1]


print(money_change(13))

            


def prim_calc(n):
    min_num_ops = [n]*n
    min_num_ops[0] = 0
    ops = [1, 2, 3]
    
    for i in range(n-1):
        
        for op in ops:
            if op == 1:
                n_tmp = (i + 1) * 3
            elif op == 2:
                n_tmp = (i + 1) * 2
            elif op == 3:
                n_tmp = (i + 1) + 1
            
            num_ops = min_num_ops[i] + 1
            idx = n_tmp - 1
            if n_tmp <= n and num_ops < min_num_ops[idx]:
                min_num_ops[idx] = num_ops
                
    return min_num_ops

# print(prim_calc(28))


def edit_distance(s1, s2):
    matrix = np.zeros((len(s1) + 1, len(s2) + 1))
    for j in range(len(s2) + 1):
        matrix[0, j] = j
    for i in range(len(s1) + 1):
        matrix[i, 0] = i
    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            if s1[i-1] == s2[j-1]:
                deletion = matrix[i-1, j]
                insertion = matrix[i, j-1]
                match = matrix[i-1, j-1]
                matrix[i, j] = min(match, insertion, deletion)
            elif s1[i-1] != s2[j-1]:
                deletion = matrix[i-1, j]
                insertion = matrix[i, j-1]
                match = matrix[i-1, j-1]
                matrix[i, j] = min(match, insertion, deletion) + 1
    return matrix



# print(edit_distance('editing', 'distance'))

def long_com_subseq(s1, s2):
    matrix = np.zeros((len(s1) + 1, len(s2) + 1))
    
    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            if s1[i-1] == s2[j-1]:
                deletion = matrix[i-1, j]
                insertion = matrix[i, j-1]
                match = matrix[i-1, j-1]
                matrix[i, j] = match + 1
            elif s1[i-1] != s2[j-1]:
                deletion = matrix[i-1, j]
                insertion = matrix[i, j-1]
                match = matrix[i-1, j-1]
                matrix[i, j] = max(match, insertion, deletion)
    return matrix


# print(long_com_subseq('gxtxayb', 'aggtab'))
import numpy as np
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