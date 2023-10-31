import heapq
from collections import defaultdict

# Node class for building the Huffman tree
class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

# Function to build the Huffman tree
def build_huffman_tree(data):
    # Count character frequencies
    frequency = defaultdict(int)
    for char in data:
        frequency[char] += 1

    # Create a priority queue (min heap) of nodes
    priority_queue = [Node(char, freq) for char, freq in frequency.items()]
    heapq.heapify(priority_queue)

    # Build the Huffman tree
    while len(priority_queue) > 1:
        left = heapq.heappop(priority_queue)
        right = heapq.heappop(priority_queue)
        parent = Node(None, left.freq + right.freq)
        parent.left, parent.right = left, right
        heapq.heappush(priority_queue, parent)

    return priority_queue[0]

# Function to encode the data
def huffman_encoding(data):
    if not data:
        return "", None

    root = build_huffman_tree(data)
    encoding_map = {}
    encoded_data = ""

    def build_huffman_codes(node, code=""):
        if node:
            if node.char is not None:
                encoding_map[node.char] = code
            build_huffman_codes(node.left, code + "0")
            build_huffman_codes(node.right, code + "1")

    build_huffman_codes(root)

    for char in data:
        encoded_data += encoding_map[char]

    return encoded_data, root

# Function to decode the data
def huffman_decoding(data, tree):
    if not data or not tree:
        return ""
    decoded_data = ""
    current_node = tree

    for bit in data:
        if bit == "0":
            current_node = current_node.left
        else:
            current_node = current_node.right

        if current_node.char is not None:
            decoded_data += current_node.char
            current_node = tree

    return decoded_data

# Example usage
if __name__ == "__main__":
    data = "this is an example for huffman encoding"
    encoded_data, huffman_tree = huffman_encoding(data)
    decoded_data = huffman_decoding(encoded_data, huffman_tree)

    print(f"Original data: {data}")
    print(f"Encoded data: {encoded_data}")
    print(f"Decoded data: {decoded_data}")

# Time Complexity Analysis:
# - Building the Huffman tree: O(n*log(n)), where n is the number of unique characters.
# - Encoding data: O(m), where m is the length of the input data.
# - Decoding data: O(m), where m is the length of the encoded data.
# Overall time complexity: O(n*log(n)) + O(m) + O(m), which simplifies to O(n*log(n) + m).

# Space Complexity Analysis:
# - Storing character frequencies: O(n), where n is the number of unique characters.
# - Priority queue (min heap): O(n) to store nodes.
# - Encoding map: O(n) to store Huffman codes.
# - Encoded data: O(m), where m is the length of the input data.
# Overall space complexity: O(n + n + n + m), which simplifies to O(n + m).

"""
**Huffman Coding** is a widely used data compression algorithm that is capable of encoding and decoding data in a lossless manner. It was developed by David A. Huffman in 1952. The main idea behind Huffman coding is to assign shorter codes to more frequent characters and longer codes to less frequent characters, reducing the average length of the encoded data. Huffman coding is commonly used in file compression formats like ZIP, as well as in data transmission protocols.

Here's a step-by-step explanation of how Huffman coding works for encoding and decoding:

**Encoding:**
1. **Frequency Analysis:** In the encoding process, the first step is to analyze the input data to determine the frequency of each character (or symbol) that needs to be encoded. The more frequent a character, the shorter its Huffman code will be.

2. **Build Huffman Tree:** Next, a Huffman tree (also known as a Huffman encoding tree) is constructed. This is a binary tree where each leaf node represents a character and its frequency, and internal nodes represent the sum of the frequencies of their children. The tree is built by repeatedly merging the two nodes with the lowest frequencies, creating a new internal node as their parent, until there is only one node left, which becomes the root of the tree.

3. **Assign Codes:** To create Huffman codes, you traverse the Huffman tree from the root to each leaf node. When you move left in the tree, you append a '0' to the code, and when you move right, you append a '1'. The resulting codes for each character are unique and variable in length.

4. **Encode Data:** Finally, you encode the input data by replacing each character with its corresponding Huffman code. The encoded data is typically a binary string, where the Huffman codes are concatenated to represent the original data.

**Decoding:**
1. **Huffman Tree:** To decode the data, you need the same Huffman tree that was used for encoding. It's crucial to have the original tree structure to map the Huffman codes back to their respective characters.

2. **Decode Data:** Starting at the root of the Huffman tree, you read the encoded data bit by bit. When you encounter a '0', you move left in the tree, and when you encounter a '1', you move right. You continue this process until you reach a leaf node, which represents a character. That character is the decoded output. You then start over at the root to decode the next character in the input data.

**Advantages of Huffman Coding:**
- Huffman codes are variable-length and prefix-free, meaning no code is the prefix of another, making decoding unambiguous.
- It provides an efficient way to compress data, particularly when the input has variable symbol frequencies.

**Limitations of Huffman Coding:**
- Huffman encoding requires transmitting the tree structure alongside the encoded data, which can add overhead.
- It may not be the most efficient compression method for all types of data. Other algorithms, like Lempel-Ziv-Welch (LZW), are better for certain data patterns.

Huffman coding is a fundamental concept in data compression and forms the basis for many modern compression techniques. It's widely used in applications where efficient data storage and transmission are essential, such as in file compression, image compression, and data communication.
"""
