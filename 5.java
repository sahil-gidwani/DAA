public class NQueensWithFirstQueenPlaced {
    public static void printBoard(int[][] board) {
        int n = board.length;
        System.out.println();
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                System.out.print(board[i][j] + " ");
            }
            System.out.println();
        }
    }

    public static boolean isSafe(int[][] board, int row, int col) {
        int n = board.length;

        // Check left side of the current row
        for (int i = 0; i < col; i++) {
            if (board[row][i] == 1) {
                return false;
            }
        }

        // Check upper diagonal on the left side
        for (int i = row, j = col; i >= 0 && j >= 0; i--, j--) {
            if (board[i][j] == 1) {
                return false;
            }
        }

        // Check lower diagonal on the left side
        for (int i = row, j = col; i < n && j >= 0; i++, j--) {
            if (board[i][j] == 1) {
                return false;
            }
        }

        return true;
    }

    public static boolean solveNQueens(int[][] board, int col) {
        int n = board.length;

        if (col >= n) {
            // All queens are placed, return true
            return true;
        }

        // Try placing the queen in each row of the current column
        for (int i = 0; i < n; i++) {
            if (isSafe(board, i, col)) {
                // Place the queen
                board[i][col] = 1;

                // Recur to place the rest of the queens
                if (solveNQueens(board, col + 1)) {
                    return true;
                }

                // If placing the queen in board[i][col] doesn't lead to a solution, backtrack
                board[i][col] = 0;
            }
        }

        return false;
    }

    public static void main(String[] args) {
        int n = 8; // Change 'n' to the desired board size
        int[][] board = new int[n][n];

        // Place the first queen at (0, 0)
        board[0][0] = 1;

        // Call the backtracking function to solve the rest of the board
        if (solveNQueens(board, 1)) {
            System.out.println("Solution exists:");
            printBoard(board);
        } else {
            System.out.println("No solution exists.");
        }
    }
}
