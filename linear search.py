import time


def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1


n = int(input("Enter the number of elements: "))

arr = []
print("Enter the elements:")
for i in range(n):
    arr.append(int(input()))

key = int(input("Enter the element to search: "))

start_time = time.perf_counter()


result = linear_search(arr, key)


end_time = time.perf_counter()


if result != -1:
    print(f"\nElement {key} found at index {result}.")
else:
    print(f"\nElement {key} not found.")

print(f"\nExecution Time: {end_time - start_time:.10f} seconds")


print("\nTime Complexity:")
print("Best Case    : O(1)")
print("Average Case : O(n)")
print("Worst Case   : O(n)")
print("Space Complexity: O(1)")
