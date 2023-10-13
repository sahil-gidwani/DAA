import java.util.Arrays;
import java.util.Comparator;

class Item {
    int weight;
    int value;
    double valuePerWeight;

    Item(int weight, int value) {
        this.weight = weight;
        this.value = value;
        this.valuePerWeight = (double) value / weight;
    }
}

class FractionalKnapsack {
    public static double fractionalKnapsack(int capacity, Item[] items) {
        Arrays.sort(items, Comparator.comparingDouble((Item item) -> item.valuePerWeight).reversed());

        double totalValue = 0.0;
        int remainingCapacity = capacity;

        for (Item item : items) {
            if (item.weight <= remainingCapacity) {
                totalValue += item.value;
                remainingCapacity -= item.weight;
            } else {
                totalValue += (item.valuePerWeight * remainingCapacity);
                break;
            }
        }

        return totalValue;
    }

    public static void main(String[] args) {
        int capacity = 50;
        Item[] items = {
            new Item(10, 60),
            new Item(20, 100),
            new Item(30, 120)
        };

        double maxValue = fractionalKnapsack(capacity, items);
        System.out.println("Maximum value that can be obtained: " + maxValue);
    }
}
