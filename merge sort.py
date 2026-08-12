import time

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


# User input
n = int(input("Enter number of elements: "))

arr = []
for i in range(n):
    value = int(input(f"Enter element {i + 1}: "))
    arr.append(value)

print("Original array:", arr)

# Start execution time
start = time.perf_counter()

sorted_array = merge_sort(arr)

# End execution time
end = time.perf_counter()

print("Sorted array:", sorted_array)
print("Execution time:", end - start, "seconds")
