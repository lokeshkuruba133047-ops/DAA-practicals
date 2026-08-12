import time

def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]


n = int(input("Enter the number of elements: "))

arr = []
print("Enter the elements:")
for i in range(n):
    arr.append(int(input()))

start_time = time.perf_counter()

selection_sort(arr)


end_time = time.perf_counter()


print("\nSorted Array:")
print(arr)

print(f"\nExecution Time: {end_time - start_time:.10f} seconds")


print("\nTime Complexity:")
print("Best Case    : O(n²)")
print("Average Case : O(n²)")
print("Worst Case   : O(n²)")
print("Space Complexity: O(1)")
