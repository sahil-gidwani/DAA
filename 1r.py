# Recursive Approach to Calculate Fibonacci Numbers

def fibonacci_recursive(n):
    # Base case: If n is 0 or 1, return n.
    if n <= 1:
        return n
    else:
        # Recursive step: Calculate Fibonacci numbers for n-1 and n-2.
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

n = 10  # Change this to the desired Fibonacci number

# Calculate Fibonacci number using the recursive method
result = fibonacci_recursive(n)
print(f"Fibonacci({n}) using recursive method: {result}")

# Time Complexity Analysis:
# Time Complexity: O(2^n)
# The recursive approach has exponential time complexity because it recalculates Fibonacci numbers repeatedly, resulting in a lot of redundant work.

# Space Complexity Analysis:
# Space Complexity: O(n)
# The recursive approach has a linear space complexity because it uses the function call stack,
# and in the worst case, there will be n function calls in the stack.
