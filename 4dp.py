# Function to solve the 0-1 Knapsack Problem using dynamic programming
def knapsack_01(values, weights, capacity):
    n = len(values)

    # Initialize a table to store the maximum value for each (item, capacity) combination
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Populate the table using dynamic programming
    for i in range(n + 1):
        for w in range(capacity + 1):
            if i == 0 or w == 0:
                dp[i][w] = 0
            # The previous item's weight is less than the current capacity (w) so try to include it
            elif weights[i - 1] <= w:
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    # Find the items included in the optimal solution
    selected_items = []
    i, w = n, capacity
    while i > 0 and w > 0:
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(i - 1)
            w -= weights[i - 1]
        i -= 1

    selected_items.reverse()

    return dp[n][capacity], selected_items

# Example usage
if __name__ == "__main__":
    values = [10, 40, 30, 50]
    weights = [5, 4, 6, 3]
    capacity = 10

    max_value, selected_items = knapsack_01(values, weights, capacity)

    print(f"Maximum value in the knapsack: {max_value}")
    print("Selected items:")
    for i in selected_items:
        print(f"Item {i + 1} (Value: {values[i]}, Weight: {weights[i]})")

# Time Complexity Analysis:
# - Filling the dp table: O(n*capacity), where n is the number of items and capacity is the knapsack capacity.

# Space Complexity Analysis:
# - Space required for the dp table: O(n*capacity), where n is the number of items and capacity is the knapsack capacity.

"""
The 0/1 Knapsack Problem is a classic optimization problem in computer science and mathematics. It is a problem of combinatorial optimization where the goal is to select a combination of items, each with a given weight and value, to maximize the total value while not exceeding a given weight limit (the capacity of the knapsack). The term "0/1" indicates that for each item, you can either choose to include it (1) or exclude it (0) in the knapsack, meaning you can't take a fractional part of an item. In other words, it's a binary choice for each item.

Here's a formal description of the problem:

- You have a set of n items, each with a specific weight (w_i) and value (v_i).
- You have a knapsack with a maximum weight capacity (W).
- You can choose to include or exclude each item in the knapsack (0 or 1).
- The goal is to find the combination of items to include in the knapsack, such that the total weight of the selected items does not exceed W, and the total value is maximized.

Mathematically, the problem can be defined as follows:

Maximize Σ(v_i * x_i) for i = 1 to n
Subject to Σ(w_i * x_i) for i = 1 to n ≤ W
x_i = 0 or 1 for all i

Where:
- v_i is the value of item i.
- w_i is the weight of item i.
- x_i is a binary variable (0 or 1) indicating whether item i is included (1) or excluded (0) from the knapsack.
- W is the maximum weight capacity of the knapsack.

The 0/1 Knapsack Problem is known to be an NP-hard problem, meaning there is no known algorithm to solve it optimally in polynomial time for all inputs. However, dynamic programming and branch and bound algorithms can be used to find the optimal solution for relatively small instances of the problem. For larger instances, heuristics and approximation algorithms are often used to find near-optimal solutions.

This problem has various practical applications, such as resource allocation, portfolio optimization, and cutting stock problems.

-----------------------------

Dynamic programming is a problem-solving technique in computer science and mathematics used to efficiently solve problems by breaking them down into smaller overlapping subproblems and storing the results of these subproblems to avoid redundant computations. It is a powerful approach for solving optimization problems, particularly those with recursive or overlapping substructures. Here are the key principles and concepts of dynamic programming:

1. **Optimal Substructure:** Dynamic programming problems can be broken down into subproblems, and the optimal solution to the original problem can be constructed from optimal solutions to its subproblems. This is often expressed as a recursive formula or relation.

2. **Overlapping Subproblems:** In many dynamic programming problems, the same subproblems are encountered multiple times during the computation. Dynamic programming avoids redundant work by storing the results of already-solved subproblems in a data structure (usually a table or array) for later use.

3. **Memoization:** Memoization is the process of storing intermediate results (such as function values) in a data structure (often an array or dictionary) and returning the cached result when the same inputs reappear. This avoids redundant computation in recursive algorithms.

4. **Bottom-Up Approach:** Dynamic programming can be solved using either a top-down approach (recursion with memoization) or a bottom-up approach (iterative approach). In the bottom-up approach, you start by solving the smallest subproblems and build up to the original problem iteratively.

5. **State Transition:** Dynamic programming problems involve transitions from one state to another. These transitions can be represented by a recurrence relation or formula. The relation between subproblems and the order in which they are solved are crucial for finding an efficient solution.

6. **Tabulation:** In the bottom-up approach, you use a table (usually a multi-dimensional array) to store the results of subproblems. Each entry in the table corresponds to a specific state, and you fill it based on the optimal solution to smaller subproblems.

7. **Examples:** Dynamic programming is used in various problem domains, including:
   - **Fibonacci Sequence:** Calculating Fibonacci numbers using dynamic programming to avoid redundant calculations.
   - **0/1 Knapsack Problem:** Finding the most valuable combination of items to fit in a knapsack with limited capacity.
   - **Shortest Path Problems:** Finding the shortest path between nodes in a graph (e.g., Dijkstra's algorithm).
   - **Sequence Alignment:** Aligning sequences, such as DNA or protein sequences, to find the best match.
   - **Dynamic Time Warping:** Measuring the similarity between two time series sequences.
   - **Longest Common Subsequence (LCS):** Finding the longest subsequence common to two sequences.

8. **Time and Space Complexity:** The time and space complexity of dynamic programming solutions can vary depending on the specific problem and the chosen approach. While it often provides efficient solutions, dynamic programming can be computationally expensive for problems with large input sizes. Memoization and tabulation help manage time and space complexity.

Overall, dynamic programming is a versatile technique for solving a wide range of optimization problems, and its efficiency depends on how well the problem can be divided into smaller subproblems and how effectively overlapping subproblems are handled.
"""
