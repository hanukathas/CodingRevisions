def coin_change(amt: int, coins: list, mem: dict):
    if amt == 0:
        return 0
    elif amt in mem:
        return mem[amt]
    elif amt < 0:
        return float('inf')

    min_count = float('inf')

    for coin in coins:
        result = coin_change(amt=amt-coin, coins=coins, mem=mem)
        if result != float('inf'):
            min_count = min (min_count, result+1)

    mem[amt] = min_count
    return mem[amt]

if __name__ == '__main__':
    print(coin_change(12, [1,5,10], {}))





