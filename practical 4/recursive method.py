import time

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

n = int(input("Enter a number: "))

start = time.perf_counter()

fact = factorial(n)

end = time.perf_counter()

print("Factorial =", fact)
print("Execution Time =", end - start, "seconds")
print("Time Complexity = O(n)")
