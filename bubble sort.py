
import time


def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
               
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

       
        if not swapped:
            break


n = int(input("Enter the number of elements: "))

arr = []
print("Enter the elements:")
for i in range(n):
    arr.append(int(input()))


start_time = time.perf_counter()


bubble_sort(arr)


end_time = time.perf_counter()

print("\nSorted Array:")
print(arr)

print(f"\nExecution Time: {end_time - start_time:.10f} seconds")


print("\nTime Complexity:")
print("Best Case    : O(n)")
print("Average Case : O(n²)")
print("Worst Case   : O(n²)")
print("Space Complexity: O(1)")
