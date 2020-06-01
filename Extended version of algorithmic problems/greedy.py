def knapsack_greedy():
    n, weight = list(map(int, input().split()))
    choice = {}

    for i in range(n):
        total, amount = list(map(int, input().split()))
        cost = total/amount
        choice[cost] = amount

    total_val = 0
    while weight > 0:
        best_value = max(choice.keys())
        if choice[best_value] > weight:
            total_val += best_value * weight
            break
        else:
            weight -= choice[best_value]
            total_val += choice[best_value] * best_value
        del choice[best_value]
    return total_val


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


# -------------------------------------------------------------------------------------------


def Maximum_salary():
    result = []
    n = int(input())
    digits = list(map(int, input().split()))
    
    while digits:
        
        best_possible = 0
        for digit in digits:
            
            if int(str(digit)[0]) == int(str(best_possible)[0]) and len(str(digit)) < len(str(best_possible)):      
                i = 1
                while i <= len(str(digit)) - 1:
                    if int(str(digit)[i]) > int(str(best_possible)[i]):
                        best_possible = digit
                        break
                    elif int(str(digit)[i]) < int(str(best_possible)[i]):
                        break
                    i += 1
                if i == len(str(digit)):
                    best_possible = digit
            elif int(str(digit)[0]) == int(str(best_possible)[0]) and len(str(digit)) > len(str(best_possible)):
                i = 1
                while i < len(str(best_possible)) - 1:
                    if int(str(digit)[i]) > int(str(best_possible)[i]):
                        best_possible = digit
                        break
                    elif int(str(digit)[i]) < int(str(best_possible)[i]):
                        break
                    i += 1
            elif digit > best_possible:
                best_possible = digit

        result.append(best_possible)
        digits.remove(best_possible)
    
    return "".join(list(map(str, result)))
print(Maximum_salary())
                
                
                
                






