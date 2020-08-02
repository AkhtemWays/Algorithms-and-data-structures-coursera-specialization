def money_change(money, coins=[1, 3, 7, 8]):
    min_coins = [0]
    coins_to_change = [[] for i in range(money+1)]
    

    for m in range(1, money+1):
        min_coins.append(float('inf'))
        for coin in coins:
            if m >= coin:
                num_coins = min_coins[m - coin] + 1
                if num_coins <= min_coins[m]:
                    min_coins[m] = num_coins
                    new_coins = coins_to_change[m - coin].copy()
                    new_coins.append(coin)
                    coins_to_change[m] = new_coins



                    
    return min_coins[-1], coins_to_change[-1]


print(money_change(13))
