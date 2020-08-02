def points_on_segments():
    sets = []
    n = int(input())
    for i in range(n):
        start, end = list(map(int, input().split()))
        cur = set()
        for j in range(start, end+1):
            cur.add(j)
        if len(sets) == 0:
            sets.append(cur)
        k = 0
        while k < len(sets):
            if len(sets[k].intersection(cur)) != 0:
                sets[k] = sets[k].intersection(cur)
                break
            else:
                k += 1
        if k == len(sets):
            sets.append(cur)
    ans1 = len(sets)
    ans2 = []
    for s in sets:
        ans2.append(s.pop())
    print(ans1)
    print(" ".join(list(map(str, ans2))))
    return