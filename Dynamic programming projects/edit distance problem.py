# python3


import numpy as np

def edit_distance(A, B):
    D = np.zeros((len(A)+1, len(B)+1))
    for i in range(D.shape[0]):
        D[i][0] = i
    for j, ele in enumerate(D[0][:]):
        D[0][j] = j
    for j in range(1, len(B)+1):
        for i in range(1, len(A)+1):
            insertion = D[i][j-1] + 1
            deletion = D[i-1][j] + 1
            match = D[i-1][j-1]
            mismatch = D[i-1][j-1] + 1
            if A[i-1] == B[j-1]:
                D[i][j] = min(insertion, deletion, match)
            else:
                D[i][j] = min(insertion, deletion, mismatch)
    return int(D[i][j])



