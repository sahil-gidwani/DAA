# Dynamic Programming Bottom-Up (Tabulation) Approach to Calculate Fibonacci Numbers

def fibonacci_bottom_up(n):
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

"""
Dynamic programming (DP) is a powerful technique for solving problems by breaking them down into smaller subproblems and reusing the solutions to those subproblems. Two common approaches to implementing dynamic programming are "bottom-up" (also known as iterative or tabulation) and "top-down" (also known as recursive or memoization). Both approaches have their advantages and are suitable for different scenarios. Here's a comparison of bottom-up and top-down dynamic programming:

**1. Bottom-Up Dynamic Programming (Iterative / Tabulation):**

   - **Iterative Approach:** In the bottom-up approach, you start solving the problem by solving its subproblems first, and you build up the solution from smaller subproblems to larger ones iteratively.
   
   - **State Transition:** You typically use an array (or table) to store the results of subproblems, and you fill in this table in a bottom-up manner, progressing from the smallest subproblem to the original problem.
   
   - **Advantages:**
     - Efficient use of memory: Since you only store the results of subproblems once and in a specific order, you can optimize memory usage.
     - No risk of exceeding the stack limit: This approach avoids stack overflow issues for problems with deep recursion.
     - Typically faster: It can be more efficient because it avoids function call overhead and has better cache performance.

   - **Disadvantages:**
     - Not always intuitive: Constructing the table and state transitions can be less intuitive compared to the recursive approach.
     - Lack of elegance: The code might appear less elegant, as you're explicitly managing the table.

**2. Top-Down Dynamic Programming (Recursive / Memoization):**

   - **Recursive Approach:** In the top-down approach, you start by solving the original problem recursively. However, you use memoization (caching) to store the results of subproblems to avoid redundant computations.
   
   - **Memoization:** Memoization involves caching (storing) the results of subproblems in a data structure, such as a dictionary or an array, so that if the same subproblem is encountered again, you can simply look up the cached result rather than recomputing it.
   
   - **Advantages:**
     - More intuitive: Recursive solutions can closely mirror the mathematical formulation of the problem, making them easier to understand and code.
     - Readability: Memoization allows you to maintain a clear separation between the problem's logic and the caching of results.
     - Elegance: Recursive solutions can be more elegant and resemble the problem's mathematical structure.

   - **Disadvantages:**
     - Risk of stack overflow: For problems with deep recursion, you may encounter stack overflow errors.
     - Potentially less efficient: Due to the function call overhead and the potential for redundant recursive calls, memoization can be less efficient in terms of time and space for some problems.

**When to Choose Each Approach:**

1. **Bottom-Up (Iterative) DP:**
   - Choose the bottom-up approach when you have identified the structure of your problem and can efficiently construct a table to store results.
   - Use it for problems with well-defined, nested subproblems.
   - It's particularly useful when you want to optimize memory usage and avoid stack overflow errors.

2. **Top-Down (Recursive) DP with Memoization:**
   - Choose the top-down approach when the recursive structure of the problem is more apparent and directly mirrors the problem's mathematical formulation.
   - Use it for problems where caching (memoization) simplifies the solution.
   - It's often the more intuitive choice when the mathematical formulation is clear.

In practice, the choice between bottom-up and top-down DP may also depend on the specific problem and personal preference. Some problems are more naturally solved with one approach over the other. Additionally, hybrid approaches that combine both techniques can be effective in certain scenarios.
"""
