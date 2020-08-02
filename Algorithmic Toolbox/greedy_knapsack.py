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


