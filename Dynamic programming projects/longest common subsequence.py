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