# Iterative Approach to Calculate Fibonacci Numbers

def fibonacci_iterative(n):
    # Base cases for Fibonacci sequence
    if n <= 1:
        return n

    # Initialize variables for the first two Fibonacci numbers
    fib_minus_2 = 0
    fib_minus_1 = 1

    # Calculate the Fibonacci numbers iteratively
    for i in range(2, n + 1):
        current_fib = fib_minus_1 + fib_minus_2
        fib_minus_2, fib_minus_1 = fib_minus_1, current_fib

    return fib_minus_1

n = 10  # Change this to the desired Fibonacci number

# Calculate Fibonacci number using the iterative method
result = fibonacci_iterative(n)
print(f"Fibonacci({n}) using iterative method: {result}")

# Time Complexity Analysis:
# Time Complexity: O(n)
# The iterative approach calculates Fibonacci numbers from the bottom up, starting with the base cases and using a loop to calculate each Fibonacci number only once. This results in a linear time complexity.

# Space Complexity Analysis:
# Space Complexity: O(1)
# The iterative approach uses a constant amount of memory since it doesn't rely on function call stacks or recursion. It only requires a few variables to store intermediate results.

"""
**Recursion:**
1. **Method**: Recursion is a programming technique where a function calls itself in order to solve a problem. It breaks a problem into smaller, similar subproblems.
2. **Control Flow**: It uses a function call stack to keep track of multiple recursive function calls. Each call is added to the stack, and the program returns from each call when a base case is met.
3. **Termination**: It requires a base case or a set of base cases to stop the recursive calls. Without a base case, recursion can result in an infinite loop.
4. **Memory Usage**: Recursive functions use memory to store intermediate results and function call information, which can lead to stack overflow errors if the recursion depth is too deep.
5. **Readability**: Recursive code can sometimes be more elegant and easier to understand, especially for problems that have a recursive structure.

**Iteration:**
1. **Method**: Iteration is a programming technique where a set of instructions is repeated in a loop. It involves explicit control structures like "for" and "while" loops.
2. **Control Flow**: It uses loops to repeat a block of code until a specific condition is met. There is no function call stack, and the flow of control is more explicit.
3. **Termination**: It relies on loop conditions or explicit exit conditions to stop execution. There is no need for a base case like in recursion.
4. **Memory Usage**: Iteration usually consumes less memory than recursion because there's no need to store function call information. It is less likely to lead to stack overflow errors.
5. **Readability**: Iterative code can be more verbose, especially for problems that have a repetitive structure. It may require more lines of code compared to recursive solutions.

**Use Cases:**

- **Recursion** is often used when the problem can be naturally divided into smaller, similar subproblems (e.g., recursive algorithms for tree traversal or dynamic programming problems).

- **Iteration** is commonly used when you need to perform a specific action repeatedly for a fixed number of times or as long as a certain condition is met (e.g., looping through an array or implementing iterative algorithms like sorting or searching).
"""
