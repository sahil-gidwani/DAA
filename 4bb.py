class Item:
    def __init__(self, value, weight, index):
        self.value = value
        self.weight = weight
        self.index = index
        self.ratio = value / weight  # Calculate the value-to-weight ratio for the item

def knapsack_branch_and_bound(values, weights, capacity):
    # Create a list of items, each represented by the Item class with value, weight, index, and ratio.
    items = [Item(value, weight, i) for i, (value, weight) in enumerate(zip(values, weights))]

    # Sort the items by value-to-weight ratio in descending order (highest ratio first).
    items.sort(key=lambda x: x.ratio, reverse=True)
    # print("Sorted items:")
    # for item in items:
    #     print(f"Item {item.index + 1} - Value: {item.value}, Weight: {item.weight}, Ratio: {item.ratio}")

    def get_bound(current, remaining_capacity, i):
        # Calculate the bound for the current node based on the fractional items.
        bound = current
        total_weight = 0

        while i < len(items) and total_weight + items[i].weight <= remaining_capacity:
            bound += items[i].value
            total_weight += items[i].weight
            i += 1

        if i < len(items):
            # Include a fraction of the next item to reach the remaining capacity.
            bound += (remaining_capacity - total_weight) * items[i].ratio
        
        return bound

    def branch_and_bound(i, current_value, current_weight, selected_items):
        # Declare 'max_value' and 'result_items' as nonlocal so they can be updated within the function
        nonlocal max_value, result_items
    
        # If the current weight exceeds the capacity or we have considered all items, return
        if current_weight > capacity or i == len(items):
            # print(f"Stopping at node {i}, current_value: {current_value}, current_weight: {current_weight}")
            return
    
        # If the current value is greater than the current maximum value, update the maximum value and selected items
        if current_value > max_value:
            max_value = current_value
            result_items = selected_items.copy()
        
        # print(f"Exploring node {i}, current_value: {current_value}, current_weight: {current_weight}")
    
        # Calculate the bound for the current state
        bound = get_bound(current_value, capacity - current_weight, i)
        # print(f"Bound at node {i}: {bound}")
    
        # If the bound is greater than the current maximum value, consider including the current item
        if bound > max_value:
            selected_items.append(items[i].index)  # Include the current item
            # print(f"Including item {i + 1} with value {items[i].value} and weight {items[i].weight}")
            branch_and_bound(i + 1, current_value + items[i].value, current_weight + items[i].weight, selected_items)
            selected_items.pop()  # Backtrack by excluding the current item
            # print(f"Excluding item {i + 1} with value {items[i].value} and weight {items[i].weight}")
            branch_and_bound(i + 1, current_value, current_weight, selected_items)
    
    # Initialize maximum value and selected items
    max_value = 0
    result_items = []
    
    # Start the branch and bound algorithm with the first item (index 0) and initial values
    branch_and_bound(0, 0, 0, [])
    
    # Return the maximum value and the list of selected items as the result
    return max_value, result_items


if __name__ == "__main__":
    values = [10, 40, 30, 50]
    weights = [5, 4, 6, 3]
    capacity = 10

    max_value, selected_items = knapsack_branch_and_bound(values, weights, capacity)

    print(f"Maximum value in the knapsack: {max_value}")
    print("Selected items:")
    for i in selected_items:
        print(f"Item {i + 1} (Value: {values[i]}, Weight: {weights[i]})")

# Time Complexity Analysis:
# The time complexity of the knapsack_branch_and_bound function can be summarized as O(n*log(n)) for the sorting step 
# in the best case, and potentially exponential (O(2^n)) in the worst case. The actual time taken to solve a specific instance
# of the problem will depend on the characteristics of the input data and the effectiveness of the pruning.

# Space Complexity Analysis:
# - The space complexity of this implementation is O(n) due to the recursion stack, where n is the number of items in the knapsack problem.

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

Branch and Bound is a widely used algorithmic technique for solving optimization problems, particularly in combinatorial and discrete domains. It systematically explores the solution space by dividing it into smaller subproblems and bounding the search to find the best possible solution efficiently. It is often used when the problem cannot be solved using greedy or dynamic programming approaches. Here's an explanation of the Branch and Bound technique:

1. **Optimization Problems:** Branch and Bound is primarily used for optimization problems, where the goal is to find the best solution among a set of possible solutions. These problems often involve maximizing or minimizing an objective function under certain constraints.

2. **Systematic Search:** The key idea behind Branch and Bound is to explore the solution space in a systematic manner, similar to a tree search. It involves branching and bounding the search space to efficiently find the optimal solution.

3. **Main Components:**
   - **Branching:** At each node of the search tree, the algorithm makes branching decisions to divide the problem into smaller subproblems. These decisions often involve selecting one of several possible choices for a variable or element of the solution.
   - **Bounding:** The algorithm establishes bounds or estimates for each node in the search tree, allowing it to determine whether the subproblem at that node has the potential to lead to a better solution than the current best solution found. This helps in pruning unfruitful branches.
   - **Selection:** Branch and Bound maintains a priority queue or a list of nodes to be explored, and it selects nodes based on their bounds and estimates to ensure that more promising nodes are explored first.
   - **Completion:** The algorithm continues to branch and bound until it has explored the entire search tree or until the bounds of remaining unexplored nodes are worse than the best solution found so far.

4. **Termination and Pruning:** The algorithm terminates when it has explored the entire search space or when it determines that there cannot be a better solution than the current best solution. This pruning is achieved by comparing the bounds of nodes with the best solution found so far and skipping those nodes that are guaranteed to be suboptimal.

5. **Applications:** Branch and Bound can be applied to various optimization problems, including:
   - Traveling Salesman Problem (TSP)
   - 0/1 Knapsack Problem
   - Job Scheduling
   - Graph Coloring
   - Cutting Stock Problem
   - Combinatorial Auctions
   - Integer Linear Programming

6. **Complexity Analysis:** The efficiency of Branch and Bound depends on the problem's characteristics and the quality of the bounding function. In the worst case, it explores all nodes in the search tree, resulting in exponential time complexity. However, effective bounding strategies and heuristics can greatly improve its efficiency.

7. **Trade-offs:** Branch and Bound may not always guarantee the optimal solution, but it is designed to find good solutions efficiently. The quality of the solution found can depend on the quality of bounding estimates and the branching strategy used.

8. **Variations:** There are variations of Branch and Bound, such as Branch and Bound with Subproblems, which is used to solve larger problems by dividing them into smaller subproblems that can be solved optimally.

In summary, Branch and Bound is a powerful technique for solving optimization problems. It systematically explores the solution space by dividing it into smaller subproblems and bounding the search to find the best possible solution efficiently, making it a valuable tool in combinatorial and discrete optimization.
"""
