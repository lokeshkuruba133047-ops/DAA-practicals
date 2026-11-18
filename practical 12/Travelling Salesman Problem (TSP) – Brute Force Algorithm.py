import random
import time
from itertools import permutations

cities = ['A', 'B', 'C', 'D']
n = len(cities)

graph = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(i + 1, n):
        cost = random.randint(1, 50)
        graph[i][j] = cost
        graph[j][i] = cost

print("COST MATRIX:")
print("    ", *cities)

for i in range(n):
    print(cities[i], graph[i])

start_time = time.time()

minimum_cost = float('inf')
best_path = []

print("\nALL POSSIBLE PATHS AND COSTS:")

for path in permutations(range(1, n)):
    route = (0,) + path + (0,)
    total_cost = 0

    for i in range(len(route) - 1):
        total_cost += graph[route[i]][route[i + 1]]

    print(" -> ".join(cities[i] for i in route),
          "| Cost:", total_cost)

    if total_cost < minimum_cost:
        minimum_cost = total_cost
        best_path = route

end_time = time.time()

print("\nOPTIMAL PATH:")
print(" -> ".join(cities[i] for i in best_path))

print("\nMINIMUM COST:", minimum_cost)

print("\nPATH-WISE COST:")

for i in range(len(best_path) - 1):
    a = best_path[i]
    b = best_path[i + 1]
    print(cities[a], "->", cities[b],
          "Cost:", graph[a][b])

print("\nExecution Time:", end_time - start_time)
print("Time Complexity: O(n!)")
print("Space Complexity: O(n)")
