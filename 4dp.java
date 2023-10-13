public class ZeroOneKnapsack {
    public static int knapsack(int capacity, int[] weights, int[] values, int n) {
        int[][] dp = new int[n + 1][capacity + 1];

        for (int i = 0; i <= n; i++) {
            for (int w = 0; w <= capacity; w++) {
                if (i == 0 || w == 0) {
                    dp[i][w] = 0;
                } else if (weights[i - 1] <= w) {
                    dp[i][w] = Math.max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w]);
                } else {
                    dp[i][w] = dp[i - 1][w];
                }
            }
        }

        return dp[n][capacity];
    }

    public static void main(String[] args) {
        int capacity = 10;
        int[] weights = {2, 1, 3, 2};
        int[] values = {12, 10, 20, 15};
        int n = weights.length;

        int maxValue = knapsack(capacity, weights, values, n);
        System.out.println("Maximum value that can be obtained: " + maxValue);
    }
}
