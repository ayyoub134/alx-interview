#!/usr/bin/env python3
import sys

def is_safe(board, row, col, N):
    # Check if there's a queen in the same column
    for i in range(row):
        if board[i] == col:
            return False

    # Check upper left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i] == j:
            return False

    # Check upper right diagonal
    for i, j in zip(range(row, -1, -1), range(col, N)):
        if board[i] == j:
            return False

    return True

def solve_nqueens(N):
    def backtrack(row, board):
        if row == N:
            # Print the current solution
            solution = [[i, board[i]] for i in range(N)]
            print(solution)
            return

        for col in range(N):
            if is_safe(board, row, col, N):
                board[row] = col
                backtrack(row + 1, board)
                # backtrack step
                board[row] = -1

    # Initialize board
    board = [-1] * N
    backtrack(0, board)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve_nqueens(N)

