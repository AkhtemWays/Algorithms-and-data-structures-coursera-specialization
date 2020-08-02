def InverseBWT():
	# write your code here
    bwt = input()
    A, C, G , T = 1, 1, 1, 1
    lastColunm = []
    for c in bwt:
    	if c == '$':
    		lastColunm.append(('$', 0))
    	elif c == 'A':
    		lastColunm.append(('A', A))
    		A += 1
    	elif c == 'C':
    		lastColunm.append(('C', C))
    		C += 1
    	elif c == 'G':
    		lastColunm.append(('G', G))
    		G += 1
    	else:
    		lastColunm.append(('T', T))
    		T += 1
    firstColunm = sorted(lastColunm)
    firstToLast = {}
    for i in range(len(firstColunm)):
    	firstToLast[firstColunm[i]] = lastColunm[i]
    result = ""
    nextChar = ('$', 0)
    while len(result) < len(firstColunm):
    	result += nextChar[0]
    	nextChar = firstToLast[nextChar]
    result = result[::-1]
    return result

# print(InverseBWT())