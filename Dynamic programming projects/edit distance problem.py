# python3

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