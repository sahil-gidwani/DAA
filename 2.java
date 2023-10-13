import java.util.Comparator;
import java.util.PriorityQueue;

class HuffmanNode {
    char data;
    int frequency;
    HuffmanNode left, right;

    HuffmanNode(char data, int frequency) {
        this.data = data;
        this.frequency = frequency;
        left = right = null;
    }
}

class MyComparator implements Comparator<HuffmanNode> {
    public int compare(HuffmanNode x, HuffmanNode y) {
        return x.frequency - y.frequency;
    }
}

class HuffmanEncoding {
    public static void printCodes(HuffmanNode root, String code) {
        if (root == null) {
            return;
        }

        if (root.data != '$') {
            System.out.println(root.data + ":" + code);
        }

        printCodes(root.left, code + "0");
        printCodes(root.right, code + "1");
    }

    public static void buildHuffmanTree(char[] data, int[] freq, int n) {
        PriorityQueue<HuffmanNode> minHeap = new PriorityQueue<>(n, new MyComparator());

        for (int i = 0; i < n; i++) {
            HuffmanNode node = new HuffmanNode(data[i], freq[i]);
            minHeap.add(node);
        }

        while (minHeap.size() > 1) {
            HuffmanNode left = minHeap.poll();
            HuffmanNode right = minHeap.poll();

            HuffmanNode parent = new HuffmanNode('$', left.frequency + right.frequency);
            parent.left = left;
            parent.right = right;

            minHeap.add(parent);
        }

        HuffmanNode root = minHeap.poll();
        printCodes(root, "");
    }

    public static void main(String[] args) {
        char[] data = { 'a', 'b', 'c', 'd', 'e', 'f' };
        int[] freq = { 5, 9, 12, 13, 16, 45 };
        int n = data.length;

        buildHuffmanTree(data, freq, n);
    }
}
