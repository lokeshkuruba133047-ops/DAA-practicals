def coin_change(coins, amount):

    dp = [float('inf')] * (amount + 1)


    dp[0] = 0

    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    if dp[amount] == float('inf'):
        return -1
    return dp[amount]


n = int(input("Enter number of coins: "))

coins = []
for i in range(n):
    coin = int(input(f"Enter coin {i + 1}: "))
    coins.append(coin)

amount = int(input("Enter target amount: "))

result = coin_change(coins, amount)

print("Minimum number of coins:", result)
