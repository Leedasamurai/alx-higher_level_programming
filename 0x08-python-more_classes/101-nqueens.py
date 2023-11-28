#!/usr/bin/python3
"""Solves the N-queens puzzle."""

import sys

def init_board(n):
    """Initialize an `n`x`n` sized chessboard with 0's."""
    board = [[' ' for _ in range(n)] for _ in range(n)]
    return board

def board_deepcopy(board):
    """Return deepcopy of a chessboard."""
    if isinstance(board, list):
        return list(map(board_deepcopy, board))
    return board

def get_solution(board):
    """Return list of lists representation of a solved chessboard."""
    solution = [[r, c] for r in range(len(board)) for c in range(len(board)) if board[r][c] == "Q"]
    return solution

def xout(board, row, col):
    """X out spots on a chessboard where non-attacking queens can no longer be placed."""

    for c in range(col + 1, len(board)):
        board[row][c] = "x"

    for c in range(col - 1, -1, -1):
        board[row][c] = "x"

    for r in range(row + 1, len(board)):
        board[r][col] = "x"

    for r in range(row - 1, -1, -1):
        board[r][col] = "x"

    c = col + 1
    for r in range(row + 1, len(board)):
        if c >= len(board):
            break
        board[r][c] = "x"
        c += 1

    c = col - 1
    for r in range(row - 1, -1, -1):
        if c < 0:
            break
        board[r][c]
        c -= 1

    c = col + 1
    for r in range(row - 1, -1, -1):
        if c >= len(board):
            break
        board[r][c] = "x"
        c += 1

    c = col - 1
    for r in range(row + 1, len(board)):
        if c < 0:
            break
        board[r][c] = "x"
        c -= 1

def recursive_solve(board, row, queens, solutions):
    """Recursively solve an N-queens puzzle."""
    if queens == len(board):
        solutions.append(get_solution(board))
        return solutions

    for col in range(len(board)):
        if board[row][col] == " ":
            tmp_board = board_deepcopy(board)
            tmp_board[row][col] = "Q"
            xout(tmp_board, row, col)
            solutions = recursive_solve(tmp_board, row + 1, queens + 1, solutions)

    return solutions

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit("Error: Invalid number of arguments")

    if not sys.argv[1].isdigit() or int(sys.argv[1]) < 4:
        sys.exit("Error: N must be a positive integer greater than or equal to 4")

    N = int(sys.argv[1])
    board = init_board(N)
    solutions = recursive_solve(board, 0, 0, [])

    for sol in solutions:
        print(sol)
