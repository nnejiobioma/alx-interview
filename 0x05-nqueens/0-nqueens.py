#!/usr/bin/python3
"""
Puzzle to Solving
N Queens Problem using backtracking
"""
import sys


def printSolution(board, N):
    """allocated positions
    to the queen
    """
    solution = []

    for r in range(N):
        for i in range(N):
            if i == board[z]:
                solution.append([z, i])
    print(solution)


def is_position_safe(board, z, i, row):
    """The position is
    safe for the queen
    """
    return board[z] in (i, i - z + row, z - row + i)


def recursive_solve(board, row, N):
    """safe positions where
    the queen can be allocated
    """
    if row == N:
        printSolution(board, N)

    else:
        for i in range(n):
            allowed = True
            for z in range(row):
                if is_position_safe(board, z, i, row):
                    allowed = False
            if allowed:
                board[row] = i
                recursive_solve(board, row + 1, n)


def create_board(size):
    """Generates the board gamein other to
    resolve the issue
    """
    return [0 * size for i in range(size)]


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    N = int(sys.argv[1])
    myboard = create_board(N)
    solutions = recursive_solve(myboard, 0, N)
