first_queen_row = 0
first_queen_col = 0

def print_board(board):
    n = len(board)
    for i in range(n):
        for j in range(n):
            print(board[i][j], end=" ")
        print()

def is_safe(row, col, slashCode, backslashCode, rowLookup, slashCodeLookup, backslashCodeLookup):
    if (slashCodeLookup[slashCode[row][col]] or backslashCodeLookup[backslashCode[row][col]] or rowLookup[row]):
        return False
    return True

def solve_n_queens(board, col, slashCode, backslashCode, rowLookup, slashCodeLookup, backslashCodeLookup):
    n = len(board)

    if col >= n:
        # All queens are placed, return True
        return True
    
    if col == first_queen_col:
        # First queen is placed, move to next column
        return solve_n_queens(board, col + 1, slashCode, backslashCode, rowLookup, slashCodeLookup, backslashCodeLookup)

    # Try placing the queen in each row of the current column
    for i in range(n):
        if i != first_queen_row and is_safe(i, col, slashCode, backslashCode, rowLookup, slashCodeLookup, backslashCodeLookup):
            # Place the queen
            board[i][col] = 1
            rowLookup[i] = True
            slashCodeLookup[slashCode[i][col]] = True
            backslashCodeLookup[backslashCode[i][col]] = True
            
            # Recur to place the rest of the queens
            if solve_n_queens(board, col + 1, slashCode, backslashCode, rowLookup, slashCodeLookup, backslashCodeLookup):
                return True

            # If placing the queen in board[i][col] doesn't lead to a solution, backtrack
            board[i][col] = 0
            rowLookup[i] = False
            slashCodeLookup[slashCode[i][col]] = False
            backslashCodeLookup[backslashCode[i][col]] = False

    return False

def main():
    n = 8  # Change 'n' to the desired board size
    board = [[0 for _ in range(n)] for _ in range(n)]

    # Place the first queen at
    board[first_queen_row][first_queen_col] = 1
    
    # Helper matrices 
    slashCode = [[0 for i in range(n)] for j in range(n)]
    backslashCode = [[0 for i in range(n)] for j in range(n)]
     
    # Arrays to tell us which rows are occupied 
    rowLookup = [False] * n
     
    # Keep two arrays to tell us which diagonals are occupied 
    x = 2 * n - 1
    slashCodeLookup = [False] * x
    backslashCodeLookup = [False] * x
    
    # Initialize helper matrices 
    for rr in range(n):
        for cc in range(n):
            slashCode[rr][cc] = rr + cc
            backslashCode[rr][cc] = rr - cc + n - 1
    
    # Update the board and matrices based on the first queen's placement
    rowLookup[first_queen_row] = True
    slashCode[first_queen_row][first_queen_col] = first_queen_row + first_queen_col
    backslashCode[first_queen_row][first_queen_col] = first_queen_row - first_queen_col + n - 1
    slashCodeLookup[first_queen_row + first_queen_col] = True
    backslashCodeLookup[first_queen_row - first_queen_col + n - 1] = True
     
    if(solve_n_queens(board, 0, slashCode, backslashCode, rowLookup, slashCodeLookup, backslashCodeLookup) == False):
        print("Solution does not exist")
        return False
    
    # Solution found 
    print_board(board)
    return True

if __name__ == "__main__":
    main()

# Time Complexity:
# 1. The main part of the code is the `solve_n_queens` function, which uses a backtracking algorithm to find a solution to the N-Queens problem.
# 2. In the worst case, the algorithm explores all possible combinations of queen placements on the board.
# 3. The time complexity is O(n!), where n is the size of the board. This is because there are n possibilities for placing the queen in the first column, n-1 possibilities for the second column, and so on.

# Space Complexity:
# 1. The primary space-consuming data structures in the code are the `board` matrix, `slashCode`, `backslashCode`, `rowLookup`, `slashCodeLookup`, and `backslashCodeLookup` arrays.
# 2. The space complexity is O(n^2) for the `board`, `slashCode`, and `backslashCode` matrices.
# 3. The `rowLookup`, `slashCodeLookup`, and `backslashCodeLookup` arrays have a space complexity of O(n).
# 4. Overall, the space complexity is O(n^2) + O(n) + O(n) = O(n^2).

# In summary, the time complexity of the code is exponential (O(n!)) due to the nature of the N-Queens problem, and the space complexity is quadratic (O(n^2)) because of the chessboard and related data structures. This code efficiently explores possible solutions using backtracking, and the time complexity grows rapidly with the board size.

