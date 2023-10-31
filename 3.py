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

"""
Fractional Knapsack, also known as the Fractional Knapsack Problem, is a classic optimization problem in computer science and mathematics. It is a variation of the Knapsack Problem, where you are given a set of items, each with a weight and a value, and a knapsack with a maximum weight capacity. The goal is to determine the most valuable combination of items to include in the knapsack without exceeding its weight capacity. In the Fractional Knapsack version, you are allowed to take fractions of items, not just whole items.

Here's a step-by-step explanation of how the Fractional Knapsack Problem works:

1. Given Data:
   - A set of items, each characterized by its weight (w[i]) and its value (v[i]).
   - A knapsack with a maximum weight capacity (W).

2. Calculate the Value-to-Weight Ratios:
   For each item, calculate the value-to-weight ratio (v[i] / w[i]). This ratio represents how much value you get for each unit of weight. Sorting the items by this ratio in descending order is a common approach.

3. Initialize Variables:
   - Initialize a variable to keep track of the total value of items selected (initially set to 0).
   - Initialize a variable to keep track of the remaining weight capacity of the knapsack (initially set to W).

4. Iterate Over Items:
   - Iterate through the sorted items (sorted by value-to-weight ratio).
   - For each item, calculate how much of it can be added to the knapsack:
     - If the entire item fits into the knapsack (i.e., w[i] <= remaining capacity), add the entire item, update the total value, and subtract its weight from the remaining capacity.
     - If the item doesn't fit entirely, calculate the fraction that can fit (remaining capacity / w[i]), add that fraction to the knapsack, update the total value, and set the remaining capacity to zero.

5. Continue the process:
   Keep iterating through the sorted items until the knapsack is full (remaining capacity is zero) or there are no more items to consider.

6. Calculate the Final Value:
   The total value obtained after filling the knapsack with items (either partially or completely) is the maximum achievable value under the given constraints.

Fractional Knapsack is a greedy algorithm because, at each step, it selects the item with the highest value-to-weight ratio, making it a locally optimal choice. This approach may or may not lead to a globally optimal solution. It is important to note that Fractional Knapsack is used when fractional parts of items can be included, which is not the case in the traditional (0/1) Knapsack Problem, where items must be taken entirely or not at all.
"""
