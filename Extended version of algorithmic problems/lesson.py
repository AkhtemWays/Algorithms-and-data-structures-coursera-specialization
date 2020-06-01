from itertools import combinations
import numpy as np
def edit_distance(s1, s2, wdel, wins, wsub):
    matrix = [[0 for j in range(len(s2) + 1)] for i in range(len(s1) + 1)]

    for j in range(len(s2) + 1):

        matrix[0][j] = j
    for i in range(len(s1) + 1):

        matrix[i][0] = i
    
    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            if s1[i-1] == s2[j-1]:
                deletion = matrix[i-1][j] + wdel
                insertion = matrix[i][j-1] + wins
                match = matrix[i-1][j-1]
                optimal = min(match, insertion, deletion)
                if optimal == match: matrix[i][j] = optimal
                else: matrix[i][j] = optimal
                
            elif s1[i-1] != s2[j-1]:
                deletion = matrix[i-1][j]
                insertion = matrix[i][j-1]
                substitution = matrix[i-1][j-1]
                matrix[i][j] = min(substitution, insertion, deletion)
                
                

    return matrix[-1][-1]

print(edit_distance('goodaga', 'badgh', 2, 1, 3))





def edistance_substring2(s1, s2):
    matrix = [[0 for j in range(len(s2) + 1)] for i in range(len(s1) + 1)]

    for j in range(len(s2) + 1):

        matrix[0][j] = j
    for i in range(len(s1) + 1):

        matrix[i][0] = i
    
    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            if s1[i-1] == s2[j-1]:
                deletion = matrix[i-1][j]
                insertion = matrix[i][j-1]
                match = matrix[i-1][j-1]
                optimal = min(match, insertion, deletion)
                if optimal == match: matrix[i][j] = optimal
                else: matrix[i][j] = optimal + 1 
            elif s1[i-1] != s2[j-1]:
                deletion = matrix[i-1][j]
                insertion = matrix[i][j-1]
                substitution = matrix[i-1][j-1]
                matrix[i][j] = min(substitution, insertion, deletion) + 1
    for i in matrix:
        print(i)
    return
    #  "" A  G  A  T
# G [0, 1, 2, 3, 4]
# G [1, 1, 1, 2, 3]
# T [2, 1, 2, 2, 3]
# V [3, 2, 2, 2, 3]
# A [4, 3, 3, 3, 2]

def edistance_substring(s1, s2):
    all_other_combs = []

    for i in range(1, len(s1)):
        if s1[:i] + s1[i+1:] not in all_other_combs:
            all_other_combs.append(s1[:i] + s1[i+1:])
    result = len(s2)

    for substr in all_other_combs:
        check = edistance_substring2(substr, s2)
        if result > check:
            result = check
    return result
                
    

# acd bcd bad bac
# print(edistance_substring2('bacd', 'abcd'))





def voc_to_list(vocabulary):
    # 
    max_len = max([len(w) for w in vocabulary])
    lengths = [0] * (max_len + 1) # 
    for i, w in enumerate(vocabulary):
        lengths[i+1] = len(w)
    return lengths

def passwords(L, vocabulary):
    lengths = voc_to_list(vocabulary)
    k = len(lengths)
    tbl = [0] * (L + 1)
    for i in range(L + 1):
        if i < k:
            tbl[i] = lengths[i]
        for j in range(min(k, i)):
            tbl[i] = sum([2*tbl[m] + 1 if 2*tbl[m] + 1 <= i else 1 for m in range(1, j)])
            # tbl[i] = tbl[i-1] + 1
    return sum(tbl)
print(passwords(5, ['hello', 'oh' + '_' + 'oh']))














