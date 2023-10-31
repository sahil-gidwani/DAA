class Item:
    def __init__(self, value, weight, index):
        self.value = value
        self.weight = weight
        self.index = index
        self.ratio = value / weight

def knapsack_branch_and_bound(values, weights, capacity):
    items = [Item(value, weight, i) for i, (value, weight) in enumerate(zip(values, weights))]
    items.sort(key=lambda x: x.ratio, reverse=True)  # Sort items by value/weight ratio (highest first)

    def get_bound(current, remaining_capacity, i):
        # Calculate the bound for the current node
        bound = current
        total_weight = 0
        while i < len(items) and total_weight + items[i].weight <= remaining_capacity:
            bound += items[i].value
            total_weight += items[i].weight
            i += 1
        if i < len(items):
            bound += (remaining_capacity - total_weight) * items[i].ratio
        return bound

    def branch_and_bound(i, current_value, current_weight, selected_items):
        nonlocal max_value, result_items

        if current_weight > capacity or i == len(items):
            return

        if current_value > max_value:
            max_value = current_value
            result_items = selected_items.copy()

        bound = get_bound(current_value, capacity - current_weight, i)

        if bound > max_value:
            selected_items.append(items[i].index)
            branch_and_bound(i + 1, current_value + items[i].value, current_weight + items[i].weight, selected_items)
            selected_items.pop()
            branch_and_bound(i + 1, current_value, current_weight, selected_items)

    max_value = 0
    result_items = []
    branch_and_bound(0, 0, 0, [])

    return max_value, result_items

# Example usage
if __name__ == "__main__":
    values = [10, 40, 30, 50]
    weights = [5, 4, 6, 3]
    capacity = 10

    # Solve the 0-1 Knapsack Problem using Branch and Bound
    max_value, selected_items = knapsack_branch_and_bound(values, weights, capacity)

    # Output the results
    print(f"Maximum value in the knapsack: {max_value}")
    print("Selected items:")
    for i in selected_items:
        print(f"Item {i + 1} (Value: {values[i]}, Weight: {weights[i]})")

# Time Complexity Analysis:
# - The Branch and Bound method's time complexity is generally exponential in the worst case,
#   but it often performs much better than brute-force methods due to pruning.
# - The `get_bound` function helps reduce the number of branches explored and is essential for its performance.

# Space Complexity Analysis:
# - The space complexity of this implementation is O(n) due to the recursion stack, where n is the number of items in the knapsack problem.
