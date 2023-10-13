import java.util.PriorityQueue;

class Node implements Comparable<Node> {
    int level;
    int profit;
    int weight;
    double bound;

    Node(int level, int profit, int weight) {
        this.level = level;
        this.profit = profit;
        this.weight = weight;
    }

    @Override
    public int compareTo(Node other) {
        return Double.compare(other.bound, this.bound);
    }
}

class BranchAndBoundKnapsack {
    public static double knapsack(int capacity, int[] weights, int[] values, int n) {
        PriorityQueue<Node> priorityQueue = new PriorityQueue<>();
        Node u, v;

        // Initialize the root node.
        u = new Node(-1, 0, 0);
        u.bound = computeBound(u, capacity, weights, values, n);

        double maxProfit = 0.0;

        // Add the root node to the priority queue.
        priorityQueue.add(u);

        while (!priorityQueue.isEmpty()) {
            // Get the highest bound node.
            u = priorityQueue.poll();

            if (u.bound > maxProfit) {
                int level = u.level + 1;

                // Include the next item.
                v = new Node(level, u.profit + values[level], u.weight + weights[level]);
                v.bound = computeBound(v, capacity, weights, values, n);

                if (v.weight <= capacity && v.profit > maxProfit) {
                    maxProfit = v.profit;
                }

                if (v.bound > maxProfit) {
                    priorityQueue.add(v);
                }

                // Exclude the next item.
                v = new Node(level, u.profit, u.weight);
                v.bound = computeBound(v, capacity, weights, values, n);

                if (v.bound > maxProfit) {
                    priorityQueue.add(v);
                }
            }
        }

        return maxProfit;
    }

    public static double computeBound(Node node, int capacity, int[] weights, int[] values, int n) {
        if (node.weight >= capacity) {
            return 0;
        }

        double bound = node.profit;
        int j = node.level + 1;
        int totalWeight = node.weight;

        while (j < n && totalWeight + weights[j] <= capacity) {
            totalWeight += weights[j];
            bound += values[j];
            j++;
        }

        if (j < n) {
            bound += (capacity - totalWeight) * ((double) values[j] / weights[j]);
        }

        return bound;
    }

    public static void main(String[] args) {
        int capacity = 10;
        int[] weights = {2, 1, 3, 2};
        int[] values = {12, 10, 20, 15};
        int n = weights.length;

        double maxValue = knapsack(capacity, weights, values, n);
        System.out.println("Maximum value that can be obtained: " + maxValue);
    }
}
