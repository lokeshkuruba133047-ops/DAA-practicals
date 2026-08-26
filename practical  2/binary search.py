import time


def binary_search(arr, key):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1

    return -1

n = int(input("Enter the number of elements: "))

arr = []
print("Enter the elements:")
for i in range(n):
    arr.append(int(input()))

arr.sort()

print("\nSorted Array:", arr)

key = int(input("Enter the element to search: "))


start_time = time.perf_counter()


result = binary_search(arr, key)

end_time = time.perf_counter()


if result != -1:
    print(f"\nElement {key} found at index {result}.")
else:
    print(f"\nElement {key} not found.")

print(f"\nExecution Time: {end_time - start_time:.10f} seconds")

print("\nTime Complexity:")
print("Best Case    : O(1)")
print("Average Case : O(log n)")
print("Worst Case   : O(log n)")
print("Space Complexity: O(1)")
