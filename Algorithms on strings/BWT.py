


def BWT():
    text = input()
    l = len(text)
    M = []
    for i in range(l):
	    M.append(text[i:]+text[:i])
    M.sort()
    
    result = ""
    for row in M:
	    result += row[-1]
    return result
