def fibonacci_top_down(n, memo={}):
    # Base case: If n is 0 or 1, return n.
    if n <= 1:
        return n
    
    # Check if the Fibonacci number for n is already calculated and stored in the memo dictionary.
    if n in memo:
        return memo[n]
    
    # Calculate the Fibonacci number for n recursively and store it in the memo dictionary.
    memo[n] = fibonacci_top_down(n - 1, memo) + fibonacci_top_down(n - 2, memo)
    
    return memo[n]

n = 10  # Change this to the desired Fibonacci number

# Calculate Fibonacci number using the top-down dynamic programming method
result = fibonacci_top_down(n)
print(f"Fibonacci({n}) using top-down dynamic programming method: {result}")
