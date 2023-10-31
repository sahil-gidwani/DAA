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

-------------------------------------

A greedy approach is a problem-solving strategy used in algorithms and optimization, where decisions are made by selecting the best available option at each step, without considering the overall effect of those decisions. The greedy approach aims to find an optimal solution by making a series of locally optimal choices.

Key characteristics of a greedy approach include:

1. Local Optimization: At each step, the greedy algorithm makes a choice that appears to be the best option among those available. This choice is based solely on the current information without any consideration of future consequences.

2. Irreversibility: Greedy choices are generally not revisited or undone in later stages of the algorithm. Once a decision is made, it is considered final.

3. Simplicity: Greedy algorithms are typically straightforward and easy to implement. They involve simple rules or heuristics for making decisions.

4. Efficiency: Greedy algorithms are often efficient in terms of time complexity because they make simple decisions at each step.

5. Suboptimal Solutions: While greedy algorithms provide a solution quickly, they may not always yield the globally optimal solution. In some cases, they can produce solutions that are close to optimal but not guaranteed to be the absolute best.

Examples of Greedy Algorithms:

1. **Greedy Coin Change**: In the problem of making change with the fewest coins, a greedy approach would involve selecting the largest coin denomination at each step. While this usually works, it may not always yield the minimum number of coins for change.

2. **Dijkstra's Shortest Path Algorithm**: Dijkstra's algorithm for finding the shortest path in a weighted graph employs a greedy approach. It repeatedly selects the node with the smallest tentative distance to the starting point and explores its neighbors. This algorithm is guaranteed to work for non-negative edge weights.

3. **Prim's Minimum Spanning Tree**: Prim's algorithm builds a minimum spanning tree by iteratively selecting the edge with the smallest weight that connects a vertex in the tree with a vertex outside the tree. It guarantees a minimum spanning tree for graphs with non-negative edge weights.

4. **Fractional Knapsack**: As explained earlier, the Fractional Knapsack problem is solved using a greedy approach by selecting items with the highest value-to-weight ratios at each step.

It's important to note that while greedy algorithms are useful and efficient for many problems, they may not be appropriate for all situations. The choice of a greedy approach depends on the specific problem and its characteristics. In some cases, additional constraints or more complex algorithms may be required to find the optimal solution. Greedy algorithms are a valuable tool in an algorithm designer's toolkit, but they need to be used judiciously with an understanding of their limitations.
"""
