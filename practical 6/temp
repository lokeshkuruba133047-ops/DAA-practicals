import time

def matrix_chain(p):
    n = len(p)
    dp = [[0] * n for _ in range(n)]

    for length in range(2, n):
        for i in range(1, n - length + 1):
            j = i + length - 1
            dp[i][j] = float('inf')

            for k in range(i, j):
                cost = dp[i][k] + dp[k+1][j] + p[i-1] * p[k] * p[j]
                dp[i][j] = min(dp[i][j], cost)

    return dp[1][n-1]



n = int(input("Enter number of matrices: "))

p = []
print("Enter dimensions:")

for i in range(n + 1):
    p.append(int(input(f"Dimension {i+1}: ")))

start = time.perf_counter()

result = matrix_chain(p)

end = time.perf_counter()

print("\nMinimum multiplication cost:", result)
print("Execution time:", end - start, "seconds")
print("Time Complexity: O(n^3)")
print("Space Complexity: O(n^2)")
