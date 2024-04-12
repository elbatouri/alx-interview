#!/usr/bin/python3
""" N queens """
import sys


def print_solution(queens_positions):
    """ Print the solution """
    print([[i, j] for i, j in enumerate(queens_positions)])


def is_safe(row, col, queens_positions):
    """ Check if placing a queen at position (row, col) is safe """
    for i in range(row):
        if queens_positions[i] == col or \
           queens_positions[i] - i == col - row or \
           queens_positions[i] + i == col + row:
            return False
    return True


def solve(n, row, queens_positions):
    """ Recursive function to solve N queens problem """
    if row == n:
        print_solution(queens_positions)
        return
    for col in range(n):
        if is_safe(row, col, queens_positions):
            queens_positions[row] = col
            solve(n, row + 1, queens_positions)


def nqueens(n):
    """ Main function to solve N queens problem """
    if n < 4:
        print("N must be at least 4")
        exit(1)
    queens_positions = [-1] * n
    solve(n, 0, queens_positions)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        exit(1)
    nqueens(n)
