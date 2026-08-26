1. Bubble Sort
Summary:

Bubble Sort repeatedly compares adjacent elements and swaps them if they are in the wrong order. After each pass, the largest element moves to its correct position at the end of the array. This process continues until the array becomes sorted.

Algorithm:
Start from the first element.
Compare adjacent elements.
Swap if left element > right element.
Repeat for all elements.
Continue passes until sorted.
Time Complexity:
Best Case: O(n)
Average Case: O(n²)
Worst Case: O(n²)
Space Complexity:
O(1)

2. Insertion Sort
Summary:

Insertion Sort builds the sorted array one element at a time. It picks an element and inserts it into its correct position among already sorted elements.

Algorithm:
Consider the first element as sorted.
Pick the next element.
Compare with previous elements.
Insert at correct position.
Repeat until all elements are sorted.
Time Complexity:
Best Case: O(n)
Average Case: O(n²)
Worst Case: O(n²)
Space Complexity:
O(1)

3. Selection Sort
Summary:

Selection Sort repeatedly finds the minimum element from the unsorted part and places it at the beginning of the sorted part.

Algorithm:
Find the minimum element.
Swap it with the first unsorted element.
Move boundary of sorted array.
Repeat until all elements are sorted.
Time Complexity:
Best Case: O(n²)
Average Case: O(n²)
Worst Case: O(n²)
Space Complexity:
O(1)
Loading

4. Merge Sort
Summary:

Merge Sort uses the Divide and Conquer technique. It divides the array into smaller parts, sorts them recursively, and merges them back into a sorted array.

Algorithm:
Divide array into two halves.
Recursively sort both halves.
Merge sorted halves.
Repeat until array is sorted.
Time Complexity:
Best Case: O(n log n)
Average Case: O(n log n)
Worst Case: O(n log n)
Space Complexity:
O(n)

5. Quick Sort
Summary:

Quick Sort selects a pivot element and partitions the array into elements smaller and larger than the pivot. The process is repeated recursively.

Algorithm:
Choose a pivot element.
Partition array.
Recursively sort left part.
Recursively sort right part.
Time Complexity:
Best Case: O(n log n)
Average Case: O(n log n)
Worst Case: O(n²)
Space Complexity:
O(log n)

Final Complexity Table

Algorithm	Best Case	Average Case	Worst Case	Space Complexity
Bubble Sort	O(n)	O(n²)	O(n²)	O(1)
Insertion Sort	O(n)	O(n²)	O(n²)	O(1)
Selection Sort	O(n²)	O(n²)	O(n²)	O(1)
Merge Sort	O(n log n)	O(n log n)	O(n log n)	O(n)
Quick Sort	O(n log n)	O(n log n)	O(n²)	O(log n)
