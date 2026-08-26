import time

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]

    left = []
    right = []

    for i in arr[1:]:
        if i < pivot:
            left.append(i)
        else:
            right.append(i)

    return quick_sort(left) + [pivot] + quick_sort(right)


# User input
n = int(input("Enter number of elements: "))

arr = []
for i in range(n):
    element = int(input(f"Enter element {i + 1}: "))
    arr.append(element)

# Execution time
start = time.perf_counter()

sorted_arr = quick_sort(arr)

end = time.perf_counter()

print("Original array:", arr)
print("Sorted array:", sorted_arr)
print("Execution time:", end - start, "seconds")
