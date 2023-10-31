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
