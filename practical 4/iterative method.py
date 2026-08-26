import time

n = int(input("Enter a number: "))

start = time.perf_counter()

fact = 1
for i in range(1, n + 1):
    fact = fact * i

end = time.perf_counter()

print("Factorial =", fact)
print("Execution Time =", end - start, "seconds")
print("Time Complexity = O(n)")
