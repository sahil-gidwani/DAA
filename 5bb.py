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