"""
The N-Queens problem is a classical combinatorial problem in chessboard-based puzzles. It asks for a placement of N chess queens on an N×N chessboard, in such a way that no two queens threaten each other. This means that no two queens can be in the same row, column, or diagonal. The goal is to find all distinct solutions to the problem, or sometimes just one solution.

Here are some key points about the N-Queens problem:

1. **Chessboard Setup:** The problem is typically presented on an N×N chessboard, where N is the number of queens to be placed.

2. **Valid Solutions:** In a valid solution, no two queens share the same row, column, or diagonal. This means that there is exactly one queen in each row and each column.

3. **Constraints:** The problem is constrained by the requirement that queens must not attack each other. A queen can attack any piece in its row, column, and along both diagonals.

4. **Search Algorithms:** Solving the N-Queens problem involves using various search and optimization algorithms. Backtracking algorithms, such as recursive depth-first search, are commonly employed to find solutions. Constraint programming and other heuristic-based methods can also be used.

5. **Solution Count:** For larger N values, the problem can have multiple solutions. Finding all distinct solutions is a common goal in solving the N-Queens problem.

6. **Symmetry and Rotations:** Solutions to the N-Queens problem often have rotational symmetry. This means that if a solution is found, several other solutions can be generated by rotating the board or mirroring it.

7. **Applications:** While the N-Queens problem is often considered a recreational puzzle, it has practical applications in various fields, including computer science, artificial intelligence, and operations research. It serves as a useful example for testing and evaluating search and optimization algorithms.

8. **Complexity:** The N-Queens problem can become computationally challenging as N increases. The problem's time complexity grows exponentially with N, making it suitable for benchmarking the performance of search and optimization algorithms.

9. **Extensions:** There are variations of the N-Queens problem, such as the N-Queens completion problem, where some queens are pre-placed, and the goal is to complete the board with additional queens.

Solving the N-Queens problem involves searching for valid queen placements on the chessboard while adhering to the constraints that no two queens threaten each other. Finding solutions can be achieved through various algorithms, and the problem remains a classic puzzle and a fascinating challenge in computer science and mathematics.

---------------------------------

Branch and Bound is a widely used algorithmic technique for solving optimization problems, particularly in combinatorial and discrete domains. It systematically explores the solution space by dividing it into smaller subproblems and bounding the search to find the best possible solution efficiently. It is often used when the problem cannot be solved using greedy or dynamic programming approaches. Here's an explanation of the Branch and Bound technique:

1. **Optimization Problems:** Branch and Bound is primarily used for optimization problems, where the goal is to find the best solution among a set of possible solutions. These problems often involve maximizing or minimizing an objective function under certain constraints.

2. **Systematic Search:** The key idea behind Branch and Bound is to explore the solution space in a systematic manner, similar to a tree search. It involves branching and bounding the search space to efficiently find the optimal solution.

3. **Main Components:**
   - **Branching:** At each node of the search tree, the algorithm makes branching decisions to divide the problem into smaller subproblems. These decisions often involve selecting one of several possible choices for a variable or element of the solution.
   - **Bounding:** The algorithm establishes bounds or estimates for each node in the search tree, allowing it to determine whether the subproblem at that node has the potential to lead to a better solution than the current best solution found. This helps in pruning unfruitful branches.
   - **Selection:** Branch and Bound maintains a priority queue or a list of nodes to be explored, and it selects nodes based on their bounds and estimates to ensure that more promising nodes are explored first.
   - **Completion:** The algorithm continues to branch and bound until it has explored the entire search tree or until the bounds of remaining unexplored nodes are worse than the best solution found so far.

4. **Termination and Pruning:** The algorithm terminates when it has explored the entire search space or when it determines that there cannot be a better solution than the current best solution. This pruning is achieved by comparing the bounds of nodes with the best solution found so far and skipping those nodes that are guaranteed to be suboptimal.

5. **Applications:** Branch and Bound can be applied to various optimization problems, including:
   - Traveling Salesman Problem (TSP)
   - 0/1 Knapsack Problem
   - Job Scheduling
   - Graph Coloring
   - Cutting Stock Problem
   - Combinatorial Auctions
   - Integer Linear Programming

6. **Complexity Analysis:** The efficiency of Branch and Bound depends on the problem's characteristics and the quality of the bounding function. In the worst case, it explores all nodes in the search tree, resulting in exponential time complexity. However, effective bounding strategies and heuristics can greatly improve its efficiency.

7. **Trade-offs:** Branch and Bound may not always guarantee the optimal solution, but it is designed to find good solutions efficiently. The quality of the solution found can depend on the quality of bounding estimates and the branching strategy used.

8. **Variations:** There are variations of Branch and Bound, such as Branch and Bound with Subproblems, which is used to solve larger problems by dividing them into smaller subproblems that can be solved optimally.

In summary, Branch and Bound is a powerful technique for solving optimization problems. It systematically explores the solution space by dividing it into smaller subproblems and bounding the search to find the best possible solution efficiently, making it a valuable tool in combinatorial and discrete optimization.
"""
