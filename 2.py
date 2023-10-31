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
