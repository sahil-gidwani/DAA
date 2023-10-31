# Function to solve the Fractional Knapsack Problem using a greedy method
def fractional_knapsack(items, capacity):
    # Calculate the value-to-weight ratio for each item
    for item in items:
        item['ratio'] = item['value'] / item['weight']

    # Sort items by their value-to-weight ratio in descending order
    items.sort(key=lambda x: x['ratio'], reverse=True)

    total_value = 0.0
    knapsack = []

    for item in items:
        if capacity == 0:
            break
        if item['weight'] <= capacity:
            knapsack.append(item)
            total_value += item['value']
            capacity -= item['weight']
        else:
            fraction = capacity / item['weight']
            item['fraction'] = fraction
            knapsack.append(item)
            total_value += item['value'] * fraction
            break

    return knapsack, total_value

# Example usage
if __name__ == "__main__":
    items = [
        {'name': 'item1', 'value': 10, 'weight': 2},
        {'name': 'item2', 'value': 5, 'weight': 3},
        {'name': 'item3', 'value': 15, 'weight': 5},
        {'name': 'item4', 'value': 7, 'weight': 7},
        {'name': 'item5', 'value': 6, 'weight': 1},
    ]

    capacity = 15
    selected_items, total_value = fractional_knapsack(items, capacity)

    print("Selected items in the knapsack:")
    for item in selected_items:
        if 'fraction' in item:
            print(f"{item['name']} - {item['fraction']:.2f}")
        else:
            print(f"{item['name']} - 1.00")

    print(f"Total value in the knapsack: {total_value}")

# Time Complexity Analysis:
# - Sorting items: O(n*log(n)), where n is the number of items.
# - Iterating through the items: O(n), where n is the number of items.
# Overall time complexity: O(n*log(n)) + O(n), which simplifies to O(n*log(n)).

# Space Complexity Analysis:
# - Space required for the sorted items: O(n), where n is the number of items.
# - Space required for the knapsack: O(n), where n is the number of items.
# Overall space complexity: O(n) + O(n), which simplifies to O(n).
