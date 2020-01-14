# python3



def create_array(money):
    return [i for i in range(money+1)]

def change(money):
    coins = [1, 3, 4]
    min_num_of_change = create_array(money)
    for m in range(1, money+1):
        for i in range(len(coins)):
            if m >= coins[i]:
                NumCoins = min_num_of_change[m-coins[i]] + 1
                if NumCoins < min_num_of_change[m]:
                    min_num_of_change[m] = NumCoins
    return min_num_of_change[money]


if __name__ == '__main__':
    amount = int(input())
    print(change(amount))
