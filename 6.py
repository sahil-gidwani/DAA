import random
import time

# Deterministic Quick Sort
def deterministic_quick_sort(arr):
    if len(arr) <= 1:
        return arr

    # Choose the pivot element as the middle element
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    # Recursively sort the left and right subarrays
    return deterministic_quick_sort(left) + middle + deterministic_quick_sort(right)

# Randomized Quick Sort
def randomized_quick_sort(arr):
    if len(arr) <= 1:
        return arr

    # Randomly choose a pivot element
    pivot = random.choice(arr)
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    # Recursively sort the left and right subarrays
    return randomized_quick_sort(left) + middle + randomized_quick_sort(right)

# Measure execution time of a sorting algorithm
def measure_time(sort_function, arr):
    start_time = time.time()
    sorted_arr = sort_function(arr)
    end_time = time.time()
    return sorted_arr, end_time - start_time

# Generate a random list of integers for testing
arr = [random.randint(1, 1000) for _ in range(1000)]

# Analyze Deterministic Quick Sort
det_sorted_arr, det_time = measure_time(deterministic_quick_sort, arr.copy())
print("Deterministic Quick Sort:")
print(f"Time taken: {det_time:.6f} seconds")  # Time taken for sorting
print(f"Is Sorted: {det_sorted_arr == sorted(arr)}")  # Check if the sorting is correct

# Analyze Randomized Quick Sort
rand_sorted_arr, rand_time = measure_time(randomized_quick_sort, arr.copy())
print("\nRandomized Quick Sort:")
print(f"Time taken: {rand_time:.6f} seconds")  # Time taken for sorting
print(f"Is Sorted: {rand_sorted_arr == sorted(arr)}")  # Check if the sorting is correct

# Time Complexity Analysis:
# - Deterministic Quick Sort:
#   - Average-case time complexity: O(n*log(n)) - Pivot strategy divides the list into nearly equal parts.
#   - Worst-case time complexity: O(n^2) - Occurs when the pivot is always the minimum or maximum element.
#   - Best-case time complexity: O(n) - Occurs when the pivot divides the list into roughly equal halves.
# - Randomized Quick Sort:
#   - Average-case time complexity: O(n*log(n)) - Random pivot selection reduces the likelihood of worst-case scenarios.
#   - Worst-case time complexity: O(n^2) - Unlikely to occur in practice.
#   - Best-case time complexity: O(n) - Pivot divides the list into roughly equal halves.

# Space Complexity Analysis:
# - Both variants have a space complexity of O(log(n)) in the average case, corresponding to the function call stack.
# - In the worst case, space complexity can be O(n) for deterministic Quick Sort due to unbalanced partitions, but it remains O(log(n)) on average.
