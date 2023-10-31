# Iterative (Non-Recursive) Approach to Calculate Fibonacci Numbers

def fibonacci_iterative(n):
    # Initialize an array to store Fibonacci numbers
    fib = [0, 1]

    # Calculate and store Fibonacci numbers up to n
    for i in range(2, n + 1):
        next_fib = fib[i - 1] + fib[i - 2]
        fib.append(next_fib)

    # Return the Fibonacci number for n
    return fib[n]

n = 10  # Change this to the desired Fibonacci number

# Calculate Fibonacci number using the iterative method
result = fibonacci_iterative(n)
print(f"Fibonacci({n}) using iterative method: {result}")

# Time Complexity Analysis:
# Time Complexity: O(n)
# The non-recursive approach calculates Fibonacci numbers in a loop that iterates n times.

# Space Complexity Analysis:
# Space Complexity: O(n)
# It stores all Fibonacci numbers up to n in a list, resulting in a linear space complexity.
