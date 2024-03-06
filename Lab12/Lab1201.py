'''Labs 12.01 Coin Exchange'''
import json
def coin_exchange(amount, coins):
    '''Coin Exchange'''
    print("Amount:", amount)
    lis, dic, total = [10, 5, 2, 1], {}, 0
    for i in lis:
        total += min(coins[i], amount//i)
        dic[i] = min(coins[i], amount//i)
        amount -= min(coins[i], amount//i) * i
    if amount <= 0:
        print("Coin exchange result:")
        for j in dic:
            print("  {} baht = {} coins".format(j, dic[j]))
        print("Number of coins:", total)
    else:
        print("Coins are not enough.")
def convert_key(data):
    """JSON"""
    return {int(k): v for k, v in data.items()}

coin_exchange(int(input()), convert_key(json.loads(input())))
