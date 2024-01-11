#!/usr/bin/python3
"""N queens"""
import sys


def is_safe(board, row, col, n):
    """
    Check if it is safe to place a queen on a given position in the chessboard.

    Parameters:
    - board (list): The current state of the
    chessboard, represented as a list of integers.
    - row (int): The row index of the position to check.
    - col (int): The column index of the position to check.
    - n (int): The size of the chessboard.

    Returns:
    - bool: True if it is safe to place a queen
    at the given position, False otherwise.
    """
    # Check if there is a queen in the same row
    for i in range(col):
        if board[i] == row or \
           board[i] - i == row - col or \
           board[i] + i == row + col:
            return False
    return True


def solve_nqueens_util(board, col, n, solutions):
    """
    Generate all possible solutions for the N-Queens problem.

    Args:
        board (list): A list representing the current state of the chessboard.
        col (int): The current column being considered for queen placement.
        n (int): The number of queens and board size.
        solutions (list): A list to store all possible solutions.

    Returns:
        None
    """
    if col == n:
        solutions.append([i for i in board])
        return

    for i in range(n):
        if is_safe(board, i, col, n):
            board[col] = i
            solve_nqueens_util(board, col + 1, n, solutions)


def solve_nqueens(n):
    """
    Generates a function comment for the given function body.

    Parameters:
        n (int): The size of the chessboard and the number of queens.

    Returns:
        None
    """
    if not isinstance(n, int):
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1] * n
    solutions = []
    solve_nqueens_util(board, 0, n, solutions)

    for solution in solutions:
        print([[i, solution[i]] for i in range(n)])


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
        solve_nqueens(N)
    except ValueError:
        print("N must be a number")
        sys.exit(1)