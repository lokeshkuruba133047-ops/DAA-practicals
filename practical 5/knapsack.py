def knapsack(weights, profits, W):
    n = len(weights)

    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, W + 1):

            if weights[i - 1] <= w:
                dp[i][w] = max(
                    profits[i - 1] + dp[i - 1][w - weights[i - 1]],
                    dp[i - 1][w]
                )
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][W]


n = int(input("Enter number of items: "))

weights = []
profits = []

for i in range(n):
    weight = int(input(f"Enter weight of item {i + 1}: "))
    profit = int(input(f"Enter profit of item {i + 1}: "))

    weights.append(weight)
    profits.append(profit)

W = int(input("Enter knapsack capacity: "))

result = knapsack(weights, profits, W)

print("Maximum Profit =", result)
